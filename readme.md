# Hackathon TTS

## Description

Some scripts based on the bark model that can generate speach models and audio files.

## Installation

Must have

- Ubuntu 22.04
- python 3.10
- CUDA 11.7

### Install packages`

```
sudo apt-get update
sudo apt-get install python3-distutils python3-distutils-extra
pip install bark tensorboardX ipython audiolm_pytorch
```

### Go to folder

```
cd {path}
```

Run `pip install -r requirements.txt` to install the required packages.

## Usage

1. Run the script for generating the model.

```
python3.10 generate_model.py
```

2. Run the script for generating the audio files.

```
python3.10 generate_audio_from_model.py
```
