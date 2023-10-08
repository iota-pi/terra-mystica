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
    ./dc.sh up -d application
  fi
fi

if [[ "${1:-}" == "poetry" ]]; then
  ./dc.sh run --rm poetry "poetry ${@:2}"
fi

if [[ "${1:-}" =~ (py)?test ]]; then
  DOCKER_MAIN="${DOCKER_TEST}" \
  ./dc.sh run --rm application python -m pytest "${@:2}"
fi

if [[ "${1:-}" == "black" ]]; then
  DOCKER_MAIN="${DOCKER_TEST}" \
  ./dc.sh run --rm application python -m black --check --diff .
fi
