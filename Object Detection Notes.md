# 🧠 YOLO (You Only Look Once) - Object Detection Notes

## 📌 Overview

YOLO is a **real-time object detection algorithm** that detects objects and their bounding boxes in a **single forward pass** of a CNN — making it **extremely fast and efficient**.

- **YOLO = You Only Look Once**
- Introduced in 2015 by Joseph Redmon
- Suitable for both **images and videos**
- Replaces slower sliding window or R-CNN methods

---

## 📸 Traditional Classification vs Detection

| Task | Output |
|------|--------|
| Image Classification | Label (e.g., `dog`, `person`) |
| Object Localization | Label + Bounding Box |
| Object Detection     | Multiple Labels + Bounding Boxes |

---

## 🔧 What YOLO Predicts

For each **grid cell** in the input image, YOLO predicts:

```
[pc, bx, by, bw, bh, c1, c2, ..., cn]
```

| Element | Description |
|---------|-------------|
| `pc`   | Objectness score (1 if object exists, 0 if not) |
| `bx, by` | Center of bounding box (relative to grid cell) |
| `bw, bh` | Width and height of bounding box (relative to image) |
| `c1 ... cn` | Class probabilities (n = number of classes) |

- 📦 Minimum vector size: **6** (if 1 class)
- 📦 Common vector size: **5 + number_of_classes**

---

## 🧮 YOLO Output Dimensions

If the image is divided into `S × S` grid cells:

```
Output Tensor = S × S × (B × (5 + C))
```

Where:

- `S` = grid size (e.g., 7, 13, 19, etc.)
- `B` = number of bounding boxes per grid cell (aka anchor boxes)
- `C` = number of classes
- `5` = `[pc, bx, by, bw, bh]`

---

## 🧱 Grid Cell Logic

- Each image is divided into an `S × S` grid.
- Each cell is responsible for predicting objects whose **center falls inside** the cell.
- For each bounding box, the cell predicts:
  - Objectness score (`pc`)
  - Bounding box location (`bx, by, bw, bh`)
  - Class probabilities (`c1, c2, ..., cn`)

---

## 📊 Training Data Format

- Each training image is paired with labels in the form of multiple 7-element vectors (or more if multiple classes).
- If using 2 anchor boxes, each cell outputs **2 × (5 + C)** values.

---

## 🧠 YOLO Architecture

1. A CNN (e.g., Darknet) extracts features from the image.
2. Output is passed through fully connected layers to predict bounding boxes and class probabilities for each grid cell.
3. One single forward pass is enough to make all predictions — hence, **"You Only Look Once."**

---

## 🧹 Post-Processing – Non-Max Suppression (NMS)

YOLO might output **multiple boxes** for the same object. NMS is used to remove these duplicates.

1. **Keep the box with the highest confidence.**
2. **Suppress** all other boxes that have high **IoU (Intersection over Union)** with it (typically IOU > 0.5).
3. Repeat for all predicted classes.

---

## 📐 IOU (Intersection Over Union)

IOU is used to measure overlap between two bounding boxes:

```
IOU = Area of Overlap / Area of Union
```

- `IOU = 1` → perfect match
- `IOU = 0` → no overlap
- Used in NMS and for evaluation (mAP metric)

---

## 🎯 Challenges in YOLO

- **Multiple objects in one grid cell**: Solved using **anchor boxes**
- **Small objects close together**: Later YOLO versions use **larger grid sizes** or **feature pyramid networks**
- **Class imbalance**: Addressed using **focal loss**, **label smoothing**, etc.

---

## 🚀 Advantages of YOLO

✅ Extremely fast (real-time)

✅ Single-pass architecture

✅ End-to-end trainable

✅ Good for real-world use cases (CCTV, drones, autonomous driving)

---

## ⛔ Limitations of YOLO (v1–v3)

- May struggle with **small objects**
- Fixed number of predictions per grid cell
- Limited localization accuracy (addressed in YOLOv4+)

---

## 📚 Example

**For a 2-class (dog/person) problem with 2 anchor boxes and 4×4 grid:**

- Vector per anchor = `5 + 2 = 7`
- Output tensor shape = `4 × 4 × 2 × 7 = 224 values`

---

## 🏁 Summary

| Feature | YOLO |
|--------|------|
| Speed | Very fast (real-time) |
| Accuracy | High (but not best on tiny objects) |
| Prediction | In one forward pass |
| Output | Bounding boxes + Class probabilities |
| Grid-based? | Yes |
| Anchor boxes | Yes (used in later versions) |
| Best for | Real-time applications |

---

## 🔗 YOLO Versions (Short Notes)

| Version | Highlights |
|---------|------------|
| YOLOv1 | First version, basic grid + single box |
| YOLOv2 | Introduced anchor boxes, batch norm |
| YOLOv3 | Multi-scale detection, Darknet-53 |
| YOLOv4 | SOTA improvements, CSPDarknet |
| YOLOv5 | PyTorch-based, easy to use, community version |
| YOLOv6–v8 | Further speed/accuracy boosts, new backbones |
