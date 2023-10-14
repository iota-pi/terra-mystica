#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$(realpath "$0")")"

source .env
if [[ -f .secrets.* ]]; then
  source .secrets.*
fi

if [[ "${1:-}" == "build" ]]; then
  docker build \
    -f docker/base.Dockerfile \
    -t "$PYTHON_BASE" \
    --build-arg app_name="$APP_NAME" \
    --build-arg userid="$(id -u)" \
    .
  docker build \
    -f docker/poetry.Dockerfile \
    -t "$PYTHON_POETRY" \
    --build-arg base_image="$PYTHON_BASE" \
    .
  docker build \
    -f docker/test.Dockerfile \
    -t "$DOCKER_TEST" \
    -t "python_docker_dev_base" \
    --build-arg venv_image="$PYTHON_POETRY" \
    .
  docker build \
    -f docker/Dockerfile \
    -t "$DOCKER_MAIN" \
    --build-arg app_name="$APP_NAME" \
    --build-arg base_image="$PYTHON_BASE" \
    --build-arg venv_image="$PYTHON_POETRY" \
    .
fi

if [[ "${1:-}" == "up" ]]; then
  if [[ -n ${2:-} ]]; then
    ./dc.sh up -d "${@:2}"
  else
    ./dc.sh up -d app
  fi
fi

if [[ "${1:-}" == "poetry" ]]; then
  ./dc.sh run --rm --user root poetry poetry "${@:2}"
fi

if [[ "${1:-}" =~ (py)?test ]]; then
  DOCKER_MAIN="${DOCKER_TEST}" \
  ./dc.sh run --rm app python -m pytest "${@:2}"
fi

if [[ "${1:-}" == "format" ]]; then
  DOCKER_MAIN="${DOCKER_TEST}" \
  ./dc.sh run --rm app python -m black .
fi

if [[ "${1:-}" == "check-format" ]]; then
  DOCKER_MAIN="${DOCKER_TEST}" \
  ./dc.sh run --rm app python -m black --check --diff .
fi
