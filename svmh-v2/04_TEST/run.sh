#!/usr/bin/env bash
# Run the whole static suite against ../03_BUILD.
# Exits non-zero if any check fails. Writes reports/latest.txt.
set -uo pipefail

cd "$(dirname "$0")"
mkdir -p reports

PY=${PYTHON:-python3}
REPORT=reports/latest.txt

{
  echo "SVMH v2 verification — $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "build: $(cd ../03_BUILD && pwd)"
} > "$REPORT"

fail=0
for t in static/test_*.py; do
  if ! "$PY" "$t" >> "$REPORT" 2>&1; then
    fail=$((fail + 1))
  fi
done

# Serve check: every page and asset must answer 200 over HTTP, not just exist
# on disk. Uses its own port so it never collides with the dev server.
PORT=${PORT:-8099}
( cd ../03_BUILD && exec "$PY" -m http.server "$PORT" >/dev/null 2>&1 ) &
SERVER=$!
trap 'kill "$SERVER" 2>/dev/null' EXIT
sleep 1

{
  echo ""
  echo "=== http"
} >> "$REPORT"

http_fail=0
while IFS= read -r path; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "http://localhost:$PORT/$path")
  if [ "$code" != "200" ]; then
    echo "  FAIL  $code $path" >> "$REPORT"
    http_fail=$((http_fail + 1))
  fi
done < <(cd ../03_BUILD && find . -type f \
           \( -name '*.html' -o -name '*.css' -o -name '*.js' \
              -o -name '*.jpg' -o -name '*.png' \) \
           -not -path '*/.*' | sed 's|^\./||')

if [ "$http_fail" -eq 0 ]; then
  echo "  PASS  every page and asset returns 200" >> "$REPORT"
else
  fail=$((fail + 1))
fi

{
  echo ""
  if [ "$fail" -eq 0 ]; then
    echo "RESULT: all suites passed"
  else
    echo "RESULT: $fail suite(s) failed"
  fi
} >> "$REPORT"

cat "$REPORT"
exit "$fail"
