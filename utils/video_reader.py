import cv2
import os

path_res = "/home/zhengziang/zaspace/projects/ugv_draw/video/res"

path_base = "/home/zhengziang/zaspace/projects/ugv_draw/video"

path_video = os.path.join(path_base, "ugv.mp4")

path_video_ai = os.path.join(path_base, "ai_gen.mp4")

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

def accelerate_video(input_video_path, output_video_path, acceleration_factor):
    # Open the input video file
    input_video = cv2.VideoCapture(input_video_path)
    
    # Get the video properties
    fps = input_video.get(cv2.CAP_PROP_FPS)
    frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_video_path, fourcc, int(fps * acceleration_factor), (frame_width, frame_height))
    
    # Read and write frames with acceleration
    frame_number = 0
    while input_video.isOpened():
        ret, frame = input_video.read()
        if not ret:
            break
        
        # Write every nth frame, where n is the acceleration factor
        # if frame_number % acceleration_factor == 0:
        output_video.write(frame)
        
        frame_number += 1
    
    # Release video objects
    input_video.release()
    output_video.release()
    
    print("Video acceleration complete.")

def delete_frames(input_video_path, frames_to_remove = [10, 20, 30], out_put_video_path='output_video.mp4'):
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Open an output video file
    output_video_path = os.path.join(path_res, 'output_video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Read and write each frame
    frame_index = 0
    tmp_frame = None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f"End with {frame_index}")
            break
        
        # Skip frames to be removed
        if frame_index not in frames_to_remove:
            out.write(frame)
            # tmp_frame = frame
        # else:
        #     out.write(tmp_frame)
            
        frame_index += 1

    # Release the video capture and writer objects
    cap.release()
    out.release()

    print("Video processing complete. Output saved to", output_video_path)
    return

path_frame_saved = "/home/zhengziang/zaspace/projects/ugv_draw/figure/frames_2"

def extract_frames(input_video_path, frames_to_save = [10, 20, 30]):
    cap = cv2.VideoCapture(input_video_path)

    # Read and write each frame
    frame_index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f"End with {frame_index}.")
            break
        
        # Skip frames to be removed
        if frame_index in frames_to_save:
            cv2.imwrite(os.path.join(path_frame_saved, f"frame_{frame_index}.png"), frame)
            
        frame_index += 1

    # Release the video capture and writer objects
    cap.release()
    return

def replace_frames(input_video_path, replace_video_path, output_video_path, start_frame=180, end_frame=None):
    cap_source = cv2.VideoCapture(input_video_path)
    cap_rep = cv2.VideoCapture(replace_video_path)

    # Get video properties
    frame_width = int(cap_source.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap_source.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_source = int(cap_source.get(cv2.CAP_PROP_FPS))
    total_frames_source = int(cap_source.get(cv2.CAP_PROP_FRAME_COUNT))

    total_frames_rep = int(cap_rep.get(cv2.CAP_PROP_FRAME_COUNT))

    end_frame = end_frame if end_frame is not None else start_frame + total_frames_rep - 1

    # output_video_path = os.path.join(path_res, 'output_video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps_source, (frame_width, frame_height))

    frame_index = 0
    while cap_source.isOpened():
        ret, frame = cap_source.read()
        if not ret:
            print(f"End with {frame_index}")
            break
        if frame_index >= start_frame and frame_index < end_frame:
            ret, frame = cap_rep.read()
        out.write(frame)
        frame_index += 1

    cap_source.release()
    cap_rep.release()
    out.release()

    return

if __name__ == "__main__":

    # frames = list(range(210, 220, 1)) + list(range(230, 240, 1))
    # frames = list(range(180, 220, 2)) + [221, 222, 224, 225, 226, 227] +  list(range(230, 240, 1))
    # frame_to_repeat = [239]
    # frames = list(range(222, 245, 2))

    # delete_frames(path_video, frames)

    # extract_frames(path_video, frames)

    replace_frames(path_video, path_video_ai, os.path.join(path_res, "rep_ai.mp4"))

    pass
