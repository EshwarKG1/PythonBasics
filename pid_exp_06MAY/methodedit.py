from tkinter import *

from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import re

def ValidateFloatFormat(String):
  regex = '[+-]?[0-9]+\.[0-9]+'
  if(re.search(regex, String)): 
        return True          
  else: 
        return False
        
def ValidateTimeFormat(String):
  pattern = '[0-9]{1,2}:[0-9]{1,2}(:[0-9]{0,1}){0,1}'
  if re.match(pattern, String):
    return True
  else:
    return False
    
    
class MethodEdit:    
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()  
        self.values = {} # Initalize the dictionary 
        self.decimalFoundFlag  = False 
        return

    def InitializeVariables(self):
        self.popUpWindow       = None
        self.helpPopUp         = None
        self.rampingFlag       = BooleanVar()
        self.SensorSettingFlag = BooleanVar()
        self.OvenDoorManualFlag= BooleanVar()
        self.TempSettingFlag   = BooleanVar()
        self.SyringeInjFlag    = BooleanVar()
        
        self.hold_time_2       = StringVar()
        self.hold_time_3       = StringVar()
        self.Hold_time_1       = StringVar()
        self.Hold_time_2       = StringVar()
        self.Hold_time_3       = StringVar()
        self.Ramp1             = StringVar()
        self.Ramp2             = StringVar()
        self.slope_m           = StringVar()
        self.intercept_m       = StringVar()
 
        self.avgCycle          = StringVar()
        self.repeatCycle       = StringVar()
        self.calibrationCycle  = StringVar()

        self.SetFlow           = StringVar()
        
        self.slope_k           = StringVar()
        self.intercept_d       = StringVar()
        self.R1AONval          = StringVar()
        self.R1AOFFval         = StringVar()
        self.R1BONval          = StringVar()
        self.R1BOFFval         = StringVar()
        self.X3ONval           = StringVar()
        self.X3OFFval          = StringVar()
        self.X4ONval           = StringVar()
        self.X4OFFval          = StringVar()
        self.X5ONval           = StringVar()
        self.X5OFFval          = StringVar()
        self.InjDetTemprature  = StringVar()
        self.calibrateTime     = StringVar()
        self.analysis_time     = StringVar()
        self.inject_time       = StringVar()
        self.equil_time        = StringVar()
        self.OvenTemp          = StringVar()
        self.sample_time       = StringVar()
        return
    
          
    def OKCallBack(self):
        #print("OK callback")
        errorFlag = False 
        
        val=self.hold_time_2.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 2 is not valid")
              errorFlag = True      
              return
        else:
            self.hold_time_2.set("0:0:0")
        
        val = self.hold_time_3.get()        
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 3 is not valid")
              errorFlag = True      
              return              
        else:
           self.hold_time_3.set("0:0:0")
           
        val = self.Hold_time_1.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 1 is not valid")
              errorFlag = True             
              return
        else:
           self.Hold_time_1.set("0:0:0")
        
        
        val = self.Hold_time_2.get() 
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 2 is not valid")
              errorFlag = True             
              return
        else:
           self.Hold_time_2.set("0:0:0")
           
        val= self.Hold_time_3.get() 
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 3 is not valid")
              errorFlag = True             
              return
        else:
           self.Hold_time_3.set("0:0:0")
           
        val=self.Ramp1.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Ramp 1 is not valid")
              errorFlag = True             
              return
        else:
           self.Ramp1.set("0")
           
        val=self.Ramp2.get() 
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Ramp 2is not valid")
              errorFlag = True             
              return
        else:
           self.Ramp2.set("0")
           
        val=self.slope_m.get()
        if (val != ""):
           if(ValidateFloatFormat(val) == False):
              messagebox.showerror("Error", "Value of Slope m is not valid")
              errorFlag = True             
              return
        else:        
           self.slope_m.set("0.0")
        
        val=self.intercept_m.get()
        if (val != ""):
           if(ValidateFloatFormat(val) == False):
              messagebox.showerror("Error", "Value ofIntercept M  is not valid")
              errorFlag = True             
              return
        else:        
           self.intercept_m.set("0.0")
           
        val=self.avgCycle.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Value of Average Cycle is not valid")
              errorFlag = True             
              return
        else:        
           self.avgCycle.set("0")
           
        val=self.repeatCycle.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Repeat Cycle Value is not valid")
              errorFlag = True             
              return
        else:
           self.repeatCycle.set("0")
           
        val=self.calibrationCycle.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Value of Calibration Cycle is not valid")
              errorFlag = True             
              return
        else:        
           self.calibrationCycle.set("0")
           
        val=self.SetFlow.get()
        if (val != ""):
           if(ValidateFloatFormat(val) == False):
              messagebox.showerror("Error", "Value of Set Flow is not valid")
              errorFlag = True             
              return
        else:        
           self.SetFlow.set("0.0")
           
                   
        val=self.slope_k.get()
        if (val != ""):
           if(ValidateFloatFormat(val) == False):
              messagebox.showerror("Error", "Slope k is not valid")
              errorFlag = True             
              return
        else:        
           self.slope_k.set("0.0")
           
        val=self.intercept_d.get()
        if (val != ""):
           if(ValidateFloatFormat(val) == False):
              messagebox.showerror("Error", "Intercept d is not valid")
              errorFlag = True             
              return
        else:        
           self.intercept_d.set("0.0")
           
        val=self.R1AONval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of R1A ON is not valid")
              errorFlag = True             
              return
        else:        
           self.R1AONval.set("0:0:0")
           
        val=self.R1AOFFval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "R1A OFF  is not valid")
              errorFlag = True             
              return
        else:        
           self.R1AOFFval.set("0:0:0")
           
        val=self.R1BONval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of R1B ON is not valid")
              errorFlag = True             
              return
        else:        
           self.R1BONval.set("0:0:0")
           
        val=self.R1BOFFval.get() 
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of R1B OFF is not valid")
              errorFlag = True             
              return
        else:        
           self.R1BOFFval.set("0:0:0")
           
        val=self.X3ONval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X3 ON is not valid")
              errorFlag = True             
              return
        else:        
           self.X3ONval.set("0:0:0")
           
        val=self.X3OFFval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X3 OFF not valid")
              errorFlag = True             
              return
        else:        
           self.X3OFFval.set("0:0:0")
           
        val = self.X4ONval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X4 ON is not valid")
              errorFlag = True             
              return
        else:        
           self.X4ONval.set("0:0:0")
           
        
        val=self.X4OFFval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X4 OFF is not valid")
              errorFlag = True             
              return
        else:        
           self.X4OFFval.set("0:0:0")
           
        val=self.X5ONval.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X5 ON is not valid")
              errorFlag = True             
              return
        else:        
           self.X5ONval.set("0:0:0")
           
        val=self.X5OFFval.get() 
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of X5 OFF is not valid")
              errorFlag = True             
              return
        else:        
          self.X5OFFval.set("0:0:0")
          
        val=self.InjDetTemprature.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Value of Inj Det Temp is not valid")
              errorFlag = True             
              return
        else:        
          self.InjDetTemprature.set("0")
          
        val=self.calibrateTime.get() 
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of Calibrate time is not valid")
              errorFlag = True             
              return
        else:        
          self.calibrateTime.set("0:0:0")
          
        val=self.analysis_time.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of Analysis Time is not valid")
              errorFlag = True             
              return
        else:        
          self.analysis_time.set("0:0:0")
          
        val=self.inject_time.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value Inject Time is not valid")
              errorFlag = True             
              return
        else:        
          self.inject_time.set("0:0:0")
          
        val=self.equil_time.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Value of Equil Time is not valid")
              errorFlag = True             
              return
        else:        
          self.equil_time.set("0:0:0")
          
        val=self.OvenTemp.get()
        if (val != ""):
           if(val.isdigit() == False):
              messagebox.showerror("Error", "Value of Oven Temperature is not valid")
              errorFlag = True             
              return
        else:        
          self.OvenTemp.set("0")
                    
        val=self.sample_time.get()
        if (val != ""):
           if(ValidateTimeFormat(val) == False):
              messagebox.showerror("Error", "Hold Time 1 is not valid")
              errorFlag = True             
              return
        else:        
          self.sample_time.set("0.0")
          
        self.values['RampingFlag']       =self.rampingFlag.get()   
        self.values['TempSettingFlag']   =self.TempSettingFlag.get()
        self.values['OvenDoorManualFlag']=self.OvenDoorManualFlag.get()   
        self.values['SensorSettingFlag'] =self.SensorSettingFlag.get() 
        self.values['SyringeInjFlag']    =self.SyringeInjFlag.get()
         
        self.values['Ramp1']             =self.Ramp1.get()
        self.values['Ramp2']             =self.Ramp2.get()                
        self.values['avgCycle']          =self.avgCycle.get()
        self.values['repeatCycle']       =self.repeatCycle.get()
        self.values['calibrationCycle']  =self.calibrationCycle.get()
         
        self.values['hold_time_2']       =self.hold_time_2.get()
        self.values['hold_time_3']       =self.hold_time_3.get()
        self.values['Hold_time_1']       =self.Hold_time_1.get()
        self.values['Hold_time_2']       =self.Hold_time_2.get()
        self.values['Hold_time_3']       =self.Hold_time_3.get()
        self.values['slop_m']            =self.slope_m.get()
        self.values['intercept_m']       =self.intercept_m.get()

         
        self.values['SetFlow']           =self.SetFlow.get()
        self.values['slope_k']           =self.slope_k.get()
        self.values['intercept_d']       =self.intercept_d.get()
        self.values['R1AONval']          =self.R1AONval.get()  
        self.values['R1AOFFval']         =self.R1AOFFval.get()
        self.values['R1BONval']          =self.R1BONval.get() 
        self.values['R1BOFFval']         =self.R1BOFFval.get()
        self.values['X3ONval']           =self.X3ONval.get()  
        self.values['X3OFFval']          =self.X3OFFval.get()
        self.values['X4ONval']           =self.X4ONval.get()
        self.values['X4OFFval']          =self.X4OFFval.get()
        self.values['X5ONval']           =self.X5ONval.get()
        self.values['X5OFFval']          =self.X5OFFval.get()
        self.values['InjDetTemprature']  =self.InjDetTemprature.get()
        self.values['calibrateTime']     =self.calibrateTime.get()
        self.values['analysis_time']     =self.analysis_time.get()
        self.values['inject_time']       =self.inject_time.get()
        self.values['equil_time']        =self.equil_time.get()   
        self.values['OvenTemp']          =self.OvenTemp.get()
        self.values['sample_time']       =self.sample_time.get()
        
        if (errorFlag == False):
           self.popUpWindow.destroy()
           self.popUpWindow = None
        return
        
    def GetValueFromMethod(self):
        return self.values
        
    def CancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
    def popUpWindowXPressed(self):
        self.CancelCallBack()
        
    def PrintCallBack(self):
        return
        
    def CloseHelp(self):
        self.helpPopUp.destroy()
        self.helpPopUp = None
        
    def HelpCallBack(self):
        if (self.helpPopUp == None):
            self.helpPopUp= Toplevel(self.parentWindow)
        else:
            return
            
        self.helpPopUp.title("Help")
        self.helpPopUp.resizable(False, False)
        TextWindow = Text(self.helpPopUp, height = 5, width = 50)
        l = Label(helpPopUp, text = "Help On Method")
  
        Fact = "This window is used for editing various parameters,refer to PID Analyzer documentation for details"
        TextWindow.insert(END, Fact)
        TextWindow.config(state=DISABLED,wrap=WORD )
        # Create an Exit button.    
        b2 = Button(self.helpPopUp, text = "OK",  command = self.helpPopUp.destroy) 
  
        l.pack()
        TextWindow.pack()
        b2.pack()
        return
        
    def CreateTemperatureProgrammingFrame(self):
        Panel2Frame   = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        TempProgFrame = LabelFrame(Panel2Frame,text='Temperature Progamming')
        
        #TempProgFrame = Frame(Panel2Frame,borderwidth=4,relief=GROOVE)
        #rowOneFrame   = Frame(TempProgFrame,borderwidth=4,relief=FLAT)
        #Label(rowOneFrame, text='Temperature Progamming').grid(row=0,column=0)
        #rowOneFrame.pack(side=TOP,fill=X,expand=1)    
        
        rowTwoFrame = Frame(TempProgFrame,borderwidth=4,relief=FLAT)
        rowTwoFrame.pack(side=TOP,fill=X,expand=1)
        
        Checkbutton(rowTwoFrame, variable=self.rampingFlag,text='Ramping').pack(side=LEFT,ipadx=17)
        
        Label(rowTwoFrame, text='Hold Time 2').pack(side=LEFT)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.hold_time_2,
                     width= 6).pack(side=LEFT)
                        
        Label(rowTwoFrame, text='Hold Time 3').pack(side=LEFT)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.hold_time_3, 
                     width=6).pack(side=LEFT)
        rowTwoFrame.pack(side=TOP,ipadx=5)
        
        rowThreeFrame = Frame(TempProgFrame,borderwidth=4,relief=FLAT)
        
        Label(rowThreeFrame, text='Hold Time 1').pack(side=LEFT)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.Hold_time_1, 
                     width= 6).pack(side=LEFT)
        
        
        Label(rowThreeFrame, text='Hold Time 2').pack(side=LEFT)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.Hold_time_2, 
                     width=6).pack(side=LEFT)
        
        
        Label(rowThreeFrame, text='Hold Time 3').pack(side=LEFT)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.Hold_time_3, 
                     width=6).pack(side=LEFT)
        rowThreeFrame.pack(side=TOP,fill=X,expand=1)
        rowFourFrame = Frame(TempProgFrame,borderwidth=4,relief=FLAT)
        
        Label(rowFourFrame, text='Ramp 1').pack(side=LEFT,ipadx=12)
        
        entry= Entry(rowFourFrame,relief=SUNKEN, textvariable=self.Ramp1, 
                     width= 6).pack(side=LEFT)
        
        
        Label(rowFourFrame, text='Ramp 2').pack(side=LEFT,ipadx=12)
        
        entry= Entry(rowFourFrame,relief=SUNKEN, textvariable=self.Ramp2, 
                     width=6).pack(side=LEFT)
            
        rowFourFrame.pack(side=TOP,fill=X,expand=1)
        TempProgFrame.pack(side=LEFT, ipadx= 60)
        
        # Now Create the next frame in panel2
        # This is the for the small frame for oven settings
        #OvenSettingFrame = Frame(Panel2Frame,borderwidth=4,relief=GROOVE)
        #rowOneFrame = Frame(OvenSettingFrame,borderwidth=4,relief=FLAT)
        #Label(rowOneFrame, text='Oven T =  mV + b').grid(row=0,column=0)
        #rowOneFrame.pack(side=TOP,fill=X,expand=1)  
        
        OvenSettingFrame = LabelFrame(Panel2Frame,text='Oven T =  mV + b')
        rowTwoFrame = Frame(OvenSettingFrame,borderwidth=4,relief=FLAT)
        
        Checkbutton(rowTwoFrame, variable=self.TempSettingFlag,text='Temp Setting').pack(side=TOP)
        rowTwoFrame.pack(side=TOP)
        
        rowThreeFrame = Frame(OvenSettingFrame,borderwidth=4,relief=FLAT)
        Label(rowThreeFrame, text='Slope m').pack(side=LEFT)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.slope_m, 
                     width=6).pack(side=LEFT)  
        rowThreeFrame.pack(side=TOP)
        
        rowFourFrame = Frame(OvenSettingFrame,borderwidth=4,relief=FLAT)
        Label(rowFourFrame, text='Intercept m').pack(side=LEFT)
        
        entry= Entry(rowFourFrame,relief=SUNKEN, textvariable=self.intercept_m, 
                     width=6).pack(side=LEFT)     
        rowFourFrame.pack(side=TOP)
        
          
        OvenSettingFrame.pack(side=LEFT)

        Panel2Frame.pack(side=TOP,anchor=W)
        return
        

        
    def CreateMiscTableFrame(self):

        Panel3Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        #MiscTableFrame = Frame(Panel3Frame,borderwidth=4,relief=GROOVE)
        #rowOneFrame = Frame(MiscTableFrame,borderwidth=4,relief=FLAT)
        #Label(rowOneFrame, text='Misc Table        ').grid(row=0,column=0) 
        #rowOneFrame.pack(side=TOP,fill=X,expand=1)    
        
        MiscTableFrame = LabelFrame(Panel3Frame,text='Misc Table')
        rowTwoFrame = Frame(MiscTableFrame,borderwidth=4,relief=FLAT)
      
        rowTwoFrame.pack(side=TOP,fill=X,expand=1)    
        
        Checkbutton(rowTwoFrame, variable=self.SyringeInjFlag,text='Syringe Inj     ').pack(side=LEFT)
        
        Label(rowTwoFrame, text='  Avg Cycle').pack(side=LEFT)
        
        Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.avgCycle, 
              width=6).pack(side=LEFT)
        
        Label(rowTwoFrame, text='  Repeat Cycle').pack(side=LEFT)
        
        Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.repeatCycle, 
              width=6).pack(side=LEFT)
        
        Label(rowTwoFrame, text='  Calibration Cycle').pack(side=LEFT)
        
        Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.calibrationCycle, 
              width=6).pack(side=LEFT)
        rowTwoFrame.pack(side=TOP,fill=X,expand=1)   
        
        rowThreeFrame = Frame(MiscTableFrame,borderwidth=4,relief=FLAT)
        
        Checkbutton(rowThreeFrame, variable=self.OvenDoorManualFlag,text='Oven Door Manual  ').pack(side=LEFT)
        rowThreeFrame.pack(side=TOP,fill=X,expand=1) 
        
        rowFourFrame = Frame(MiscTableFrame,borderwidth=4,relief=FLAT)
        
        Entry(rowFourFrame,relief=SUNKEN, textvariable=self.SetFlow, width=6).pack(side=RIGHT)
        Label(rowFourFrame, text='Set Flow').pack(side=RIGHT)
        rowFourFrame.pack(side=TOP,fill=X,expand=1) 
        MiscTableFrame.pack(side=LEFT)
           
        # Now Create the next frame in panel3
        # This is the for the small frame for Flow settings
        
        FlowSettingFrame = LabelFrame(Panel3Frame,text='Flow = kV + d')
        #RowOneFrame = Frame(FlowSettingFrame,borderwidth=4,relief=FLAT)
        #Label(RowOneFrame, text='Flow = kV + d').grid(row=0,column=0, pady=3)
        #RowOneFrame.pack(side=TOP,fill=X,expand=1)  
        
        RowTwoFrame = Frame(FlowSettingFrame,borderwidth=4,relief=FLAT)
        
        Checkbutton(RowTwoFrame, variable=self.SensorSettingFlag,text='Sensor Setting').pack(side=TOP)
        RowTwoFrame.pack(side=TOP)
        
        RowThreeFrame = Frame(FlowSettingFrame,borderwidth=4,relief=FLAT)
        Label(RowThreeFrame, text='Slope k').pack(side=LEFT)
        
        entry= Entry(RowThreeFrame,relief=SUNKEN, textvariable=self.slope_k, 
                     width=6).pack(side=LEFT)  
        RowThreeFrame.pack(side=TOP)
        
        RowFourFrame = Frame(FlowSettingFrame,borderwidth=4,relief=FLAT)
        Label(RowFourFrame, text='Intercept d').pack(side=LEFT)
        
        entry= Entry(RowFourFrame,relief=SUNKEN, textvariable=self.intercept_d, 
                     width=6).pack(side=LEFT)     
        RowFourFrame.pack(side=TOP)
        
        #rowFiveFrameEmpty = Frame(FlowSettingFrame,borderwidth=4,relief=GROOVE)
        #rowFiveFrameEmpty.pack(side=TOP)
        
        
        FlowSettingFrame.pack(side=LEFT)
            
        Panel3Frame.pack(side=TOP,anchor=W)

        return


    def CreateMethodTableFrame(self):

        #methodTableFrame = Frame(self.popUpWindow,borderwidth=4,relief=GROOVE)
        
        
        #rowOneFrame = Frame(methodTableFrame,borderwidth=4,relief=FLAT)
        #Label(rowOneFrame, text='Method Table').grid(row=0,column=0)
        #rowOneFrame.pack(side=TOP,fill=X,expand=1)
        
        methodTableFrame=LabelFrame(self.popUpWindow,text="Method Table")
        
        rowTwoFrame = Frame(methodTableFrame,borderwidth=4,relief=FLAT)
        Label(rowTwoFrame, text='Inj/Det Temp').pack(side=LEFT)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.InjDetTemprature, 
                     width= 6).pack(side=LEFT)
        
        Label(rowTwoFrame, text='Calibrate Time').pack(side=LEFT)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.calibrateTime, 
                     width= 6).pack(side=LEFT)
        
        
        Label(rowTwoFrame, text='Analysis Time').pack(side=LEFT)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.analysis_time, 
                     width=6).pack(side=LEFT)

        Label(rowTwoFrame, text='Inject Time').pack(side=LEFT,anchor=W)
        
        entry= Entry(rowTwoFrame,relief=SUNKEN, textvariable=self.inject_time, 
                     width= 6).pack(side=LEFT)
        
        
        rowThreeFrame = Frame(methodTableFrame,borderwidth=4,relief=FLAT)
        Label(rowThreeFrame, text='Oven Temp').pack(side=LEFT,anchor=W)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.OvenTemp, 
                     width= 6).pack(side=LEFT,anchor=W,padx=7)
        
        Label(rowThreeFrame, text='Sample Time').pack(side=LEFT,anchor=W,padx=1)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.sample_time, 
                     width= 6).pack(side=LEFT,anchor=W)
                     
        Label(rowThreeFrame, text='Equil Time').pack(side=LEFT,anchor=W,padx=9)
        
        entry= Entry(rowThreeFrame,relief=SUNKEN, textvariable=self.equil_time, 
                     width= 6).pack(side=LEFT,anchor=W)
        rowTwoFrame.pack(side=TOP,ipadx=5)
        
        rowThreeFrame.pack(side=TOP,anchor=W)
       
        methodTableFrame.pack(side=TOP,anchor=W,padx=4)
        
        return
    def CreateBottomFrame(self):
        BottomFrame = Frame(self.popUpWindow,borderwidth=1,relief=SOLID)
        
        NotesFrame  = Frame(BottomFrame,borderwidth=4,relief=FLAT)
        Label(NotesFrame, text='Notes     ').pack(side=TOP)
        text_area = ScrolledText(NotesFrame,
                                          width = 40, 
                                          height = 5, 
                                          font = ("Times New Roman",
                                                  15))
        text_area.pack(side=TOP)  
        
        EntryFrame  = Frame(BottomFrame,borderwidth=2,relief=FLAT)
        
        entryRowOne   = Frame(EntryFrame,borderwidth=4,relief=FLAT)
        
        Label(entryRowOne, text='R1A ON').pack(side=LEFT)
        
        entry= Entry(entryRowOne,relief=SUNKEN, textvariable=self.R1AONval, 
                     width=6).pack(side=LEFT)     
        
        
        Label(entryRowOne, text='OFF').pack(side=LEFT)
        
        entry= Entry(entryRowOne,relief=SUNKEN, textvariable=self.R1AOFFval, 
                     width=6).pack(side=LEFT)     
        
        entryRowOne.pack(side=TOP)
        
        entryRowTwo   = Frame(EntryFrame,borderwidth=4,relief=FLAT)
       
        Label(entryRowTwo, text='R1B ON').pack(side=LEFT)
        
        entry= Entry(entryRowTwo,relief=SUNKEN, textvariable=self.R1BONval, 
                     width=6).pack(side=LEFT)     
        
       
        Label(entryRowTwo, text='OFF').pack(side=LEFT)
        
        entry= Entry(entryRowTwo,relief=SUNKEN, textvariable=self.R1BOFFval, 
                     width=6).pack(side=LEFT)     
        
        entryRowTwo.pack(side=TOP)
        
        entryRowThree = Frame(EntryFrame,borderwidth=4,relief=FLAT)
        Label(entryRowThree, text='X3   ON').pack(side=LEFT)
        
        entry= Entry(entryRowThree,relief=SUNKEN, textvariable=self.X3ONval, 
                     width=6).pack(side=LEFT)     
        
       
        Label(entryRowThree, text='OFF').pack(side=LEFT)
        
        entry= Entry(entryRowThree,relief=SUNKEN, textvariable=self.X3OFFval, 
                     width=6).pack(side=LEFT)     
        
        entryRowThree.pack(side=TOP)

        entryRowFour  = Frame(EntryFrame,borderwidth=4,relief=FLAT)
        Label(entryRowFour, text='X4   ON').pack(side=LEFT)
        
        entry= Entry(entryRowFour,relief=SUNKEN, textvariable=self.X4ONval, 
                     width=6).pack(side=LEFT)     
        
       
        Label(entryRowFour, text='OFF').pack(side=LEFT)
        
        entry= Entry(entryRowFour,relief=SUNKEN, textvariable=self.X4OFFval, 
                     width=6).pack(side=LEFT)     
        
        entryRowFour.pack(side=TOP)

        entryRowFive  = Frame(EntryFrame,borderwidth=4,relief=FLAT)
        Label(entryRowFive, text='X5   ON').pack(side=LEFT)
        
        entry= Entry(entryRowFive,relief=SUNKEN, textvariable=self.X5ONval, 
                     width=6).pack(side=LEFT)     
        
       
        Label(entryRowFive, text='OFF').pack(side=LEFT)
        
        entry= Entry(entryRowFive,relief=SUNKEN, textvariable=self.X5OFFval, 
                     width=6).pack(side=LEFT)     
        
        entryRowFive.pack(side=TOP)    
        
        
        ButtonFrame = Frame(self.popUpWindow,borderwidth=4,relief=GROOVE)
        Button(ButtonFrame, text ="  OK  ", command = self.OKCallBack).pack(side=LEFT,ipadx=4)
        Button(ButtonFrame, text ="Cancel", command=  self.CancelCallBack).pack(side=LEFT)
        Button(ButtonFrame, text =" Print ", command = self.PrintCallBack).pack(side=LEFT,ipadx=4)
        Button(ButtonFrame, text =" Help ", command = self.HelpCallBack).pack(side=LEFT,ipadx=4)
        
        NotesFrame.pack(side=LEFT)
        EntryFrame.pack(side=LEFT)
        ButtonFrame.pack(side=BOTTOM)
        BottomFrame.pack(side=TOP,anchor=W,padx=5)       
        return
        

        
    def CreateStatusBar(self):
        statusFrame = Frame(self.popUpWindow,borderwidth=1,relief=SOLID,highlightbackground="grey")
        statusbar = Label(statusFrame, text="This is where the status where status will be displayed", bd=1, relief=SUNKEN).pack(side=RIGHT,anchor=E)    
        statusFrame.pack(side=BOTTOM,anchor=E)
        
        
    def MethodEditEntry(self):        
        #Create a Toplevel window
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return
        self.popUpWindow.geometry("750x550")
        self.popUpWindow.resizable(False, False)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                    
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.title("Method")
        self.CreateMethodTableFrame()
        self.CreateTemperatureProgrammingFrame()
        self.CreateMiscTableFrame()
        self.CreateStatusBar()
        self.CreateBottomFrame()
        return

