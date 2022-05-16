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
  WriteMixtureNames();
  WriteRetentionTimeFromFile();
  server.begin();
  Serial.println("HTTP server started");
  delay(100); 
}

typedef struct CompoundRetentionTime
{ 
  char name[20];
  float retentionTime;  
};

typedef struct Mixture
{
  char name[10];
  int totalNo;
  char compounds[5][20]; 
};

CompoundRetentionTime ListofCompoundRetTime[10];
Mixture ListofMixture[10];

void WriteRetentionTimeFromFile(){
  strcpy(ListofCompoundRetTime[0].name,"benzene");
  ListofCompoundRetTime[0].retentionTime = 5.5;
  strcpy(ListofCompoundRetTime[1].name,"toluene");
  ListofCompoundRetTime[1].retentionTime = 8.6;
  strcpy(ListofCompoundRetTime[2].name,"hydrogen");
  ListofCompoundRetTime[2].retentionTime = 10.5;
  strcpy(ListofCompoundRetTime[3].name,"nitrogen");
  ListofCompoundRetTime[3].retentionTime = 12.6;
  strcpy(ListofCompoundRetTime[4].name,"oxygen");
  ListofCompoundRetTime[4].retentionTime = 16.3;
}

void WriteMixtureNames()
{
  strcpy(ListofMixture[0].name,"Sample1");
  strcpy(ListofMixture[0].compounds[0],"Oxygen");
  strcpy(ListofMixture[0].compounds[1],"hydrogen");
  strcpy(ListofMixture[1].name,"Sample2");
  strcpy(ListofMixture[1].compounds[0],"Nitrogen");
  strcpy(ListofMixture[1].compounds[1],"benzene");
  strcpy(ListofMixture[2].name,"Sample3");
  strcpy(ListofMixture[2].compounds[0],"toluene");
  strcpy(ListofMixture[2].compounds[1],"hydrogen");
  strcpy(ListofMixture[3].name,"Sample4");
  strcpy(ListofMixture[3].compounds[0],"Oxygen");
  strcpy(ListofMixture[3].compounds[1],"nitrogen");
}

void loop() {
  server.handleClient();
}

bool flag_plot = true;

void handle_mixture1(){
  server.send(200, "text/html", HTML);
  Serial.println("Name:");
  Serial.println(ListofMixture[0].name);
  Serial.println("Compound 1:");
  Serial.println(ListofMixture[0].compounds[0]);
  Serial.println("Compound 2:");
  Serial.println(ListofMixture[0].compounds[1]);
  if (flag_plot){
    dacCurve(0,255,0,10);
    delay(1000);
    dacCurve(0,125,0,10);
    flag_plot = false;
  }
}

void handle_mixture2(){
  server.send(200, "text/html", HTML);
  Serial.println("Name:");
  Serial.println(ListofMixture[1].name);
  Serial.println("Compound 1:");
  Serial.println(ListofMixture[1].compounds[0]);
  Serial.println("Compound 2:");
  Serial.println(ListofMixture[1].compounds[1]);
  if (flag_plot) {
    dacCurve(0,255,0,10);
    delay(1000);
    dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,180,0,10);
}

void handle_mixture3(){
  server.send(200, "text/html", HTML);
  Serial.println("Name:");
  Serial.println(ListofMixture[2].name);
  Serial.println("Compound 1:");
  Serial.println(ListofMixture[2].compounds[0]);
  Serial.println("Compound 2:");
  Serial.println(ListofMixture[2].compounds[1]);
  if (flag_plot) {
    dacCurve(0,255,0,10);
    delay(1000);
    dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,125,0,10);
}

void handle_mixture4(){
  server.send(200, "text/html", HTML);
  Serial.println("Name:");
  Serial.println(ListofMixture[3].name);
  Serial.println("Compound 1:");
  Serial.println(ListofMixture[3].compounds[0]);
  Serial.println("Compound 2:");
  Serial.println(ListofMixture[3].compounds[1]);
  if (flag_plot) {
    dacCurve(0,255,0,10);
    delay(1000);
    dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,80,0,10);
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
