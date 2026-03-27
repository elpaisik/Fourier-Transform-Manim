pi#!/usr/bin/env bash
set -euo pipefail

# Debian/Ubuntu prerequisites for manim/manimpango
if [[ "$(uname)" == "Linux" ]]; then
  echo "Installiere System-Abhängigkeiten for manim/manimpango + OpenCV + ffmpeg..."
  sudo apt-get update || true
  sudo apt-get install -y \
    pkg-config \
    libcairo2-dev \
    libpango1.0-dev \
    libgdk-pixbuf2.0-dev \
    libglib2.0-dev \
    libfreetype6-dev \
    libffi-dev \
    ffmpeg \
    libgl1 \
    libglx0 \
    libgl1-mesa-dev \
    libsm6 \
    libxrender1
fi

echo "Python-Abhängigkeiten installieren..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Fertig: requirements installiert."