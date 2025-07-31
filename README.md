# 🖐️ Hand Gesture Drawing App using OpenCV & MediaPipe

This project is a virtual drawing application that uses hand gestures to draw on the screen using your webcam. It leverages **MediaPipe** for hand landmark detection and **OpenCV** for drawing and video processing.

## 🚀 Features

- Draw on the screen using your **index finger**
- Use a **pinch gesture** (index and middle fingers close together) to draw
- **Clear the screen** with a key press
- Real-time webcam interaction
- Fullscreen drawing canvas

---

## 🧠 How It Works

- The application detects hand landmarks using **MediaPipe Hands**.
- It tracks the **index fingertip (landmark 8)** and **middle fingertip (landmark 12)**.
- When the distance between them is less than a threshold (indicating a pinch gesture), it draws on the screen by connecting the previous point with the current point.
- Drawing happens on a transparent canvas that's blended with the video feed in real-time.

---


## 🧰 Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

### 📦 Installation

```bash
pip install opencv-python mediapipe numpy
