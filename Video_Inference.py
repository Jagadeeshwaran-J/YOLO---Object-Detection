from ultralytics import YOLO
import os

# --- Configuration ---
model_path = "best.pt"               # Path to your trained model
video_path = "input-video.mp4"       # Path to the input video file
output_folder = "video-output"       # Folder to save results

# --- Create output folder ---
os.makedirs(output_folder, exist_ok=True)

# --- Load model ---
model = YOLO(model_path)

# --- Run inference on video ---
results = model.predict(
    source=video_path,
    save=True,
    project=output_folder,
    name="predict",
    exist_ok=True
)

print(f"🎉 Inference complete. Video saved to: {os.path.join(output_folder, 'predict')}")
