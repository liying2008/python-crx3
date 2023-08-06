#!/usr/bin/env bash

# Run in THIS directory
protoc -I=../src/crx3 --python_out=pyi_out:../src/crx3 ../src/crx3/crx3.proto
