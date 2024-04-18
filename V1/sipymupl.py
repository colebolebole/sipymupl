# Import pygame and os modules
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Create a list of music files in the current directory
music_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

# Sort the music files alphabetically
music_files.sort()

# Create a variable to store the current index of the music file
current_index = 0

# Load the first music file and play it
pygame.mixer.music.load(music_files[current_index])
pygame.mixer.music.play()

# Create a loop to handle user input
while True:
    # Print the current music file and the status
    print(f'Now playing: {music_files[current_index]}')
    print(f'Status: {"Playing" if pygame.mixer.music.get_busy() else "Paused"}')

    # Get the user input
    command = input('Enter a command (next, prev, play, pause, stop, quit): ')

    # Handle the command
    if command == 'next':
        # Increment the current index and wrap around if necessary
        current_index = (current_index + 1) % len(music_files)

        # Load and play the next music file
        pygame.mixer.music.load(music_files[current_index])
        pygame.mixer.music.play()
    elif command == 'prev':
        # Decrement the current index and wrap around if necessary
        current_index = (current_index - 1) % len(music_files)

        # Load and play the previous music file
        pygame.mixer.music.load(music_files[current_index])
        pygame.mixer.music.play()
    elif command == 'play':
        # Resume playing the music file if paused
        pygame.mixer.music.unpause()
    elif command == 'pause':
        # Pause playing the music file if playing
        pygame.mixer.music.pause()
    elif command == 'stop':
        # Stop playing the music file and reset the index
        pygame.mixer.music.stop()
        current_index = 0
    elif command == 'quit':
        # Quit the program
        break
    else:
        # Print an invalid command message
        print('Invalid command. Please try again.')