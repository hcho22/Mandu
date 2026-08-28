#!/usr/bin/env bash
# claimlint.sh - marketing-speak and placeholder linter for launch/ assets.
# Rule: no sentence should survive swapping the product name out; every quality
# claim travels with a number or a file path. This linter greps for the words
# that only appear in sentences violating that rule, plus build-failure placeholders.
# Usage: claimlint.sh <file-or-dir>...   Exit 1 on any hit.
set -u
fail=0

# Generic-praise vocabulary: if one of these appears, the sentence almost
# certainly survives a product-name swap. Case-insensitive, word-ish match.
BANNED_MARKETING=(
  "world-class" "best-in-class" "state-of-the-art" "cutting-edge" "next-generation"
  "revolutionary" "game-chang" "blazing" "lightning-fast" "seamless" "effortless"
  "frictionless" "supercharge" "unlock the" "unleash" "empower" "elevate your"
  "delightful" "magical" "10x your" "transform your" "innovative" "unparalleled"
  "industry-leading" "enterprise-grade" "battle-tested" "robust and" "powerful and"
  "trusted by thousands" "loved by" "turnkey" "game changer" "paradigm"
  "leverage the power" "harness the power" "take your .* to the next level"
)

# Claims the product's own docs forbid: golden-set-authoring.md calls
# single-family evals a weaker proof "you must not cite to a client as proven".
BANNED_OVERCLAIM=(
  "proven secure" "provably secure" "guaranteed secure" "zero-trust" "bulletproof"
  "unhackable" "military-grade" "100% secure" "never leaks" "leak-proof platform"
)

# Placeholders are build failures per the brief.
PLACEHOLDERS=("lorem ipsum" "TODO" "TKTK" "FIXME" "XXX" "placeholder image" "coming soon" "INSERT_" "\\[TBD\\]")

scan() {
  local label="$1"; shift
  local pattern
  for pattern in "$@"; do
    # shellcheck disable=SC2086
    hits=$(grep -rinE --include='*.md' --include='*.html' --include='*.txt' --include='*.svg' "$pattern" "${TARGETS[@]}" 2>/dev/null | grep -v 'launch/bin/claimlint' | grep -v 'CLAIMLINT-ALLOW')
    if [ -n "$hits" ]; then
      echo "[$label] pattern '$pattern':"
      echo "$hits"
      fail=1
    fi
  done
}

TARGETS=("$@")
[ ${#TARGETS[@]} -eq 0 ] && TARGETS=("$(dirname "$0")/..")

scan "MARKETING-SPEAK" "${BANNED_MARKETING[@]}"
scan "OVERCLAIM" "${BANNED_OVERCLAIM[@]}"
scan "PLACEHOLDER" "${PLACEHOLDERS[@]}"

if [ "$fail" -eq 0 ]; then
  echo "claimlint: clean"
fi
exit "$fail"
