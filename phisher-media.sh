#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${PHISHER_URL:-http://127.0.0.1:5000}"

banner() {
  clear
  cat <<'EOF'
╔══════════════════════════════════════════╗
║              PHISHER v1.0               ║
║              ROOT L00T                   ║
║       SECURITY AWARENESS LAB             ║
╚══════════════════════════════════════════╝
EOF
}

while true; do
  banner
  cat <<'EOF'
[1] Instagram training page
[2] Facebook training page
[3] X training page
[4] LinkedIn training page
[5] Google training page
[6] Generic social-media training page
[7] Campaign statistics
[8] JSON report
[0] Exit
EOF
  printf '\nSelect option: '
  read -r choice
  case "$choice" in
    1) curl -fsS "$BASE_URL/simulate/instagram" || true; read -r -p $'\nPress Enter...' _ ;;
    2) curl -fsS "$BASE_URL/simulate/facebook" || true; read -r -p $'\nPress Enter...' _ ;;
    3) curl -fsS "$BASE_URL/simulate/x" || true; read -r -p $'\nPress Enter...' _ ;;
    4) curl -fsS "$BASE_URL/simulate/linkedin" || true; read -r -p $'\nPress Enter...' _ ;;
    5) curl -fsS "$BASE_URL/simulate/google" || true; read -r -p $'\nPress Enter...' _ ;;
    6) curl -fsS "$BASE_URL/simulate/generic" || true; read -r -p $'\nPress Enter...' _ ;;
    7) curl -fsS "$BASE_URL/report" | python3 -m json.tool || true; read -r -p $'\nPress Enter...' _ ;;
    8) curl -fsS "$BASE_URL/report" || true; read -r -p $'\nPress Enter...' _ ;;
    0) exit 0 ;;
    *) echo "Invalid option"; sleep 1 ;;
  esac
done
