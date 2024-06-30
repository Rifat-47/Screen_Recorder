import cv2
import numpy as np
import pyautogui

def screen_recorder(filename, duration, fps):
    # Determine the screen size
    screen_size = pyautogui.size()

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, screen_size)

    # Calculate the number of frames to capture based on the duration and fps
    num_frames = int(duration * fps)

    for _ in range(num_frames):
        # Capture the screen
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert the color from RGB to BGR (OpenCV uses BGR by default)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

    # Release the VideoWriter object
    out.release()

if __name__ == "__main__":
    filename = "screen_recording.avi"
    duration = 10  # Duration in seconds
    fps = 20  # Frames per second
    screen_recorder(filename, duration, fps)
