import cv2
import time
from deepface import DeepFace
import matplotlib.pyplot as plt


camera_index = 1


cap = cv2.VideoCapture(camera_index)


if not cap.isOpened():
    print(f"Cannot open camera at index {camera_index}. Trying a different index...")
    cap = cv2.VideoCapture(1)  # Try index 1
    if not cap.isOpened():
        print(f"Cannot open camera at index 1. Trying index 2...")
        cap = cv2.VideoCapture(2)  # Try index 2
        if not cap.isOpened():
            print("Cannot open any camera. Please check your webcam connection.")
            exit()


print(f"Camera opened successfully at index {camera_index}")

plt.ion()  
fig, ax = plt.subplots()

try:
    while True:
       
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break

        # Resize the frame to reduce processing time
        img = cv2.resize(frame, (384, 240))
        try:
            
            emotion = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
            current_time = time.strftime("%H:%M:%S", time.localtime())  # Get current time

            
            dominant_emotion = emotion[0].get('dominant_emotion', 'Unknown')
            print(f"Emotion: {dominant_emotion}, Time: {current_time}")

           
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Time: {current_time}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print(f"DeepFace error: {e}")

        # Convert frame to RGB for Matplotlib
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame using Matplotlib
        ax.clear()
        ax.imshow(rgb_frame)
        ax.axis("off")
        plt.pause(0.001)  # Pause to update the frame display

        )
        cv2.imwrite("output_frame.jpg", frame)
        print("Frame saved to output_frame.jpg")
finally:
    # Release the camera
    cap.release()
    plt.ioff()  # Turn off interactive mode
    print("Camera released.")
