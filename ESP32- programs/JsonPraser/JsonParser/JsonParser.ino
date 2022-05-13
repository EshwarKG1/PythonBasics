#include <ArduinoJson.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while(!Serial) continue;
  const int capacity = JSON_OBJECT_SIZE(96);
  StaticJsonDocument<capacity> doc_Cnames;
  StaticJsonDocument<capacity> doc_Tvalues;
  
  /*doc["Sample A"].set("CO2", "Methane", "Hydrogen", "Oxygen");
  doc["Sample B"].set("CO", "Toluene", "Nitrogen", "Oxygen");
  doc["Sample C"].set("Hydrogen", "Benzene", "Oxygen");*/

  doc_Cnames["Sample A"] = "['CO2', 'Methane', 'Hydrogen', 'Oxygen']";
  doc_Cnames["Sample B"] = "['CO', 'Toluene', 'Nitrogen', 'Oxygen']";
  doc_Cnames["Sample C"] = "['Hydrogen', 'benzene', 'Oxygen']";
  doc_Cnames["Sample D"] = "['Vinyl Chloride','Toluene']";
  doc_Cnames["Sample E"] = "['chlorobenzene','methylchloride']";
  doc_Cnames["Sample F"] = "['benzene','perchloroethylene']";
  
  Serial.println();
  serializeJsonPretty(doc_Cnames, Serial); 

  doc_Tvalues["Vinyl Chloride"] = "2.05";
  doc_Tvalues["methylchloride"] = "2.19";
  doc_Tvalues["perchloroethylene"] = "4.5";
  doc_Tvalues["benzene"] = "6.0";
  doc_Tvalues["Toluene"] = "8.0";
  doc_Tvalues["chlorobenzene"] = "10.2";
  doc_Tvalues["CO2"] = "12.0";
  doc_Tvalues["CO"] = "13.05";
  doc_Tvalues["Hydrogen"] = "15.25";
  doc_Tvalues["Oxygen"] = "18.6";
  doc_Tvalues["Methane"] = "20.5";
  doc_Tvalues["Nitrogen"] = "22.01";
  
  Serial.println();
  serializeJsonPretty(doc_Tvalues, Serial);

}

void loop() {
  // put your main code here, to run repeatedly:

}
