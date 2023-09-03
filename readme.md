# Hackathon TTS

## Description

Some scripts based on the bark model that can generate speach models and audio files.

## Installation

Must have

- Ubuntu 22.04
- python 3.10
- CUDA 11.7

Install `distutils` and `distutils-extra`:

```
sudo apt-get update
sudo apt-get install python3-distutils python3-distutils-extra
```

Install `bark`

```
pip install bark
```

1. Run `pip install -r requirements.txt` to install the required packages.
2. Run the `generate_model.py` script for generating the model.
3. Run the `generate_audio_from_model.py` script for generating the audio files.
