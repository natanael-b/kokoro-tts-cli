#!/usr/bin/env bash

HERE="$(dirname "$(readlink -f "${0}")")"

rm kokoro-tts-cli

cd "${HERE}/models"

wget -c https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
wget -c https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

cd ..

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

files=($(/usr/bin/ls ${HERE}))

mkdir -p "AppDir"

for file in ${files[@]};do
  cp -rf "${file}" "AppDir"
done

chmod +x "AppDir/AppRun"

wget https://github.com/AppImage/type2-runtime/releases/download/continuous/runtime-$(arch)

mksquashfs AppDir/ base

cat runtime-$(arch) base > kokoro-tts-cli

rm -rf AppDir base runtime-$(arch) venv models/kokoro-v1.0.onnx models/voices-v1.0.bin