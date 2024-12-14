# Real-Time Emotion Recognizer


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

