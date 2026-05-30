import streamlit as st
import cv2
import numpy as np
from collections import Counter
from detector import ObjectDetector

st.title("🎯 Real-time Object Detection Dashboard")

model_choice = st.sidebar.selectbox("Model", ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"])
conf = st.sidebar.slider("Confidence", 0.1, 1.0, 0.5)
uploaded = st.file_uploader("Image ya video upload karo", type=["jpg", "png", "mp4"])

if uploaded:
    detector = ObjectDetector(model_choice, conf)
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if frame is not None:
        detections = detector.detect(frame)

        # Draw boxes
        for d in detections:
            x1,y1,x2,y2 = d["bbox"]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (86,66,183), 2)
            cv2.putText(frame, f"{d['label']} {d['confidence']:.2f}",
                       (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_column_width=True)

        # Stats
        counts = Counter(d["label"] for d in detections)
        st.subheader(f"Detected: {len(detections)} objects")
        st.bar_chart(counts)