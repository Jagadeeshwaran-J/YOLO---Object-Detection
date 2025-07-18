from ultralytics import YOLO
import torch

# Automatically use GPU if available, else fallback to CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load your trained YOLO model
model = YOLO("best.pt")  # Replace with your actual model path

# Run real-time webcam inference
model.predict(
    source=0,           # 0 = default webcam
    imgsz=720,          # Use 720p for quality and speed balance
    conf=0.3,           # Confidence threshold
    device=device,      # Use selected device
    show=True,          # Show live webcam with detections
    stream=False,       # Set True to control frame-by-frame (if needed)
    verbose=False       # Suppress logging for smooth display
)
