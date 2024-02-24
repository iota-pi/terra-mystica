#!/usr/bin/env bash
set -euo pipefail

set -a
if [[ -f .secrets.* ]]; then
  source .secrets.*
fi
set +a
docker compose $@
