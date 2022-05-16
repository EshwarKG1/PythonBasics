#include <WiFi.h>
#include <WebServer.h>

#include "root_page.h"

// SSID & Password
const char* ssid = "Acufore-Electronics";  // Enter your SSID here
const char* password = "Acufore@AF";  //Enter your Password here

WebServer server(80);  // Object of WebServer(HTTP port, 80 is defult)

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

typedef struct MixtureData
{
  char name[20];
  float retensionTime;
  float startTime;
  float stopTime;
};

CompoundRetentionTime ListofCompoundRetTime[10];
Mixture ListofMixture[10];
MixtureData ListofMixtureData[10];

void readRetentionTimeFromFile(){
  strcpy(ListofCompoundRetTime[0].name,"benzene");
  ListofCompoundRetTime[0].retentionTime = 5.5;
  strcpy(ListofCompoundRetTime[1].name,"toluene");
  ListofCompoundRetTime[1].retentionTime = 10.5;
  strcpy(ListofCompoundRetTime[2].name,"hydrogen");
  ListofCompoundRetTime[2].retentionTime = 15.5;
  strcpy(ListofCompoundRetTime[3].name,"nitrogen");
  ListofCompoundRetTime[3].retentionTime = 20.5;
  strcpy(ListofCompoundRetTime[4].name,"oxygen");
  ListofCompoundRetTime[4].retentionTime = 25.5;
}

void readMixtureNames()
{
  strcpy(ListofMixture[0].name,"Sample1");
  strcpy(ListofMixture[0].compounds[0],"oxygen");
  strcpy(ListofMixture[0].compounds[1],"hydrogen");
  strcpy(ListofMixture[1].name,"Sample2");
  strcpy(ListofMixture[1].compounds[0],"nitrogen");
  strcpy(ListofMixture[1].compounds[1],"benzene");
  strcpy(ListofMixture[2].name,"Sample3");
  strcpy(ListofMixture[2].compounds[0],"toluene");
  strcpy(ListofMixture[2].compounds[1],"hydrogen");
  strcpy(ListofMixture[3].name,"Sample4");
  strcpy(ListofMixture[3].compounds[0],"oxygen");
  strcpy(ListofMixture[3].compounds[1],"nitrogen");
}

void readMixtureData(){
  strcpy(ListofMixtureData[0].name,"benzene");
  ListofMixtureData[0].retentionTime = 5.5;
  ListofMixtureData[0].startTime = 3.5;
  ListofMixtureData[0].stopTime = 7.5;
  strcpy(ListofMixtureData[1].name,"toluene");
  ListofMixtureData[1].retentionTime = 10.5;
  ListofMixtureData[1].startTime = 8.5;
  ListofMixtureData[1].stopTime = 12.5;
  strcpy(ListofMixtureData[2].name,"hydrogen");
  ListofMixtureData[2].retentionTime = 15.5;
  ListofMixtureData[2].startTime = 13.5;
  ListofMixtureData[2].stopTime = 17.5;
  strcpy(ListofMixtureData[3].name,"nitrogen");
  ListofMixtureData[3].retentionTime = 20.5;
  ListofMixtureData[3].startTime = 18.5;
  ListofMixtureData[3].stopTime = 22.5;
  strcpy(ListofMixtureData[4].name,"oxygen");
  ListofMixtureData[4].retentionTime = 25.5;
  ListofMixtureData[4].startTime = 23.5;
  ListofMixtureData[4].stopTime = 27.5;
}

int count = 0;

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
  readMixtureNames();
  readRetentionTimeFromFile();
  readMixtureData();
  server.begin();
  Serial.println("HTTP server started");
  delay(100); 
}

void loop() {
  server.handleClient();
  count = count + 1;
}

bool flag_plot = true;

void handle_mixture1(){
  server.send(200, "text/html", HTML);
  char* compound_name1;
  char* compound_name2;
  float rt_time1;
  float rt_time2;
  compound_name1 = ListofMixture[0].compounds[0];
  compound_name2 = ListofMixture[0].compounds[1];
  //Serial.println(compound_name1);
  //Serial.println(compound_name2);
  for(int i=0;i<5;i++){
    //Serial.println(ListofCompoundRetTime[i].name);
    if (strcmp(compound_name1,ListofCompoundRetTime[i].name) == 0){
      //Serial.println(compound_name1);
      //Serial.println(ListofCompoundRetTime[i].retentionTime);
      ListofMixtureData[i].retensionTime
      rt_time1 = ListofCompoundRetTime[i].retentionTime;
    }

    if(strcmp(compound_name2,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name2);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
      rt_time2 = ListofCompoundRetTime[i].retentionTime;
    }
  }
  if (flag_plot){
    dacCurve(0,255,0,10,rt_time1);
    delay(1000);
    dacCurve(0,125,0,10,rt_time2);
    flag_plot = false;
  }
}

void handle_mixture2(){
  server.send(200, "text/html", HTML);
  char* compound_name1;
  char* compound_name2;
  compound_name1 = ListofMixture[1].compounds[0];
  compound_name2 = ListofMixture[1].compounds[1];
  //Serial.println(compound_name1);
  //Serial.println(compound_name2);
  for(int i=0;i<5;i++){
    //Serial.println(ListofCompoundRetTime[i].name);
    if (strcmp(compound_name1,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name1);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }

    if(strcmp(compound_name2,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name2);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }
  }
  if(flag_plot){
    //dacCurve(0,255,0,10);
    delay(1000);
    //dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,180,0,10);
}

void handle_mixture3(){
  server.send(200, "text/html", HTML);
  char* compound_name1;
  char* compound_name2;
  compound_name1 = ListofMixture[2].compounds[0];
  compound_name2 = ListofMixture[2].compounds[1];
  //Serial.println(compound_name1);
  //Serial.println(compound_name2);
  for(int i=0;i<5;i++){
    //Serial.println(ListofCompoundRetTime[i].name);
    if (strcmp(compound_name1,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name1);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }

    if(strcmp(compound_name2,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name2);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }
  }
  if (flag_plot) {
    //dacCurve(0,255,0,10);
    delay(1000);
    //dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,125,0,10);
}

void handle_mixture4(){
  server.send(200, "text/html", HTML);
  char* compound_name1;
  char* compound_name2;
  compound_name1 = ListofMixture[3].compounds[0];
  compound_name2 = ListofMixture[3].compounds[1];
  //Serial.println(compound_name1);
  //Serial.println(compound_name2);
  for(int i=0;i<5;i++){
    //Serial.println(ListofCompoundRetTime[i].name);
    if (strcmp(compound_name1,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name1);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }

    if(strcmp(compound_name2,ListofCompoundRetTime[i].name) == 0){
      Serial.println(compound_name2);
      Serial.println(ListofCompoundRetTime[i].retentionTime);
    }
  }
  if (flag_plot) {
    //dacCurve(0,255,0,10);
    delay(1000);
    //dacCurve(0,125,0,10);
    flag_plot = false;
  }
  //dacCurve(0,80,0,10);
}

void dacCurve(int start_point,int peak_point,int end_point,int delay_time, float retension_time){
  //float start_time;
  //start_time = retension_time - [(peak_point-1)*10];
  //Serial.println(start_time);
  for(int i = start_point; i < peak_point; i = i+4){
    //Serial.println(i);
    dacWrite(DAC1,i);
    dacWrite(DAC2,i);
    delay(delay_time);
  }
  
  for(int i = peak_point; i >= end_point; i = i-4){
    dacWrite(DAC1,i);
    dacWrite(DAC2,i);
    delay(delay_time);
  }

}

void dacPeak(int start_time, float retension_time){

}


// Handle root url (/)
void handle_root() {
  server.send(200, "text/html", HTML);
}
