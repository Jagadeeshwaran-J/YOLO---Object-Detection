# 🚀 YOLO Training Parameters & Hyperparameters Guide (YOLOv8 & YOLO11) 🧠

This guide lists all important parameters and hyperparameters used during YOLO model training with explanations and typical default values. These apply to both **YOLOv8** and **YOLO11** models when training on your custom dataset with multiple classes or symbols.

---

## 🚀 1. Basic Training Parameters 🧠

| Parameter        | Description                                                                 | Typical Default Value      |
|------------------|-----------------------------------------------------------------------------|----------------------------|
| `epochs`         | Number of complete passes through the training dataset                      | 100 - 600                  |
| `batch`          | Number of images per training batch                                         | 16 - 128                   |
| `imgsz`          | Input image size (width & height) for training (square)                     | 640                        |
| `device`         | GPU device to use, e.g., `"0"` for first GPU, `"cpu"` for CPU training      | `"0"`                      |
| `data`           | Path to dataset YAML file describing classes and train/val image paths      | `data.yaml`                |
| `model`          | Model config or pretrained weights file (e.g., `yolov8n.pt` or `yolo11l.yaml`) | Pretrained weights or config|
| `project`        | Directory name to save training results and checkpoints                      | `runs/train`               |
| `name`           | Name for the specific training run inside the project directory             | `exp`                      |

---

## 🚀 2. Augmentation Parameters 🧠

| Parameter         | Description                                                           | Typical Default Value |
|-------------------|-----------------------------------------------------------------------|-----------------------|
| `mosaic`          | Enable mosaic augmentation (combines 4 images into 1)                | `True` or `1`          |
| `mixup`           | Mixup augmentation (combines 2 images)                               | `0` (off) or `1`       |
| `hsv_h`           | Hue augmentation amount (color shift)                                | `0.015`                |
| `hsv_s`           | Saturation augmentation amount                                       | `0.7`                  |
| `hsv_v`           | Value (brightness) augmentation amount                              | `0.4`                  |
| `flipud`          | Probability of vertical flip                                         | `0`                    |
| `fliplr`          | Probability of horizontal flip                                       | `0.5`                  |
| `translate`       | Image translation augmentation (fraction of image)                  | `0.1`                  |
| `scale`           | Scale augmentation (zoom in/out)                                    | `0.5` to `1.5`         |
| `shear`           | Shearing augmentation (tilt)                                        | `0`                    |

---

## 🚀 3. Optimization Parameters 🧠

| Parameter         | Description                                                           | Typical Default Value |
|-------------------|-----------------------------------------------------------------------|-----------------------|
| `optimizer`       | Optimizer type (`'SGD'`, `'Adam'`, or `'auto'`)                      | `'auto'` (usually Adam)|
| `lr0`             | Initial learning rate                                                | `0.01`                 |
| `lrf`             | Final learning rate multiplier (for cosine scheduler)                | `0.01`                 |
| `momentum`        | Momentum for SGD optimizer (ignored by Adam)                        | `0.937`                |
| `weight_decay`    | Weight decay (L2 regularization)                                    | `0.0005`               |
| `warmup_epochs`   | Number of warmup epochs to ramp up learning rate                    | `3`                    |
| `warmup_momentum` | Momentum during warmup                                              | `0.8`                  |
| `warmup_bias_lr`  | Learning rate for biases during warmup                             | `0`                    |

---

## 🚀 4. Loss and Detection Parameters 🧠

| Parameter         | Description                                                       | Typical Default Value |
|-------------------|-------------------------------------------------------------------|-----------------------|
| `iou`             | IoU threshold for positive/negative anchor assignment            | `0.7`                 |
| `box`             | Box loss gain (weight of bounding box regression loss)          | `7.5`                 |
| `cls`             | Classification loss gain                                         | `0.5`                 |
| `dfl`             | Distribution Focal Loss gain (for bounding box distance)        | `1.5`                 |
| `label_smoothing` | Amount of label smoothing for classification targets            | `0`                   |
| `single_cls`      | Treat dataset as single class (True/False)                       | `False`               |

---

## 🚀 5. Data and Caching 🧠

| Parameter         | Description                                                       | Typical Default Value |
|-------------------|-------------------------------------------------------------------|-----------------------|
| `cache`           | Cache images for faster training (`ram`, `disk`, or `False`)     | `'disk'` or `False`    |
| `rect`            | Use rectangular training (images resized to rectangular shape)   | `False`               |
| `workers`         | Number of data loading workers (for multiprocessing)             | `8`                   |

---

## 🚀 6. Output & Logging Parameters 🧠

| Parameter         | Description                                                       | Typical Default Value |
|-------------------|-------------------------------------------------------------------|-----------------------|
| `save`            | Save model checkpoints                                           | `True`                |
| `save_period`     | Save checkpoint every N epochs                                  | `-1` (save only last)  |
| `save_txt`       | Save detection labels as text files                              | `False`               |
| `save_conf`      | Save confidence scores with detections                          | `False`               |
| `show`            | Display images during training                                   | `False`               |
| `verbose`         | Verbose logging during training                                 | `True`                |
| `plots`           | Create training plots                                           | `True`                |

---

## 🚀 7. Model & Task Specific Parameters (YOLO11 Extended) 🧠

| Parameter         | Description                                                       | Typical Default Value |
|-------------------|-------------------------------------------------------------------|-----------------------|
| `task`            | Task type: `detect`, `segment`, `pose`, `cls`, `obb`             | `detect`              |
| `pose`            | Number of keypoints (for pose estimation tasks)                  | `17` (COCO default)   |
| `retina_masks`    | Use retina masks in segmentation tasks                            | `False`               |
| `overlap_mask`   | Use overlapping masks (for segmentation)                         | `True`                |
| `max_det`         | Maximum detections per image                                     | `300`                 |

---

# 🚀 Summary 🧠

- Use **`epochs`**, **`batch`**, and **`imgsz`** to control training duration, batch size, and input image resolution.
- Adjust augmentation parameters like **`mosaic`**, **`mixup`**, and color augmentations to increase data variety.
- Set optimizer parameters for **learning rate** and **weight decay** for stable and effective training.
- Fine-tune loss weights (**box**, **cls**, **dfl**) based on your dataset and detection needs.
- For **YOLO11**, choose the `task` parameter depending on your use case (e.g., detection, segmentation, pose).
- Use data caching and multiprocessing to speed up training.

---

# 🚀 Example Training Command (CLI) 🧠

```bash
yolo train model=yolo11l.pt data=custom_data.yaml epochs=300 batch=64 imgsz=640 \
    optimizer=adam lr0=0.01 weight_decay=0.0005 mosaic=1 mixup=0.5 fliplr=0.5 \
    device=0 project=YOLO_Training name=gold_coin_bar_exp
