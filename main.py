import numpy as np
import wave
from tensorflow.keras import models

from tf_helper import preprocess_audiobuffer


started = False
stopped = True
# !! Modify this in the correct order
commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']


loaded_model = models.load_model("saved_model")


def predict_mic(filename):
    with wave.open("./files/"+filename, 'rb') as wav_file:
        # Get basic information about the .wav file
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Read audio data from the .wav file
        audio_data = wav_file.readframes(num_frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        print("data",audio_array)
        # print("data shape",data.shape)
        spec = preprocess_audiobuffer(audio_array)
# stopped=True
        prediction = loaded_model(spec)
        label_pred = np.argmax(prediction, axis=1)

        command = commands[label_pred[0]]
        print("Predicted label:", command)
        # move_turtle(command)

        return command

if __name__ == "__main__":
    from turtle_helper import move_turtle
    while stopped:
        # command = predict_mic()
        print("nothing")
        command ="up"
        move_turtle(command)
        if command == "stop":
            stopped = False
            # terminate()
            break