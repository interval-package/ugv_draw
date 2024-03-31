import cv2

def extract_frame(video_path, frame_number, output_path, frame_rate=20):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Get the frames per second (fps) of the video
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    
    # Calculate the frame interval based on the desired frame rate
    frame_interval = fps / frame_rate

    # Set the frame number to the desired frame
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, int(frame_number*frame_interval))
    
    # Read the frame
    success, frame = video_capture.read()
    
    if success:
        # Save the frame as a PNG image
        cv2.imwrite(output_path, frame)
        print(f"fps:{fps}, Frame {frame_number} saved as {output_path}")
    else:
        print("Failed to read the frame")

    # Release the video capture object
    video_capture.release()
