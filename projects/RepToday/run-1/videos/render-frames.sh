#!/bin/bash
# Deterministic frame renderer: drives frame.html's window.seek(ms) and screenshots each frame.
# Usage: ./render-frames.sh <dir> <duration_ms> [fps]
# Example: ./render-frames.sh launch 40000 12
set -euo pipefail
DIR="$(cd "$(dirname "$0")/$1" && pwd)"
DUR_MS="$2"
FPS="${3:-12}"
FRAMES=$(( DUR_MS * FPS / 1000 ))
mkdir -p "$DIR/frames"
chrome-devtools-axi resize 1280 720 >/dev/null
chrome-devtools-axi open "file://$DIR/frame.html" >/dev/null
sleep 1.5
for (( i=0; i<FRAMES; i++ )); do
  ms=$(( i * 1000 / FPS ))
  chrome-devtools-axi eval "window.seek($ms)" >/dev/null
  chrome-devtools-axi screenshot "$DIR/frames/$(printf 'f%04d' $i).png" >/dev/null
  if (( i % 60 == 0 )); then echo "[$1] frame $i/$FRAMES"; fi
done
echo "[$1] done: $FRAMES frames in $DIR/frames"
