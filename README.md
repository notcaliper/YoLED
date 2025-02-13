# Hand Gesture LED Control System

A computer vision project that controls LED sequences using hand gestures, combining YOLOv8 object detection with Arduino-controlled LEDs.

## Hardware Requirements

- Arduino Uno
- 10 LEDs
- 10 resistors (220Ω)
- Breadboard
- Jumper wires
- Webcam
- USB cable for Arduino

## Software Requirements

- Python 3.8+
- Arduino IDE
- Required Python packages (install using `pip install -r requirements.txt`):
  - opencv-python
  - ultralytics
  - pyserial
  - numpy

## Circuit Setup

1. Connect 10 LEDs to Arduino:
   - Connect LED anodes (longer legs) through 220Ω resistors to pins 2-11
   - Connect all LED cathodes (shorter legs) to GND
   - Use breadboard for easier connections

## Installation

1. **Arduino Setup:**
   - Install [Arduino IDE](https://www.arduino.cc/en/software)
   - Open `hand_gesture_arduino.ino`
   - Select your Arduino board and port
   - Upload code to Arduino

2. **Python Setup:**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

3. **Port Configuration:**
   - Identify your Arduino's serial port:
     - Windows: Usually 'COM3', 'COM4', etc.
     - Linux: Usually '/dev/ttyUSB0' or '/dev/ttyACM0'
     - Mac: Usually '/dev/tty.usbmodem' or '/dev/tty.usbserial'
   - Update the port in `hand_gesture_led_control.py`:
     ```python
     arduino = serial.Serial('YOUR_PORT', 9600, timeout=1)
     ```

## Usage

1. Connect Arduino and ensure code is uploaded
2. Run the Python script:
   ```bash
   python hand_gesture_led_control.py
   ```
3. Show your hand to the camera:
   - Hand detected: LEDs light up in sequence
   - No hand: LEDs turn off in reverse sequence
4. Press 'Q' to exit the program

## How It Works

1. **Detection:**
   - YOLOv8 processes webcam feed
   - Detects hands/persons in frame
   - Shows detection box and status

2. **LED Control:**
   - Detection triggers LED sequence
   - Arduino controls LED animations
   - Visual feedback shown on screen

## Troubleshooting

1. **Arduino Connection Issues:**
   - Verify correct port selection
   - Check USB connection
   - Restart Arduino IDE

2. **Camera Problems:**
   - Ensure webcam is connected
   - Try different camera index:
     ```python
     camera = cv2.VideoCapture(1)  # Try 0, 1, or 2
     ```

3. **LED Issues:**
   - Check LED connections
   - Verify resistor placement
   - Test LEDs individually

## Project Structure

```
project/
├── hand_gesture_arduino.ino   # Arduino code for LED control
├── hand_gesture_led_control.py # Python script for gesture detection
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

## Safety Notes

- Always use resistors with LEDs to limit current
- Do not exceed Arduino pin current limits (40mA max per pin)
- Keep connections secure and insulated
- Avoid touching circuits while powered
- Disconnect power before making changes

## Features

- Real-time hand gesture detection
- Sequential LED animations
- Visual feedback on camera feed
- Status messages for detection state
- Clean program exit with 'Q' key
- Error handling for hardware issues

## Common LED Patterns

1. **Startup Sequence:**
   - All LEDs light up briefly
   - Sequential shutdown
   - Indicates system is ready

2. **Detection Pattern:**
   - Sequential lighting from pin 2 to 11
   - Creates a "flowing" effect
   - Speed controlled by delay settings

3. **Shutdown Pattern:**
   - Reverse sequence from pin 11 to 2
   - Smooth transition to off state

## Future Improvements

1. **Detection:**
   - Add support for multiple hand gestures
   - Implement gesture-specific LED patterns
   - Improve detection accuracy

2. **Hardware:**
   - Add RGB LEDs for color patterns
   - Include buzzer for audio feedback
   - Support for more LED configurations

3. **Software:**
   - Add GUI for settings adjustment
   - Save user preferences
   - Multiple animation patterns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Acknowledgments

- YOLOv8 by Ultralytics
- OpenCV community
- Arduino community
- All contributors and testers
