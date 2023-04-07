#!/bin/bash

PYTHON_VERSION="3.10.0"
PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz"

if command -v python3 >/dev/null; then
    echo "Python is already installed."
else
    echo "Python not found. Downloading and installing..."
    mkdir -p ~/.python
    cd ~/.python
    curl -O $PYTHON_URL
    tar -xzf Python-${PYTHON_VERSION}.tgz
    cd Python-${PYTHON_VERSION}
    ./configure --prefix=$HOME/.python/${PYTHON_VERSION}
    make -j$(nproc)
    make install
    echo "Python has been installed."
fi