# Hackathon TTS

## Description

Some scripts based on the bark model that can generate speach models and audio files.

## Installation

Must have

- Ubuntu 22.04
- python 3.10
- CUDA 11.7

## Docker

<<<<<<< HEAD
For running in Docker use following scripts and scip Install packages

```
cd {path}
sudo docker build -t image-name:tts_test .
```

### Install packages

````
=======
```bash
>>>>>>> 5e013c159af6f95d5f805dbe192e5bf4f9b484cd
sudo apt-get update
sudo apt-get install python3-distutils python3-distutils-extra
pip install bark tensorboardX ipython audiolm_pytorch
````

Go to folder

```bash
cd {path}
```

Run to install the required packages.

```
pip install -r requirements.txt
```

## Usage

1. Run the script for generating the model.

```bash
python3.10 generate_model.py
```

2. Run the script for generating the audio files.

```bash
python3.10 generate_audio_from_model.py
```
