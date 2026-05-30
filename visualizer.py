import cv2
import time

COLORS = [
    (86, 66, 183), (15, 110, 86), (216, 90, 48),
    (24, 95, 165), (212, 83, 126), (99, 153, 34)
]

class Visualizer:
    def __init__(self):
        self.prev_time = time.time()

    def draw(self, frame, detections, track_ids=None):
        for i, det in enumerate(detections):
            x1, y1, x2, y2 = det["bbox"]
            color = COLORS[det["class_id"] % len(COLORS)]
            label = det["label"]
            conf = det["confidence"]

            tid = track_ids[i] if track_ids else None
            text = f"{label} {conf:.2f}" + (f" #{tid}" if tid else "")

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
            cv2.rectangle(frame, (x1, y1 - th - 8), (x1 + tw + 4, y1), color, -1)
            cv2.putText(frame, text, (x1 + 2, y1 - 4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        # FPS
        curr = time.time()
        fps = 1 / (curr - self.prev_time + 1e-6)
        self.prev_time = curr
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        return frame