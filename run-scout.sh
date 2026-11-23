#!/usr/bin/env bash
# run-scout.sh: apply Claude's feedback from the inbox, run the scout, and deliver
# the digest to the private inbox repository if one is set up.
# Called by the two-line ~/run-scout.sh stub, which first pulls this repository.
# Usage:  bash ~/run-scout.sh            (any scout options can follow, e.g. --no-video)
set -euo pipefail

REPO="$HOME/timeline"           # read-only copy of github.com/ai-takeoff/timeline
WORK="$HOME/scout"              # output and memory: scout-out/ lives here
INBOX="$HOME/timeline-inbox"    # copy of the private inbox repository (optional)
APPLIED="$WORK/feedback-applied.txt"

source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate scout
grep -m1 '^VERSION' "$REPO/scout.py"
cd "$WORK"; touch "$APPLIED"

if [ -d "$INBOX/.git" ]; then
  git -C "$INBOX" pull -q --ff-only || true
  echo "== Applying feedback from the inbox"
  for f in "$INBOX"/feedback/*.txt; do
    [ -e "$f" ] || continue
    name=$(basename "$f")
    grep -qxF "$name" "$APPLIED" && continue
    # Data only: accept lines that are exactly five hex characters, ignore everything else.
    ids=$(grep -oxE '[0-9a-f]{5}' "$f" | tr '\n' ' ' || true)
    if [ -n "$ids" ]; then
      # shellcheck disable=SC2086
      python "$REPO/scout.py" --out "$WORK/scout-out" --useful $ids
    fi
    echo "$name" >> "$APPLIED"
  done
fi

echo "== Running"
python "$REPO/scout.py" "$@" 2>&1 | tee "$WORK/last-run.log"

ZIP=$(ls -t "$WORK"/scout-out/*.zip | head -1)
RUNDIR="$WORK/scout-out/$(basename "$ZIP" .zip)"

if [ -d "$INBOX/.git" ]; then
  echo "== Delivering to the inbox"
  cp "$ZIP" "$INBOX/"
  cp "$RUNDIR/digest.md" "$INBOX/latest-digest.md"
  git -C "$INBOX" add -A
  git -C "$INBOX" commit -q -m "Digest $(basename "$ZIP" .zip)" || echo "(nothing new to commit)"
  git -C "$INBOX" pull -q --rebase || true
  git -C "$INBOX" push -q
  echo "Delivered: $(basename "$ZIP")"
else
  echo "No inbox set up; attach this file by hand: $ZIP"
fi
