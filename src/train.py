from ultralytics import YOLO
import torch


def main():
    # Cek device Apple Silicon
    if torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    print(f"Using device: {device}")

    # Model ringan, cocok untuk Mac dan project UTS
    model = YOLO("yolov8n.pt")

    model.train(
        data="data/helm_dataset/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device=device,
        project="runs",
        name="helmet_yolov8n",
        patience=10
    )


if __name__ == "__main__":
    main()