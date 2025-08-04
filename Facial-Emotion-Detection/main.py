import cv2
from deepface import DeepFace
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Initialize webcam
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


print("Press 'q' to quit...")

while True:
    ret, frame = video.read()
    if not ret:
        break

    try:
        # Detect faces using cvlib
        faces, confidences = cv.detect_face(frame)

        for idx, face in enumerate(faces):
            (startX, startY, endX, endY) = face

            # Crop the face from the frame
            face_crop = frame[startY:endY, startX:endX]

            # Analyze the face for emotion and gender
            analysis = DeepFace.analyze(face_crop, actions=['emotion', 'gender'], enforce_detection=False)

            # Draw bounding box
            label = f"{analysis[0]['dominant_gender']}, {analysis[0]['dominant_emotion']}"
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    except Exception as e:
        print("Error:", e)

    # Show the frame
    cv2.imshow("Face Recognition with Emotion and Gender Detection", frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video.release()
cv2.destroyAllWindows()
