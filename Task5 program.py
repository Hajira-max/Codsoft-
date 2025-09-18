# ---------------------------------------
# CPU-ONLY FACE DETECTION (Continuous Loop)
# Mobile-Friendly (Images & Videos)
# No CUDA, No dlib, Fully CPU
# ---------------------------------------

!pip install opencv-python-headless google-colab

import cv2
import numpy as np
from google.colab import files
from IPython.display import display, Image

# Load Haar cascade for CPU-only face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image or video frame
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle
    return frame, len(faces)

# Continuous loop for multiple uploads
print("👋 Welcome to CPU-Only Face Detection!")
while True:
    print("\nChoose an option:")
    print("1️⃣ Process Image")
    print("2️⃣ Process Video")
    print("3️⃣ Exit")
    choice = input("Enter 1, 2 or 3: ").strip()

    if choice == "1":
        print("📤 Upload your image:")
        uploaded = files.upload()
        for img_name in uploaded.keys():
            # Read image
            image = cv2.imdecode(np.frombuffer(uploaded[img_name], np.uint8), cv2.IMREAD_COLOR)
            # Detect faces
            result_image, count = detect_faces(image)
            # Save and display result
            cv2.imwrite("result.jpg", result_image)
            print(f"✅ Detected {count} face(s)!")
            display(Image("result.jpg"))

    elif choice == "2":
        print("📤 Upload your video:")
        uploaded = files.upload()
        for video_name in uploaded.keys():
            cap = cv2.VideoCapture(video_name)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter('result_video.mp4', fourcc, 20.0,
                                  (int(cap.get(3)), int(cap.get(4))))
            print("🎬 Processing video. Please wait...")
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                # Detect faces frame by frame
                result_frame, _ = detect_faces(frame)
                out.write(result_frame)
            cap.release()
            out.release()
            print("✅ Video processed! Download the result:")
            files.download("result_video.mp4")

    elif choice == "3":
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2 or 3.")
