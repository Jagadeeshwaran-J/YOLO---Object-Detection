# 🚀 YOLOv11 Custom Object Detection Project

This repository provides everything you need to **train** and **run inference** on a **YOLOv11** model from [Ultralytics](https://docs.ultralytics.com), specifically for your **custom object detection** tasks.

---

## 📁 Project Structure

```
.
├── Yolo_Model_Train.py          # Train your custom YOLOv11 model
├── Image_Inference.py           # Run inference on image folder
├── Video_Inference.py           # Run inference on a video file
├── Webcam_Inference.py          # Real-time webcam detection
├── data.yaml                    # Dataset configuration
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── input-images/                # Test images for inference
├── video-output/                # Output for video inference
├── image-output/                # Output for image inference
└── README.md
```

---

## ✅ Requirements

Install Ultralytics:

```bash
pip install ultralytics
```

---

## 📁 Dataset Format

Your dataset must follow this structure:

```
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Each `.jpg`/`.png` image must have a corresponding `.txt` label file in YOLO format.

---

## 📝 Configure `data.yaml`

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: object_0
  1: object_1
```

- Update `names:` with your object class names.
- Make sure `path:` matches your dataset location.

---

## 🏋️ Train the Model

Run the training script:

```bash
python Yolo_Model_Train.py
```

- You can modify the pretrained model (`yolo11l.pt`), epochs, batch size, optimizer, etc.

> ✅ The best model is saved and exported to ONNX format automatically.

---

## 🖼️ Run Inference on Images

1. Place your test images in `input-images/`
2. Run:

```bash
python Image_Inference.py
```

Results will be saved in the `image-output/predict/` folder.

---

## 🎞️ Run Inference on Video

Place your input video as `input-video.mp4`, then run:

```bash
python Video_Inference.py
```

Results will be saved in `video-output/predict/`.

---

## 📷 Real-Time Webcam Inference

Use your system webcam (GPU/CPU will be auto-detected):

```bash
python Webcam_Inference.py
```

---

## 📤 Export Trained Model

You can export your model to ONNX format like this:

```python
model.export(format="onnx", imgsz=1024)
```

---

## 📚 References

- [Ultralytics Docs](https://docs.ultralytics.com)
- [YOLO Format Explained](https://docs.ultralytics.com/tasks/detect/#annotating-data)

---

## 💡 Tips

- Use `exist_ok=True` to overwrite old runs.
- Tune learning rate, batch size, and augmentations based on your dataset.
