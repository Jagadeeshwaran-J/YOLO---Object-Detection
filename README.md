# 🚀 YOLOv11 Object Detection Project

This repository allows you to **train** and **run inference** using the latest **YOLOv11** model from [Ultralytics](https://docs.ultralytics.com). It is designed for custom object detection tasks.

---

## 📂 Project Structure

```
.
├── Yolo_Model_Train.py          # Training script using YOLOv11
├── Yolo_Model_Inference.py      # Inference script using trained model
├── data.yaml                    # Dataset configuration file
├── dataset/                     # Your custom dataset folder
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── input_images/                # Folder of images for inference
└── inference_output/            # Output folder for predictions
```

---

## ✅ Requirements

Install the required dependency:

```bash
pip install ultralytics
```

---

## 📁 Dataset Format

Organize your dataset as follows:

```
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Each image should have a corresponding `.txt` label file in YOLO format.

---

## 📝 Configure `data.yaml`

Create a `data.yaml` file in the root directory:

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: object_0
  1: object_1
```

- Update `names:` to reflect your own class names.
- Ensure `path:` points to your dataset folder.

---

## 🏋️‍♂️ How to Train the Model

Once your dataset and `data.yaml` are ready, run:

```bash
python Yolo_Model_Train.py
```

⚙️ **What you can customize:**
- Replace `yolo11l.pt` in the script with a different pretrained checkpoint if needed (e.g., `yolo11x.pt` for a larger model).
- Adjust training settings inside `Yolo_Model_Train.py` like `epochs`, `batch`, or `optimizer`.

After training, the best model is saved automatically and exported as an ONNX file.

---

## 🔍 How to Run Inference

After training, use the model to make predictions:

1. Put test images into the `input_images/` folder.
2. Run the script:

```bash
python Yolo_Model_Inference.py
```

This will load the `yolo11l.pt` model and run predictions.

✏️ **To customize:**
- Change the model path in `Yolo_Model_Inference.py` (`model_path = "yolo11l.pt"`) if using a different checkpoint.
- You can also modify `input_path` to point to a single image like `"image.jpg"` instead of a folder.

---

## 📤 Export the Trained Model

Your best model is automatically exported to ONNX format at the end of training:

```python
model.export(format="onnx", imgsz=1024)
```

---

## 📚 References

- [Ultralytics YOLO Docs](https://docs.ultralytics.com)
- [YOLO Format Explained](https://docs.ultralytics.com/tasks/detect/#annotating-data)

---

## 🧠 Tips

- Use `exist_ok=True` to overwrite old results during re-training or re-inference.
- You can fine-tune training parameters like `lr0`, `weight_decay`, and `batch` depending on your dataset size.

