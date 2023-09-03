from bark.generation import load_codec_model, generate_text_semantic
from encodec.utils import convert_audio
from hubert_manager import HuBERTManager
from custom_hubert import CustomHubert
from custom_tokenizer import CustomTokenizer
import torchaudio
import os

import torch
import numpy as np

audio_filepath = input("Enter the audio filepath (e.g. ./source/tate.wav): ")
voice_name = input("Enter the voice name (e.g. en_tate_1):") 
device = input("Enter the device (cuda or cpu): ")

if(device != 'cuda' and device != 'cpu'):
    print("Invalid device. Defaulting to cpu.")
    device = 'cpu'
folder_path= 'export_model'
output_path = ''+ folder_path + '/' + voice_name + '.npz'

isExist = os.path.exists(folder_path)
if not isExist:
    os.makedirs(folder_path)
    print("Created folder: " + folder_path)

if(device == 'cuda'):
    print("Torch version:", torch.version)
    print("CUDA available:", torch.cuda.is_available())
    print("Number of GPUs:", torch.cuda.device_count())
    print("GPU name:", torch.cuda.get_device_name(0))

model = load_codec_model(use_gpu=True if device == 'cuda' else False)

hubert_manager = HuBERTManager() 
hubert_manager.make_sure_hubert_installed() 
hubert_manager.make_sure_tokenizer_installed() 

tokenizer = CustomTokenizer.load_from_checkpoint('data/models/hubert/tokenizer.pth', map_location=torch.device('cpu')).to(device)  # Automatically uses the right layers
hubert_model = CustomHubert(checkpoint_path='data/models/hubert/hubert.pt').to(device)

wav, sr = torchaudio.load(audio_filepath) 
wav = convert_audio(wav, sr, model.sample_rate, model.channels) 
wav = wav.to(device) 

semantic_vectors = hubert_model.forward(wav, input_sample_hz=model.sample_rate)
semantic_tokens = tokenizer.get_token(semantic_vectors)

with torch.no_grad(): 
    encoded_frames = model.encode(wav.unsqueeze(0)) 
    codes = torch.cat([encoded[0] for encoded in encoded_frames], dim=-1).squeeze() 


codes = codes.cpu().numpy() 
semantic_tokens = semantic_tokens.cpu().numpy() 

np.savez(output_path, fine_prompt=codes, coarse_prompt=codes[:2, :], semantic_prompt=semantic_tokens) 
