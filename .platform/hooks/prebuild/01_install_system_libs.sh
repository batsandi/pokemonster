#!/bin/bash

echo "=== Installing system packages ==="

dnf install -y \
  zlib \
  zlib-devel \
  libjpeg-turbo \
  libjpeg-turbo-devel \
  gcc \
  python3-devel \
  make \
  findutils