from tkinter import *

from tkinter import ttk
class Detector:
  def __init__(self, name, parentwindow):
    self.detector          =  name
    self.parentWindow      =  parentwindow
    self.popUpWindow       =  None
    self.LabelStr          =  StringVar()
    self.OnOffFlag         =  BooleanVar()
    self.LogFlag           =  BooleanVar()
    self.externalFlag      =  BooleanVar()
    self.invertFlag        =  BooleanVar()
    self.TimeStr           =  StringVar()
    self.LengthStr         =  StringVar()
    self.minArea           =  StringVar()
    self.minHeight         =  StringVar()
    self.PeaksVar          =  IntVar()
    self.segmentWidth      =  StringVar()
    self.units             =  StringVar()
    self.PeaksAlgorithm    =  IntVar()
    self.DetectMethod      =  IntVar()
    self.dataToExcelFlag       =  BooleanVar()
    self.lampSaveFlag          =  BooleanVar()
    self.autoFlag          =  BooleanVar()
    self.RangeSelection    =  StringVar()
    self.Range_1_Selection =  StringVar()
    self.values = {} # Initalize the dictionary 
    self.helpPopUp = None
    self.popUpWindow = None    
    return
    
  def OKCallBack(self):
    #print("Inside OK CAll back")
    # Put all data into a python variables
    self.popUpWindow.destroy()
    self.popUpWindow               = None
    self.detectorLabelStr          =  self.LabelStr.get()      
    self.detectorOnOffFlag         =  self.OnOffFlag.get()        
    self.detectorLogFlag           =  self.LogFlag.get()  
    self.detectorExternalFlag      =  self.externalFlag.get()    
    self.detectorInvertFlag        =  self.invertFlag.get()  
    self.detectorTimeStr           =  self.TimeStr.get()  
    self.detectorLengthStr         =  self.LengthStr.get()    
    self.detectorMinArea           =  self.minArea.get()  
    self.detectorMinHeight         =  self.minHeight.get()    
    self.detectorPeaksVar          =  self.PeaksVar.get()  
    self.detectorSegmentWidth      =  self.segmentWidth.get()   
    self.detectorUnits             =  self.units.get()  
    self.detectorPeaksAlgorithm    =  self.PeaksAlgorithm.get()     
    self.detectorDetectMethod      =  self.DetectMethod.get()  
    self.detectorDataToExcelFlag   =  self.dataToExcelFlag.get()  
    self.detectorLampSaveFlag      =  self.lampSaveFlag.get()  
    self.detectorAutoFlag          =  self.autoFlag.get()  
    self.detectorRangeSelection    =  self.RangeSelection.get()   
    self.detectorRange_1_Selection =  self.Range_1_Selection.get()  
    
    self.values['DetectorName'] = self.detector
    self.values['Label']        = self.detectorLabelStr 
    self.values['OnOffFlag']    = self.detectorOnOffFlag
    self.values['LogFlag']      = self.detectorLogFlag 
    self.values['ExternalFlag'] = self.detectorExternalFlag 
    self.values['InvertFlag']   = self.detectorInvertFlag
    self.values['Time']         = self.detectorTimeStr 
    self.values['Length']       = self.detectorLengthStr 
    self.values['MinArea']      = self.detectorMinArea
    self.values['MinHeight']    = self.detectorMinHeight 
    self.values['Peaks']        = self.detectorPeaksVar 
    self.values['SegmentWidth'] = self.detectorSegmentWidth 
    self.values['Units']        = self.detectorUnits
    self.values['PeakAlgorithm']= self.detectorPeaksAlgorithm
    self.values['DetectMethod'] = self.detectorDetectMethod 
    self.values['DataToExcel']  = self.detectorDataToExcelFlag 
    self.values['LampSave']     = self.detectorLampSaveFlag 
    self.values['Auto']         = self.detectorAutoFlag
    self.values['Range']        = self.detectorRangeSelection 
    self.values['Range1']       = self.detectorRange_1_Selection 
    #print(self.values)
    return
    
  def GetValueFromDetector(self):
      return self.values
    
  def CancelCallBack(self):
      self.popUpWindow.destroy()      
      self.popUpWindow = None
      return
      
  def CloseHelp(self):
      self.helpPopUp.destroy
      self.helpPopUp = None
      return
  def helpPopUpXPressed(self):
      CloseHelp()
      

  def HelpCallBack(self):
        if (self.helpPopUp == None):
            self.helpPopUp= Toplevel(self.parentWindow)
        else:
            return 
            
        self.helpPopUp.attributes('-topmost',True)
        self.helpPopUp.protocol("WM_DELETE_WINDOW", self.helpPopUpXPressed)        
        self.helpPopUp.title("Help")
        self.helpPopUp.resizable(False, False)
        TextWindow = Text(self.helpPopUp, height = 5, width = 50)
        l = Label(self.helpPopUp, text = "Detector ")
        Fact = "This window is used  various Detector parameters,refer to PID Analyzer documentation  details"
        TextWindow.insert(END, Fact)
        TextWindow.config(state=DISABLED,wrap=WORD )
        # Create an Exit button.    
        b2 = Button(self.helpPopUp, text = "OK",  command = self.CloseHelp) 
        l.pack()
        TextWindow.pack()
        b2.pack()
        return
  def popUpWindowXPressed(self):
      self.CancelCallBack()
      return

  def DetectorPopUp(self):    
    #Create a Toplevel window
    if (self.popUpWindow == None):
       self.popUpWindow= Toplevel(self.parentWindow)
    else:
       return
    self.popUpWindow.geometry("400x350")
    titleStr = "Detector" + self.detector 
    self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)            
    self.popUpWindow.title(titleStr)
    self.popUpWindow.resizable(False, False)
    self.popUpWindow.attributes('-topmost',True)
    Panel1Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    Panel2Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    Panel3Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    Panel4Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    Panel5Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    Panel6Frame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
    
    Column1 = Frame(Panel1Frame,borderwidth=4,relief=FLAT)
    Label(Column1, text='Label').pack(side=LEFT, anchor=N)
    
    Entry(Column1,relief=SUNKEN, textvariable=self.LabelStr, width=15).pack(side=LEFT,anchor=W)
    Column1.pack(side=LEFT,anchor=W)
    
    Column2 = Frame(Panel1Frame,borderwidth=4,relief=FLAT)
    Column2Row1 = Frame(Column2,borderwidth=4,relief=FLAT)

    Checkbutton(Column2Row1, variable=self.OnOffFlag,text='On  / Off').pack(side=LEFT,anchor=N)
    Checkbutton(Column2Row1, variable=self.LogFlag,text='Log  ').pack(side=LEFT,anchor=N)
    
    Column2Row2 = Frame(Column2,borderwidth=4,relief=FLAT)
    Checkbutton(Column2Row2, variable=self.externalFlag,text='External').pack(side=LEFT)
    Checkbutton(Column2Row2, variable=self.invertFlag,text='Invert').pack(side=LEFT)
    
    Column2Row1.pack(side=TOP)
    Column2Row2.pack(side=TOP)
    Column2.pack(side=LEFT,anchor=W)
    #============== PANEL-1 END
    
    
    #======== PANEL-2 Starts =========================
    
    Panel2Column1 = LabelFrame(Panel2Frame, text="Noise & Baseline")  
    
    
    
    Label(Panel2Column1, text='Time').grid(column=0, row=0)
    Entry(Panel2Column1,relief=SUNKEN, textvariable=self.TimeStr, width=10).grid(column=2, row=0)
    
    
    Label(Panel2Column1, text='Length').grid(column=0, row=1)
    Entry(Panel2Column1,relief=SUNKEN, textvariable=self.LengthStr, width=10).grid(column=2, row=1)
    Panel2Column1.pack(side=LEFT)  
    
    Panel2Column2 = LabelFrame(Panel2Frame, text="Filter")  
    
    Label(Panel2Column2, text='Min Area').grid(column=0, row=0)
    Entry(Panel2Column2,relief=SUNKEN, textvariable=self.minArea, width=10).grid(column=1, row=0)
    
    
    Label(Panel2Column2, text='Min. Height').grid(column=0, row=1)
    Entry(Panel2Column2,relief=SUNKEN, textvariable=self.minHeight, width=10).grid(column=1,row=1)
    Panel2Column2.pack(side=LEFT,padx=40)
    
    Panel2Column3 = LabelFrame(Panel2Frame, text="Peaks")  

    
    R1 = Radiobutton(Panel2Column3, text="All", variable=self.PeaksVar, value=1)
    R1.grid(column=2,row=0,sticky=W)

    R2 = Radiobutton(Panel2Column3, text="Known", variable=self.PeaksVar, value=2)
    R2.grid(column=2,row=1)  
    Panel2Column3.pack(side=LEFT)
    
    #======== PANEL-2 Ends =========================
    
    #=====Panel=3 Starts
    
    Label(Panel3Frame, text='Segment Width').pack(side=LEFT)
    Entry(Panel3Frame,relief=SUNKEN, textvariable=self.segmentWidth, width=5).pack(side=LEFT,anchor=W)
    

    Label(Panel3Frame, text='Units').pack(side=LEFT)
    Entry(Panel3Frame,relief=SUNKEN, textvariable=self.units, width=5).pack(side=LEFT,anchor=W)
    
    #=====Panel=3 Ends
    
    #===== Panel-4 Starts ===
    Panel4Column1 = LabelFrame(Panel4Frame, text="Peak Algorithm")  
    

    R1 = Radiobutton(Panel4Column1, text="Baseline Projection", variable=self.PeaksAlgorithm, value=1)
    R1.grid(column=0,row=0,sticky=W)

    R2 = Radiobutton(Panel4Column1, text="Tangent Sinking", variable=self.PeaksAlgorithm, value=2)
    R2.grid(column=0,row=1,sticky=W)  
    

    R3 = Radiobutton(Panel4Column1, text="Peaks Deconvcolute", variable=self.PeaksAlgorithm, value=3)
    R3.grid(column=0,row=2,sticky=W)  
    
    Panel4Column1.pack(side=LEFT,anchor=W)
    
    Panel4Column2 = LabelFrame(Panel4Frame, text="Detect Method")
    
    
    R1 = Radiobutton(Panel4Column2, text="Height", variable=self.DetectMethod, value=1)
    R1.grid(column=0,row=0,sticky=W)

    R2 = Radiobutton(Panel4Column2, text="Area", variable=self.DetectMethod, value=2)
    R2.grid(column=0,row=1,sticky=W)  
    
 
    Panel4Column2.pack(side=LEFT,anchor=W)
    #===== Panel-4 Ends ===
    
    #===== Panel-5 Ends ===    
    #Panel5Frame
    
    Checkbutton(Panel5Frame, variable=self.dataToExcelFlag,text='Data To Excel').pack(side=LEFT, anchor=W)
    
    
    Checkbutton(Panel5Frame, variable=self.lampSaveFlag,text='Lamp Save').pack(side=LEFT, anchor=W)
    
    
    Checkbutton(Panel5Frame, variable=self.autoFlag,text='Auto').pack(side=LEFT, anchor=W)
    
    Label(Panel5Frame, text='Range').pack(side=LEFT, anchor=W)
 
    RangeOptions = ttk.Combobox(Panel5Frame, width = 4, textvariable = self.RangeSelection)
    RangeOptions['values'] = ('1','10','100','1000')
    RangeOptions.pack(side=LEFT,anchor=W)
    RangeOptions.current(2)
    
    
    Label(Panel5Frame, text='Range-1').pack(side=LEFT, anchor=W)
    
    Range_1_Options = ttk.Combobox(Panel5Frame, width = 4, textvariable = self.Range_1_Selection)
    Range_1_Options['values'] = ('1','10','100','1000')
    Range_1_Options.pack(side=LEFT,anchor=W)
    Range_1_Options.current(2)

    
    #===== Panel-5 Ends ===
    
    #=========== Panel -6 Starts
    Button(Panel6Frame, text ="  OK  ", command=self.OKCallBack).pack(side=LEFT,ipadx=4)
    Button(Panel6Frame, text ="Cancel", command=self.CancelCallBack).pack(side=LEFT)
    Button(Panel6Frame, text =" Help ", command = self.HelpCallBack).pack(side=LEFT,ipadx=4)
 
    #=========== Panel -6 Ends
    Panel1Frame.pack(side=TOP, anchor=W)
    Panel2Frame.pack(side=TOP, anchor=W)
    Panel3Frame.pack(side=TOP, anchor=W)
    Panel4Frame.pack(side=TOP,anchor=W)
    Panel5Frame.pack(side=TOP,anchor=W)
    Panel6Frame.pack(side=TOP,anchor=S)
    return


