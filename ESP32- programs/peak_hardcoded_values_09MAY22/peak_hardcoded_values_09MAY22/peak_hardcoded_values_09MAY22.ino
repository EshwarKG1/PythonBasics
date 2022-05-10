#define DAC2 26 // Identify the digital to analog converter pin
#define DAC1 25 // Identify the digital to analog converter pin
int arr[57] = {0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,19,18,17,16,
             15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0};

int delay1 = 10; // The delay between successive writes

void setup() {

}

void loop() {

// Fade up
// i = 255 = approx 3.3 volts, i = 0 = approx 0.0 volts
for(int i=0;i<57;i++){
  dacWrite(DAC1, arr[i]);
  dacWrite(DAC2, arr[i]);
  delay(delay1);
}
}
