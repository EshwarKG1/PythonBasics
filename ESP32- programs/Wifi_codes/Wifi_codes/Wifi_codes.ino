#include <WiFi.h>
#include <WebServer.h>

#include "root_page.h"

// SSID & Password
const char* ssid = "Acufore-Electronics";  // Enter your SSID here
const char* password = "Acufore@AF";  //Enter your Password here

WebServer server(80);  // Object of WebServer(HTTP port, 80 is defult)

void setup() {
  Serial.begin(9600);
  Serial.println("Try Connecting to ");
  Serial.println(ssid);
  
  // Connect to your wi-fi modem
  WiFi.begin(ssid, password);

  // Check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected successfully");
  Serial.print("Got IP: ");
  Serial.println(WiFi.localIP());  //Show ESP32 IP on serial

  server.on("/", handle_root);
  server.on("/mixture1", handle_mixture1);
  server.on("/mixture2", handle_mixture2);
  server.on("/mixture3", handle_mixture3);
  server.on("/mixture4", handle_mixture4);
  server.on("/mixture5", handle_mixture5);
  server.on("/mixture6", handle_mixture6);
  server.on("/mixture7", handle_mixture7);

  server.begin();
  Serial.println("HTTP server started");
  delay(100); 
}

void loop() {
  server.handleClient();
}

void handle_mixture1(){
  server.send(200, "text/html", HTML);
  dacCurve(0,255,0,10);
}

void handle_mixture2(){
  server.send(200, "text/html", HTML);
  dacCurve(0,180,0,10);
}

void handle_mixture3(){
  server.send(200, "text/html", HTML);
  dacCurve(0,125,0,10);
}

void handle_mixture4(){
  server.send(200, "text/html", HTML);
  dacCurve(0,80,0,10);
}

void handle_mixture5(){
  server.send(200, "text/html", HTML);
  dacCurve(0,125,0,10);
}

void handle_mixture6(){
  server.send(200, "text/html", HTML);
  dacCurve(0,180,0,10);
}

void handle_mixture7(){
  server.send(200, "text/html", HTML);
  dacCurve(0,255,0,10);
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

// Handle root url (/)
void handle_root() {
  server.send(200, "text/html", HTML);
}
