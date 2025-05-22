import argparse
import soundfile as sf
import numpy as np
from kokoro_onnx import Kokoro
from os import environ

model_dir = environ.get("HERE", "")

LANGS = {
    "American English": "en-us",
    "British English": "en-gb",
    "Japanese": "ja",
    "Mandarin Chinese": "zh",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Italian": "it",
    "Brazilian Portuguese": "pt-br",
}

VOICES = {
    "en-us": [
        "af_heart", "af_alloy", "af_aoede", "af_bella", "af_jessica",
        "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah",
        "af_sky", "am_adam", "am_echo", "am_eric", "am_fenrir",
        "am_liam", "am_michael", "am_onyx", "am_puck", "am_santa",
    ],
    "en-gb": [
        "bf_alice", "bf_emma", "bf_isabella", "bf_lily",
        "bm_daniel", "bm_fable", "bm_george", "bm_lewis",
    ],
    "ja": [
        "jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro", "jm_kumo",
    ],
    "zh": [
        "zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi",
        "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang",
    ],
    "es": [
        "ef_dora", "em_alex", "em_santa",
    ],
    "fr": [
        "ff_siwis",
    ],
    "hi": [
        "hf_alpha", "hf_beta", "hm_omega", "hm_psi",
    ],
    "it": [
        "if_sara", "im_nicola",
    ],
    "pt-br": [
        "pf_dora", "pm_alex", "pm_santa",
    ],
}

def main():
    parser = argparse.ArgumentParser(description="Speech generation using the Kokoro TTS model.")
    parser.add_argument("--text", type=str, default="Hello! This is a demonstration of Kokoro TTS using Dora's voice.", help="Text to synthesize.")
    parser.add_argument("--voice", type=str, default="pf_dora", help="Voice to be used.")
    parser.add_argument("--lang", type=str, default="pt-br", help="Language of the speech.")
    parser.add_argument("--speed", type=float, default=1.0, help="Speech speed.")
    parser.add_argument("--output", type=str, default="output.wav", help="Path to save the output file.")
    parser.add_argument("--list-langs", action="store_true", help="List available languages and exit.")
    parser.add_argument("--list-voices", action="store_true", help="List available voices and exit.")

    args = parser.parse_args()

    # List languages and voices, if requested
    if args.list_langs:
        print("Languages:")
        for name, code in LANGS.items():
            print(f" - {name} ({code})")
        return

    if args.list_voices:
        print("Voices:")
        for lang_code, voice_list in VOICES.items():
            print(f"  {lang_code}:")
            for voice in voice_list:
                print(f"    - {voice}")
        return

    # Initialize the Kokoro model
    kokoro = Kokoro(
      model_dir + "/models/kokoro-v1.0.onnx",
      model_dir + "/models/voices-v1.0.bin"
    )

    # Generate audio
    audio, sample_rate = kokoro.create(args.text, voice=args.voice, lang=args.lang, speed=args.speed)

    # Save the audio to a WAV file
    sf.write(args.output, audio, sample_rate)
    print(f"Audio saved as '{args.output}'.")

if __name__ == "__main__":
    main()
