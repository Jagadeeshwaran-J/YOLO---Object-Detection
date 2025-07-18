from ultralytics import YOLO
from pathlib import Path
import os

def run_inference(model_path, input_path, output_dir, imgsz=1024, conf=0.25):
    model = YOLO(model_path)
    os.makedirs(output_dir, exist_ok=True)
    
    results = model.predict(
        source=input_path,
        imgsz=imgsz,
        conf=conf,
        save=True,
        project=output_dir,
        name='predict',
        exist_ok=True
    )
    print(f"Inference completed. Results saved to: {os.path.join(output_dir, 'predict')}")

if __name__ == "__main__":
    model_path = "yolo11l.pt"
    input_path = "input_images/"  # or 'image.jpg'
    output_dir = "inference_output"

    run_inference(model_path, input_path, output_dir)
