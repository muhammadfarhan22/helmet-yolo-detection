# Deteksi Penggunaan Helm pada Pengendara Motor Menggunakan YOLOv8

Project ini merupakan implementasi **object detection** untuk mendeteksi penggunaan helm pada pengendara motor menggunakan **YOLOv8**. Project ini dibuat sebagai output UTS mata kuliah **Advanced Computer Vision** dan bertujuan untuk membangun prototipe sistem pendukung keselamatan lalu lintas berbasis computer vision.

## 📌 Deskripsi Project

Keselamatan lalu lintas merupakan salah satu aspek penting, khususnya bagi pengguna sepeda motor. Helm berfungsi sebagai alat pelindung kepala yang dapat mengurangi risiko cedera serius saat terjadi kecelakaan.

Pada project ini, model YOLOv8 dilatih untuk mendeteksi beberapa kategori penggunaan helm pada pengendara motor, yaitu:

| Kelas        | Keterangan                                        |
| ------------ | ------------------------------------------------- |
| `full-faced` | Pengendara menggunakan helm full-face             |
| `half-faced` | Pengendara menggunakan helm half-face             |
| `invalid`    | Objek atau kondisi visual yang tidak valid/ambigu |
| `no helmet`  | Pengendara tidak menggunakan helm                 |

## 🎯 Tujuan Project

Tujuan dari project ini adalah:

1. Mengimplementasikan object detection menggunakan YOLOv8.
2. Melatih model untuk mendeteksi penggunaan helm pada pengendara motor.
3. Mengevaluasi performa model menggunakan precision, recall, mAP50, dan mAP50-95.
4. Menampilkan hasil prediksi dalam bentuk bounding box.
5. Membuat project yang dapat digunakan sebagai portofolio di bidang Computer Vision.

## 🧠 Metode

Model yang digunakan adalah **YOLOv8n** dari Ultralytics. YOLOv8n dipilih karena ringan dan cocok digunakan untuk eksperimen pada perangkat lokal.

Pendekatan yang digunakan adalah **transfer learning**, yaitu menggunakan pretrained model `yolov8n.pt`, kemudian dilatih ulang menggunakan dataset deteksi helm.

## 🗂️ Dataset

Dataset yang digunakan berasal dari **Roboflow Universe**:

**Motorcycle Helmet Detection**  
Link dataset: https://universe.roboflow.com/rishabh-qz7yl/motorcycle-helmet-detection-ch64l/dataset/1

Dataset tersedia dalam format YOLO dan terdiri dari data:

```text
train/
valid/
test/
```
