import cv2
from ultralytics import YOLO
import serial
import time

# Connect to Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to start

# Setup camera and YOLO
model = YOLO('yolov8n.pt')
camera = cv2.VideoCapture(0)

def handle_led_control(hand_detected):
    # Send command to Arduino (1 for ON, 0 for OFF)
    command = b'1' if hand_detected else b'0'
    arduino.write(command)
    
    # Get Arduino's response
    response = arduino.readline().decode().strip()
    
    # Show status on camera feed
    status = f"Hand Detected: {response}" if hand_detected else f"No Hand: {response}"
    color = (0, 255, 0) if hand_detected else (0, 0, 255)  # Green or Red
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    # Add exit instruction
    cv2.putText(frame, "Press 'Q' to quit", (10, frame.shape[0] - 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

try:
    while True:
        # Get camera frame
        success, frame = camera.read()
        if not success:
            break

        # Detect objects in frame
        results = model(frame)
        hand_detected = False
        
        # Check for hand/person in frame
        for result in results:
            for box in result.boxes:
                if model.names[int(box.cls[0])] == 'person':
                    if float(box.conf[0]) > 0.5:  # If confidence > 50%
                        # Draw box around detected hand
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        hand_detected = True

        # Control LEDs based on detection
        handle_led_control(hand_detected)
        
        # Show camera feed
        cv2.imshow('Hand Detection - Press Q to Quit', frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Cleanup
    camera.release()
    cv2.destroyAllWindows()
    arduino.close() 