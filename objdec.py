import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open Webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Cannot open webcam.")
    exit()

while True:

    success, frame = camera.read()

    if not success:
        break

    # Detect and Track only Person (0) and Cell Phone (67)
    results = model.track(
        frame,
        persist=True,
        classes=[0, 67]     # 0 = Person, 67 = Cell Phone
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Close if X button is clicked
    if cv2.getWindowProperty("Object Detection and Tracking",
                             cv2.WND_PROP_VISIBLE) < 1:
        break

camera.release()
cv2.destroyAllWindows()