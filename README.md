# 🚀 YOLOv11 Object Detection Project

This repository contains scripts to **train** and **run inference** using a custom-trained **YOLOv11** model from Ultralytics.

## 📦 About

- `train_yolo11l.py`: Script to train the YOLOv11 model using a custom dataset.
- `run_inference.py`: Script to run inference on images or a folder of images using the trained model.
- `data.yaml`: Dataset configuration file that defines paths and class names.

---

## 🏋️ How to Train

To train your YOLOv11 model:

```bash
python train_yolo11l.py
```

Make sure your `data.yaml` is configured and your dataset is structured properly.

---

## 🔍 How to Run Inference

To run predictions on an image or a folder of images:

```bash
python run_inference.py
```

The predictions will be saved to the `inference_output/predict/` folder.

---

## ✅ Requirements

Install dependencies:

```bash
pip install ultralytics
```

---

## 📁 Dataset Format

```
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

---

## 📄 Example data.yaml

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: gold_coin
  1: gold_bar
```

---

## 📤 Export Model (Optional)

You can export the trained model after training using:

```python
model.export(format="onnx", imgsz=1024)
```

---

For more details, refer to [Ultralytics Docs](https://docs.ultralytics.com).
