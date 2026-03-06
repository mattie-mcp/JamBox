#!/bin/bash
set -euo pipefail

API="http://localhost:8000"

echo "=== JamBox Integration Test ==="

# Health check
echo -n "Health check... "
curl -sf "$API/health" | grep -q "ok" && echo "PASS" || echo "FAIL"

# Auth status
echo -n "Auth status... "
curl -sf "$API/auth/status" && echo " PASS" || echo " FAIL"

# Create mapping
echo -n "Create mapping... "
RESULT=$(curl -sf -X POST "$API/api/mappings" \
  -H "Content-Type: application/json" \
  -d '{"tag_id":"TEST:TAG:01","spotify_uri":"spotify:track:test","name":"Test Song"}')
echo "$RESULT" | grep -q "Test Song" && echo "PASS" || echo "FAIL"
ID=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# List mappings
echo -n "List mappings... "
curl -sf "$API/api/mappings" | grep -q "TEST:TAG:01" && echo "PASS" || echo "FAIL"

# Delete mapping
echo -n "Delete mapping... "
curl -sf -X DELETE "$API/api/mappings/$ID" -o /dev/null -w "%{http_code}" | grep -q "204" && echo "PASS" || echo "FAIL"

echo "=== Done ==="
