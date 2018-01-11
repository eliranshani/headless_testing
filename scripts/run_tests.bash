#!/usr/bin/env bash

PYTEST_ARGUMENTS=${@:-tests/test_websites_titles.py --headless=true}

docker build -t headless_image .

docker run --rm \
    -e PYTHONPATH=/code/ \
    headless_image \
    "$PYTEST_ARGUMENTS"