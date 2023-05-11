import os
import tkinter as tk
import turtle
import sounddevice as sd
import soundfile as sf
import datetime
import librosa
from main import predict_mic

def start_turtle():
    t.pendown()

s = turtle.getscreen()

t = turtle.Turtle()
size = t.turtlesize()
increase = (2 * num for num in size)
t.turtlesize(*increase)


# Create the boxes
left_box = turtle.Turtle()
left_box.shape("square")
left_box.color("blue")
left_box.shapesize(stretch_wid=3, stretch_len=3)
left_box.penup()
left_box.goto(-100, 0)

right_box = turtle.Turtle()
right_box.shape("square")
right_box.color("blue")
right_box.shapesize(stretch_wid=3, stretch_len=3)
right_box.penup()
right_box.goto(100, 0)

up_box = turtle.Turtle()
up_box.shape("square")
up_box.color("blue")
up_box.shapesize(stretch_wid=3, stretch_len=3)
up_box.penup()
up_box.goto(0, 100)

down_box = turtle.Turtle()
down_box.shape("square")
down_box.color("blue")
down_box.shapesize(stretch_wid=3, stretch_len=3)
down_box.penup()
down_box.goto(0, -100)

def start_function():
    print("Start button clicked!")
    start_turtle()

    # Start recording audio
    duration = 1  # seconds
    fs = 16000  # sampling rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    
    sd.wait()  # Wait for the recording to finish
    recording = recording.mean(axis=1)  # Convert to mono audio
    
    # Save the cleaned audio as a WAV file
    filename = "recording_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    sf.write("./files/"+filename, recording, fs)
    
    # Perform other tasks with the cleaned audio, such as prediction
    prediction = predict_mic(filename)
    # Reset box colors
    left_box.color("blue")
    right_box.color("blue")
    up_box.color("blue")
    down_box.color("blue")

    if prediction == 'left':
        left_box.color("red")
    elif prediction == 'right':
        right_box.color("red")
    elif prediction == 'up':
        up_box.color("red")
    elif prediction == 'down':
        down_box.color("red")


    #Delete the recorded audio file
    os.remove("./files/" + filename)


root = tk.Tk()

start_button = tk.Button(root, text="Choose", command=start_function)
start_button.pack()


root.mainloop()


