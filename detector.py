from ultralytics import YOLO
import numpy as np

class ObjectDetector:
    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.conf = conf_threshold
        self.class_names = self.model.names

    def detect(self, frame):
        results = self.model(frame, conf=self.conf, verbose=False)[0]
        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = self.class_names[cls_id]
            detections.append({
                "bbox": (x1, y1, x2, y2),
                "label": label,
                "confidence": conf,
                "class_id": cls_id
            })
        return detections