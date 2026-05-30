# 🎯 Real-time Object Detection — YOLOv8

A production-ready real-time object detection system built with YOLOv8, OpenCV, DeepSORT tracking, and a Streamlit dashboard.

---

## 📁 Project Structure

```
Object detection/
├── function.py         # Main entry point (webcam/video)
├── detector.py         # YOLOv8 detection wrapper
├── visualizer.py       # Bounding box drawing + FPS counter
├── tracker.py          # DeepSORT object tracking
├── dashboard.py        # Streamlit web UI
└── requirements.txt    # Dependencies
```

---

## ⚙️ Requirements

- Python **3.11**
- Windows 10/11 (64-bit)

---

## 🚀 Setup & Installation

### Step 1 — Python 3.11 install karo
Download: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe

> Install ke time **"Add python.exe to PATH"** zaroor check karo.

---

### Step 2 — Project folder mein jao
```bash
cd "E:\projects\Obect detection"
```

---

### Step 3 — Virtual environment banao
```bash
py -3.11 -m venv yolo_env
```

---

### Step 4 — Activate karo
```bash
yolo_env\Scripts\activate
```

---

### Step 5 — Packages install karo
```bash
pip install ultralytics opencv-python streamlit deep-sort-realtime numpy
```

---

## ▶️ Run karne ka tarika

### Webcam se detect karo
```bash
python function.py
```

### Video file se detect karo
```bash
python function.py --source meri_video.mp4
```

### Bada model use karo (zyada accurate)
```bash
python function.py --model yolov8m.pt --conf 0.4
```

### Web Dashboard chalao
```bash
streamlit run dashboard.py
```
Browser mein kholo: http://localhost:8501

---

## 🧠 Features

| Feature | Detail |
|---|---|
| Model | YOLOv8n / YOLOv8s / YOLOv8m |
| Classes | 80 (COCO dataset) |
| Tracking | DeepSORT (unique ID per object) |
| FPS Counter | Live overlay on video |
| Dashboard | Streamlit — image/video upload + stats |
| Input | Webcam, video file, RTSP stream |

---

## 📦 Tech Stack

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [PyTorch](https://pytorch.org/)
- [DeepSORT](https://github.com/levan92/deep_sort_realtime)
- [Streamlit](https://streamlit.io/)
- [NumPy](https://numpy.org/)

---

## ❌ Common Errors

### DLL Error on Windows
```
OSError: [WinError 1114] A dynamic link library (DLL) initialization failed
```
**Fix:** Python 3.14 supported nahi hai. Python **3.11** use karo aur nayi virtual env banao.

### `source` command not found
```
/bin/sh: source: not found
```
**Fix:** PowerShell mein `source` nahi chalta. Yeh use karo:
```bash
yolo_env\Scripts\activate
```

### `rmdir /s /q` error in PowerShell
**Fix:**
```bash
Remove-Item -Recurse -Force yolo_env
```

---

## 👤 Author

Jawad — Object Detection Project 2026
