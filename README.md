# Kokoro TTS CLI

A command-line tool for synthesizing speech using the **Kokoro TTS** model powered by ONNX. Supports multiple languages and voices for realistic, expressive text-to-speech synthesis.

---

## 📦 Features

- 🔊 High-quality voice synthesis via ONNX-based Kokoro TTS
- 🌍 Multilingual support (English, Japanese, Mandarin, Portuguese, and more)
- 🗣️ Dozens of expressive voices
- ⚙️ Adjustable speech speed
- 💾 Save output as a .wav file
- 📜 Easily list available languages and voices

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Linux

## 📦 Installation

### Download as a portable tool 

Click [here](https://github.com/natanael-b/kokoro-tts-cli/releases/download/continuous/kokoro-tts-cli)

Right click -> Propertes -> Mark as executable

### Install on system


Right click -> Propertes -> Mark as executable

```bash
wget https://github.com/natanael-b/kokoro-tts-cli/releases/download/continuous/kokoro-tts-cli -O kokoro-tts-cli;
chmod +x kokoro-tts-cli;
sudo mkdir -p /usr/local/bin;
sudo mv kokoro-tts-cli /usr/local/bin;
```
##### Remove from system

```bash
sudo rm /usr/local/bin/kokoro-tts-cli;
```

## 📈 Usage

### Basic Example

```bash
kokoro-tts-cli --text "Olá mundo!" --voice pf_dora --lang pt-br --output my_audio.wav
```

### List Available Languages

```bash
kokoro-tts-cli --list-langs
```

### List Available Voices

```bash
kokoro-tts-cli --list-voices
```

### Adjust Speech Speed

```bash
kokoro-tts-cli --text "Estou falando muito rápido!" --speed 1.5
```

### Output to Specific File

```bash
kokoro-tts-cli --output my_audio.wav
```


