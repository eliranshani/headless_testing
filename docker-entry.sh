#!/usr/bin/env bash

py.test $@ &
pid="$!"

trap "echo '=== Stopping PID $pid ==='; kill -SIGTERM $pid" SIGINT SIGTERM

wait $pid