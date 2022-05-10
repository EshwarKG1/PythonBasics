#define DAC2 26 // Identify the digital to analog converter pin
#define DAC1 25 // Identify the digital to analog converter pin

int delay1 = 10; // The delay between successive writes

void setup() {

}

void loop() {
  //dacWrite(DAC1,255);
  //dacWrite(DAC2,255);
  delay(2000);                                                                                                                                                                                                                                                                  
  dacCurve(0,190,0,10);
  delay(2000);
  dacCurve(0,140,0,20);
  delay(2000);
  dacCurve(0,190,120,10);
  dacCurve(120,255,0,10);
}

void dacCurve(int start_point,int peak_point,int end_point,int delay_time){
  
  for(int i = start_point; i < peak_point; i++){
    dacWrite(DAC1,i);
    dacWrite(DAC2,i);
    delay(delay_time);
  }
  
  for(int i = peak_point; i >= end_point; i--){
    dacWrite(DAC1,i);
    dacWrite(DAC2,i);
    delay(delay_time);
  }

}
