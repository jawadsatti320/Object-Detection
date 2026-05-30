from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, frame, detections):
        ds_input = []
        for d in detections:
            x1, y1, x2, y2 = d["bbox"]
            w, h = x2 - x1, y2 - y1
            ds_input.append(([x1, y1, w, h], d["confidence"], d["label"]))

        tracks = self.tracker.update_tracks(ds_input, frame=frame)
        ids = []
        for t in tracks:
            ids.append(t.track_id if t.is_confirmed() else None)
        return ids