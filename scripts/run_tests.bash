#!/usr/bin/env bash

PYTEST_ARGUMENTS=${@:-tests/test_big_website.py}

#ALLURE_RESULTS_DIR=allure-results


docker build -t headless_image .

# Run Selenium py.test with script arguments
#    -v $(pwd)/headless_image/$ALLURE_RESULTS_DIR:/code/$ALLURE_RESULTS_DIR \
docker run --rm \
    -e PYTHONPATH=/code/ \
    headless_image \
    "$PYTEST_ARGUMENTS"