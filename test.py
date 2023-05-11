
# import display
import numpy as np
from tf_helper import preprocess_audiobuffer
from tensorflow.keras import models

import wave

commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']


loaded_model = models.load_model("saved_model")

with wave.open("/home/ahmed/Downloads/New_Downloads/Realisation des commandes vocales/recording_20230511_000925.wav", 'rb') as wav_file:
    num_frames = wav_file.getnframes()

        # Read audio data from the .wav file
    audio_data = wav_file.readframes(num_frames)
    
    audio_array = np.frombuffer(audio_data, dtype=np.int16)
    # display.display(display.Audio(waveform, rate=16000))

    # get_spectrogram(waveform)
    spec = preprocess_audiobuffer(audio_array)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)

    command = commands[label_pred[0]]
    print("Predicted label:", command)