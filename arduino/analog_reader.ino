void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(A1, INPUT);
//Serial.println("Hello eshwar");
}

void loop() {
  // put your main code here, to run repeatedly:
int a = 0;
a = analogRead(A1);
Serial.println(a);
delay(100);
}
