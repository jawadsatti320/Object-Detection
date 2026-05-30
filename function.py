import cv2
import argparse
from detector import ObjectDetector
from visualizer import Visualizer
from tracker import Tracker

def run(source=0, model="yolov8n.pt", conf=0.5, use_tracker=True):
    detector = ObjectDetector(model, conf)
    visualizer = Visualizer()
    tracker = Tracker() if use_tracker else None

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print("Source nahi khula!")
        return

    print("Chal raha hai... 'q' press karo band karne ke liye")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        track_ids = tracker.update(frame, detections) if tracker else None
        frame = visualizer.draw(frame, detections, track_ids)

        cv2.imshow("YOLOv8 Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=0, help="0=webcam, ya video path")
    parser.add_argument("--model", default="yolov8n.pt")
    parser.add_argument("--conf", type=float, default=0.5)
    parser.add_argument("--no-track", action="store_true")
    args = parser.parse_args()

    run(args.source, args.model, args.conf, not args.no_track)