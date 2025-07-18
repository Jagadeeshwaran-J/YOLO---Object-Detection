from ultralytics import YOLO
import os

# --- Configuration ---
model_path = "best.pt"             # Path to your trained model
input_folder = "input-images"      # Folder with test images
output_folder = "image-output"     # Folder to save results

# --- Create output folder ---
os.makedirs(output_folder, exist_ok=True)

# --- Load model ---
model = YOLO(model_path)

# --- Run inference ---
results = model.predict(
    source=input_folder,
    save=True,
    project=output_folder,
    name="predict",
    exist_ok=True
)

print(f"✅ Inference complete. Results saved to: {os.path.join(output_folder, 'predict')}")
