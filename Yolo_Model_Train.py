from ultralytics import YOLO  # Import the YOLO class from Ultralytics

if __name__ == "__main__":
    # Load a pretrained YOLOv11 large model (you can also use 'yolo11x.pt' for an even larger and more accurate model)
    model = YOLO("yolo11l.pt")

    # Start training the model
    results = model.train(
        # Dataset path (data.yaml should define train/val image paths and class names)
        data="/data.yaml",

        # --- Training Schedule ---
        epochs=300,              # Train for 300 full passes (epochs) through the dataset
        patience=50,             # Stop training if validation performance doesn't improve for 50 epochs
        batch=-1,                # Auto-adjust batch size to fit GPU memory (usually ~60% of VRAM)
        imgsz=1024,              # Resize images to 1024x1024 for high accuracy

        # --- Hardware Settings ---
        device=-1,               # Use GPU automatically if available, else fallback to CPU
        workers=8,               # Use 8 CPU threads to load data in parallel (faster loading)

        # --- Optimization Settings ---
        optimizer="AdamW",       # Use AdamW optimizer (better for small datasets or fine-tuning)
        lr0=0.001,               # Initial learning rate (how fast weights are updated)
        lrf=0.01,                # Final learning rate fraction (learning rate will decay to lr0 * lrf)
        cos_lr=True,             # Use cosine decay learning rate for smoother training
        warmup_epochs=5,         # Start with small learning rate for first 5 epochs
        weight_decay=0.0002,     # Regularization to prevent overfitting
        momentum=0.9,            # Momentum for optimizers like SGD (not used in AdamW, but added just in case)
        dropout=0.1,             # Dropout to randomly ignore neurons and avoid overfitting

        # --- Loss Function Weights ---
        label_smoothing=0.01,    # Helps generalize better with slightly smoothed labels
        box=7.5,                 # Weight for bounding box regression loss (higher = more focus)
        cls=0.5,                 # Weight for classification loss (lower if classes are simple)
        dfl=1.5,                 # Weight for distribution focal loss (used for better box prediction)

        # --- Data Augmentations ---
        degrees=0.0,             # No rotation augmentation
        translate=0.1,           # Shift image left/right or up/down by 10%
        scale=0.6,               # Randomly scale images by up to ±60%
        shear=0.0,               # No slanting diagonal, keeping object shapes straight and undistorted.
        perspective=0.0,         # No 3D perspective warping
        flipud=0.0,              # No vertical flipping
        fliplr=0.5,              # 50% chance to horizontally flip images
        hsv_h=0.015,             # Slight hue adjustment
        hsv_s=0.7,               # Strong saturation augmentation
        hsv_v=0.4,               # Medium brightness variation
        mosaic=1.0,              # Mosaic: combine 4 images into 1 to improve object detection robustness
        mixup=0.2,               # MixUp: blend two images and their labels (20% of the time)
        close_mosaic=30,         # Disable mosaic in the last 30 epochs (to help model fine-tune on real images)
        auto_augment="randaugment",  # Automatically choose the best augmentations
        multi_scale=True,        # Train on different image sizes for robustness

        # --- Performance Improvements ---
        cache="ram",             # Cache images in RAM memory to speed up training
        amp=True,                # Enable Automatic Mixed Precision (faster training + less memory usage)
        seed=42,                 # Set random seed for reproducibility
        deterministic=True,      # Ensure training results are the same each time you run (slower, but reproducible)

        # --- Logging & Saving ---
        project="yolo11l_training",  # Folder where all training results are saved (under runs/detect/)
        name="high_accuracy_full",  # Sub-folder for this specific training run
        exist_ok=True,              # Overwrite folder if it already exists
        save=True,                  # Save model checkpoints
        save_best=True,             # Save only the best model (based on validation mAP)
        val=True,                   # Run validation after every epoch
        verbose=True,               # Show detailed logs during training
        plots=True                  # Save training plots (loss curves, precision-recall, etc.)
    )

    # After training, export the best model in ONNX format for deployment
    model.export(format="onnx", imgsz=1024)
