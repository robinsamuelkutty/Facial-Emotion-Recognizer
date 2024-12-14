﻿# Real-Time Emotion Recognizer
### **File Description: `emotions.py`**

The `emotions.py` script implements a **real-time emotion recognizer** using computer vision and deep learning techniques. It leverages the webcam to capture live video frames, analyzes them for facial emotions, and displays the detected emotion on the video feed.

---

### **Key Features:**

1. **Real-Time Emotion Recognition**:
   - Utilizes the DeepFace library to analyze emotions in real-time.
   - Detects dominant emotions such as happiness, sadness, anger, fear, and more.

2. **Interactive Visualization**:
   - Displays the detected emotion and the current time on the video feed using OpenCV.
   - Uses Matplotlib to show the processed frames in an interactive window.

3. **Webcam Integration**:
   - Accesses the webcam for live video feed.
   - Provides a mechanism to handle multiple camera indices if the default one fails.

4. **Error Handling**:
   - Gracefully handles scenarios like missing camera connections or errors during emotion analysis.

5. **Optional Frame Saving**:
   - Saves the processed video frames as images (`output_frame.jpg`) for further use or debugging.

