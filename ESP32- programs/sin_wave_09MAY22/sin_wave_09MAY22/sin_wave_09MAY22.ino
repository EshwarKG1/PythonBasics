#define DAC2 26 // Identify the digital to analog converter pin
#define DAC1 25 // Identify the digital to analog converter pin

int delay1 = 10; // The delay between successive writes

void setup() {
  dacWrite(DAC1,127);
  dacWrite(DAC2,127);
}

void loop() {

// Fade up

for (int deg = 0; deg < 360; deg++) {
    dacWrite(DAC1, int(128 + 80 * (sin(deg*PI/180)))); // Sine wave
    dacWrite(DAC2, int(128 + 80 * (sin(deg*PI/180)))); // Sine wave
    delay(delay1);
}
}
