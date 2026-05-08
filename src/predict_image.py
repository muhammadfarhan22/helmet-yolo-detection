from ultralytics import YOLO


def main():
    model = YOLO("runs/detect/runs/helmet_yolov8n-4/weights/best.pt")

    results = model.predict(
        source="data/helm_dataset/test/images",
        conf=0.25,
        save=True,
        project="results",
        name="image_predictions"
    )

    print("Prediksi selesai.")
    print(results)


if __name__ == "__main__":
    main()