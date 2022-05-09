#define DAC2 26 // Identify the digital to analog converter pin

int delay1 = 10; // The delay between successive writes

void setup() {

}

void loop() {

// Fade up
// i = 255 = approx 3.3 volts, i = 0 = approx 0.0 volts

dacWrite(DAC2,100);

delay(delay1);

}
