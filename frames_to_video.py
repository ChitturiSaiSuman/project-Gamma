import cv2
import os

# Path to the directory containing the images
image_folder = 'frames'

# Get the list of image filenames
image_files = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])

# Define the video output filename
output_video = 'output_video.mp4'

# Determine the frame width and height from the first image
frame = cv2.imread(os.path.join(image_folder, image_files[0]))
height, width, layers = frame.shape

# Define the frame rate (fps) of the video
fps = 10

# Create a VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID' or other codecs
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Loop through the image files and write each frame to the video
for image_file in image_files:
    img_path = os.path.join(image_folder, image_file)
    frame = cv2.imread(img_path)
    out.write(frame)

# Release the VideoWriter and close the video file
out.release()

print(f"Video saved as {output_video}")
