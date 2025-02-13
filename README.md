# Hand Gesture LED Control System

A computer vision project that uses hand gestures to control LED sequences through YOLOv8 detection and Arduino. When a hand is detected, it triggers a sequential LED animation pattern.

## 📋 Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Development](#development)

## 🔧 Requirements

### Hardware
- Arduino Uno board
- 10 LEDs (any color)
- 10 resistors (220Ω)
- Breadboard
- Jumper wires
- Webcam
- USB cable for Arduino

### Software
- Python 3.8+
- Arduino IDE
- Required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

## 🔌 Setup

### Circuit Connection
1. **LED Setup** (Connect in this order):
   ```
   Arduino Pin -> 220Ω Resistor -> LED -> GND
   ```
   - Pins used: 2 through 11 (10 LEDs total)
   - LED longer leg (anode) → resistor → Arduino pin
   - LED shorter leg (cathode) → GND

2. **Breadboard Layout**:
   ```
   + Rail: Connect to Arduino pins (2-11)
   - Rail: Connect to Arduino GND
   ```

### Software Configuration
1. **Arduino**:
   - Open Arduino IDE
   - Select board: Tools → Board → Arduino Uno
   - Select port: Tools → Port → COMx (Windows) or /dev/ttyUSBx (Linux)
   - Upload `hand_gesture_arduino.ino`

2. **Python**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure port in `hand_gesture_led_control.py`:
     ```python
     arduino = serial.Serial('YOUR_PORT', 9600, timeout=1)
     ```

## 🚀 Usage

1. **Start the System**:
   ```bash
   python hand_gesture_led_control.py
   ```

2. **LED Patterns**:
   - **Startup**: All LEDs blink in sequence
   - **Hand Detected**: Forward sequence (2→11)
   - **No Hand**: Reverse sequence (11→2)

3. **Controls**:
   - Show hand to camera to activate LEDs
   - Press 'Q' to quit program
   - Status shown on video feed

## ❗ Troubleshooting

### Common Issues

1. **Port Error**:
   ```
   Serial port 'COMx' not found
   ```
   - Solution: Check Arduino Manager for correct port
   - Try unplugging and reconnecting Arduino

2. **Camera Error**:
   ```
   Camera index out of range
   ```
   - Solution: Try different indices (0,1,2)
   - Check if webcam is recognized by system

3. **LED Issues**:
   - Check polarity (longer leg to Arduino)
   - Verify resistor connections
   - Test each LED individually

## 💻 Development

### Project Structure
```
hand-gesture-led/
├── hand_gesture_arduino.ino   # Arduino LED control
├── hand_gesture_led_control.py # Main Python script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # Documentation
```

### Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 🔒 Safety Guidelines

- Never exceed 40mA per Arduino pin
- Always use current-limiting resistors
- Disconnect power before circuit changes
- Keep connections insulated
- Handle components with care

## 📝 License

MIT License - See LICENSE file

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- OpenCV community
- Arduino community
- All contributors
