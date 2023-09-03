from bark.api import generate_audio
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav


from transformers import BertTokenizer
from bark.generation import SAMPLE_RATE, preload_models, codec_decode, generate_coarse, generate_fine, generate_text_semantic

# Enter your prompt and speaker here
text_prompt = input("Enter your text prompt:")
voice_name = input("Enter your custom voice name (e.g. bark/en_tate_1.npz):")
filepath =input("Enter the output filepath (e.g. ./output/audio.wav):")

preload_models(
    text_use_gpu=True,
    text_use_small=False,
    coarse_use_gpu=True,
    coarse_use_small=False,
    fine_use_gpu=True,
    fine_use_small=False,
    codec_use_gpu=True,
    force_reload=False,
)

audio_array = generate_audio(text_prompt, history_prompt=voice_name, text_temp=0.7, waveform_temp=0.7)
Audio(audio_array, rate=SAMPLE_RATE)

write_wav(filepath, SAMPLE_RATE, audio_array)
