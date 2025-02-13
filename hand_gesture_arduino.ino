#include <Arduino.h>

// Define LED pins (using pins 2-11 for 10 LEDs)
const int NUM_LEDS = 10;
const int LED_PINS[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

void setup() {
  Serial.begin(9600);  // Start serial communication
  
  // Setup all LED pins
  for(int i = 0; i < NUM_LEDS; i++) {
    pinMode(LED_PINS[i], OUTPUT);
  }
  
  // Run startup test
  testLEDs();
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    
    if (command == '1') {
      turnOnLEDsSequentially();
      Serial.println("ON");
    }
    else if (command == '0') {
      turnOffLEDsSequentially();
      Serial.println("OFF");
    }
  }
}

// Test all LEDs on startup
void testLEDs() {
  // Turn on each LED one by one
  for(int i = 0; i < NUM_LEDS; i++) {
    digitalWrite(LED_PINS[i], HIGH);
    delay(50);
  }
  delay(200);
  
  // Turn off each LED one by one
  for(int i = 0; i < NUM_LEDS; i++) {
    digitalWrite(LED_PINS[i], LOW);
    delay(50);
  }
}

// Turn on LEDs in sequence
void turnOnLEDsSequentially() {
  for(int i = 0; i < NUM_LEDS; i++) {
    digitalWrite(LED_PINS[i], HIGH);
    delay(50);
  }
}

// Turn off LEDs in reverse sequence
void turnOffLEDsSequentially() {
  for(int i = NUM_LEDS-1; i >= 0; i--) {
    digitalWrite(LED_PINS[i], LOW);
    delay(50);
  }
} 