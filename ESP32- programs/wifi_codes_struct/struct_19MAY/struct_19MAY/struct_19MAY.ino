#include <WiFi.h>
#include <WebServer.h>
#define DAC1 25
#define DAC2 26
#define MAX_NO_SAMPLES 5
#define MAX_COMPOUNDS_IN_A_SAMPLE 2


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
  float retentionTime;
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
  strcpy(ListofMixtureData[1].name,"toluene");
  ListofMixtureData[1].retentionTime = 10.5;
  strcpy(ListofMixtureData[2].name,"hydrogen");
  ListofMixtureData[2].retentionTime = 15.5;
  strcpy(ListofMixtureData[3].name,"nitrogen");
  ListofMixtureData[3].retentionTime = 20.5;
  strcpy(ListofMixtureData[4].name,"oxygen");
  ListofMixtureData[4].retentionTime = 25.5;
}

void setup() {
  dacWrite(DAC1,0);
  dacWrite(DAC2,0);
  Serial.begin(9600);
  Serial.println();
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
}

bool flag_plot = true;

void handle_mixture1(){
  server.send(200,"text/html",HTML);
  char* selected_name[2];
  float rt_time1;
  float rt_time2;
  float rt_time1M;
  float rt_time2M;
  float delayTime;
  selected_name[0] = ListofMixture[0].compounds[0];
  selected_name[1] = ListofMixture[0].compounds[1];
  Serial.println("Selected Name:");
  Serial.println(selected_name[0]);
  Serial.println(selected_name[1]);
  for(int i=0;i<MAX_NO_SAMPLES;i++){
    if(strcmp(ListofMixtureData[i].name,selected_name[0])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time1 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time1);
    }

    if(strcmp(ListofMixtureData[i].name,selected_name[1])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time2 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time2);
    }
  }

  if(rt_time1>rt_time2){
    rt_time2M = rt_time2*1000;
    rt_time2M = rt_time2M - 2000;
    delay(rt_time2M);
    delayTime = rt_time1-rt_time2;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
  
  else{
    rt_time1M = rt_time1*1000;
    rt_time1M = rt_time1M - 2000;
    delay(rt_time1M);
    delayTime = rt_time2-rt_time1;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
}

void handle_mixture2(){
  server.send(200, "text/html", HTML);
  char* selected_name[2];
  float rt_time1;
  float rt_time2;
  float rt_time1M;
  float rt_time2M;
  float delayTime;
  selected_name[0] = ListofMixture[1].compounds[0];
  selected_name[1] = ListofMixture[1].compounds[1];
  Serial.println("Selected Name:");
  Serial.println(selected_name[0]);
  Serial.println(selected_name[1]);
  for(int i=0;i<MAX_NO_SAMPLES;i++){
    if(strcmp(ListofMixtureData[i].name,selected_name[0])==0){
      Serial.println(ListofMixtureData[i].retentionTime);
      rt_time1 = ListofMixtureData[i].retentionTime;
      //Serial.println(rt_time1);
    }

    if(strcmp(ListofMixtureData[i].name,selected_name[1])==0){
      Serial.println(ListofMixtureData[i].retentionTime);
      rt_time2 = ListofMixtureData[i].retentionTime;
      //Serial.println(rt_time2);
    }
  }

  if(rt_time1>rt_time2){
    rt_time2M = rt_time2*1000;
    rt_time2M = rt_time2M - 2000;
    delay(rt_time2M);
    delayTime = rt_time1-rt_time2;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
  
  else{
    rt_time1M = rt_time1*1000;
    rt_time1M = rt_time1M - 2000;
    delay(rt_time1M);
    delayTime = rt_time2-rt_time1;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
}

void handle_mixture3(){
  server.send(200, "text/html", HTML);
  char* selected_name[2];
  float rt_time1;
  float rt_time2;
  float rt_time1M;
  float rt_time2M;
  float delayTime;
  selected_name[0] = ListofMixture[2].compounds[0];
  selected_name[1] = ListofMixture[2].compounds[1];
  Serial.println("Selected Name:");
  Serial.println(selected_name[0]);
  Serial.println(selected_name[1]);
  for(int i=0;i<MAX_NO_SAMPLES;i++){
    if(strcmp(ListofMixtureData[i].name,selected_name[0])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time1 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time1);
    }

    if(strcmp(ListofMixtureData[i].name,selected_name[1])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time2 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time2);
    }
  }

  if(rt_time1>rt_time2){
    rt_time2M = rt_time2*1000;
    rt_time2M = rt_time2M - 2000;
    delay(rt_time2M);
    delayTime = rt_time1-rt_time2;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
  
  else{
    rt_time1M = rt_time1*1000;
    rt_time1M = rt_time1M - 2000;
    delay(rt_time1M);
    delayTime = rt_time2-rt_time1;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
}

void handle_mixture4(){
  server.send(200, "text/html", HTML);
  char* selected_name[2];
  float rt_time1;
  float rt_time2;
  float rt_time1M;
  float rt_time2M;
  float delayTime;
  selected_name[0] = ListofMixture[3].compounds[0];
  selected_name[1] = ListofMixture[3].compounds[1];
  Serial.println("Selected Name:");
  Serial.println(selected_name[0]);
  Serial.println(selected_name[1]);
  for(int i=0;i<MAX_NO_SAMPLES;i++){
    if(strcmp(ListofMixtureData[i].name,selected_name[0])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time1 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time1);
    }

    if(strcmp(ListofMixtureData[i].name,selected_name[1])==0){
      //Serial.println(ListofMixtureData[i].retentionTime);
      rt_time2 = ListofMixtureData[i].retentionTime;
      Serial.println(rt_time2);
    }
  }

  if(rt_time1>rt_time2){
    rt_time2M = rt_time2*1000;
    rt_time2M = rt_time2M - 2000;
    delay(rt_time2M);
    delayTime = rt_time1-rt_time2;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
  
  else{
    rt_time1M = rt_time1*1000;
    rt_time1M = rt_time1M - 2000;
    delay(rt_time1M);
    delayTime = rt_time2-rt_time1;
    Serial.println(delayTime);
    delayTime = delayTime*1000;
    //delay(delayTime);
    dacCurve(0,255,0,10,delayTime);
    dacCurve(0,255,0,10,3000);
  }
}

void dacCurve(int start_point,int peak_point,int end_point,int delay_time, float delayTimeBetweenCurve){
 
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
  
  delay(delayTimeBetweenCurve);
}

// Handle root url (/)
void handle_root() {
  server.send(200, "text/html", HTML);
}
