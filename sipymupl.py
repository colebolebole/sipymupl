# Importing the modules
import pygame
import tkinter as tk
from tkinter import filedialog

# Initializing pygame mixer
pygame.mixer.init()

# Creating the main window
window = tk.Tk()
window.title("Simple Music Player")
window.geometry("300x100")

# Creating a label to display the song name
song_label = tk.Label(window, text="No song selected")
song_label.pack()

# Creating a status bar to display the song status
status_bar = tk.Label(window, text="Stopped", relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Defining a function to load a song
def load_song():
    # Getting the song file path
    song_path = filedialog.askopenfilename()
    # Loading the song into pygame mixer
    pygame.mixer.music.load(song_path)
    # Updating the song label with the song name
    song_name = song_path.split("/")[-1]
    song_label.config(text=song_name)

# Defining a function to play the song
def play_song():
    # Playing the song with pygame mixer
    pygame.mixer.music.play()
    # Updating the status bar with the song status
    status_bar.config(text="Playing")

# Defining a function to stop the song
def stop_song():
    # Stopping the song with pygame mixer
    pygame.mixer.music.stop()
    # Updating the status bar with the song status
    status_bar.config(text="Stopped")

# Defining a function to pause the song
def pause_song():
    # Pausing the song with pygame mixer
    pygame.mixer.music.pause()
    # Updating the status bar with the song status
    status_bar.config(text="Paused")

# Defining a function to resume the song
def resume_song():
    # Resuming the song with pygame mixer
    pygame.mixer.music.unpause()
    # Updating the status bar with the song status
    status_bar.config(text="Playing")

# Creating a button to load a song
load_button = tk.Button(window, text="Load", command=load_song)
load_button.pack(side=tk.LEFT)

# Creating a button to play the song
play_button = tk.Button(window, text="Play", command=play_song)
play_button.pack(side=tk.LEFT)

# Creating a button to stop the song
stop_button = tk.Button(window, text="Stop", command=stop_song)
stop_button.pack(side=tk.LEFT)

# Creating a button to pause the song
pause_button = tk.Button(window, text="Pause", command=pause_song)
pause_button.pack(side=tk.LEFT)

# Creating a button to resume the song
resume_button = tk.Button(window, text="Resume", command=resume_song)
resume_button.pack(side=tk.LEFT)

# Running the main loop
window.mainloop()