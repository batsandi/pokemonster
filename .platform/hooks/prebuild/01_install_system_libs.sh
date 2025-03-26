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

echo "=== Checking zlib installation ==="
dnf list installed | grep zlib

echo "=== Checking zlib header file ==="
ls -l /usr/include/zlib.h || echo "zlib.h NOT FOUND"

echo "=== Checking libz.so (zlib shared lib) ==="
find /usr -name 'libz.so*' || echo "libz.so NOT FOUND"