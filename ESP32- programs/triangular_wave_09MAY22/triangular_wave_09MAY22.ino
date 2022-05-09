#define DAC2 26 // Identify the digital to analog converter pin

int delay1 = 10; // The delay between successive writes

void setup() {

}

void loop() {

// Fade up

for (int i = 0; i < 256; i++) { // i = 255 = approx 3.3 volts, i = 0 = approx 0.0 volts

dacWrite(DAC2, i);

delay(delay1);

}

// Fade down

for (int i = 255; i > -1; i--) {

dacWrite(DAC2, i);

delay(delay1);

}

}
