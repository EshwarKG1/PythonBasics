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

void setup() {
}

void loop() {
  // put your main code here, to run repeatedly:

}
