#!/bin/sh
# Run once per fresh session: installs the Anton font and checks Inter + ffmpeg.
cd "$(dirname "$0")" && npm install --no-save @fontsource/anton >/dev/null 2>&1
ls /usr/share/fonts/opentype/inter/Inter-Bold.otf >/dev/null 2>&1 || echo "Inter font missing: install fonts-inter"
which ffmpeg >/dev/null || echo "ffmpeg missing"
python3 -c "import PIL, numpy" || echo "pip install pillow numpy --break-system-packages"
