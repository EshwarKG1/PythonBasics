#=====================================================================================    
#  Run Menu  Implementation
#  Top Menu Bar: Menu->Run -..... > All menu options are implemented here
#  Author : Girish S Kumar
#  Date 26-Nov-2021
#=====================================================================================  
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd


class CalibrationAcquire:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
        return
        
    def InitializeVariables(self):
        self.popUpWindow = None
        return
        
    def SelectStandardCallBack(self):
        self.StandardVal = str(self.standard)
        return
        
    def SelectStandardOKCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def SelectStandardCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
    def popUpWindowXPressed(self):
        self.SelectStandardCancelCallBack()
        return
    def SelectStandardHelpCallBack(self):
        return
    
    def TablePopUp(self):
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return
            
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.geometry('350x140')
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                            
        self.popUpWindow.title('Select Standard to save Calibration')
        self.popUpWindow.resizable(False, False)
        
        frameA = LabelFrame(self.popUpWindow,text="Select Standard to save Calibration")
        self.standard = IntVar()
        self.standard.set(1)
        R1 = Radiobutton(frameA, text="Stand 0", variable=self.standard , value=1,
                  command=self.SelectStandardCallBack)
        R1.pack( anchor = W )

        R2 = Radiobutton(frameA, text="Stand 1", variable=self.standard , value=2,
                  command=self.SelectStandardCallBack)
        R2.pack( anchor = W )

        R3 = Radiobutton(frameA, text="Stand 2", variable=self.standard , value=3,
                  command=self.SelectStandardCallBack)
        R3.pack( anchor = W)
        
        R4 = Radiobutton(frameA, text="Stand 3", variable=self.standard , value=4,
                  command=self.SelectStandardCallBack)
        R4.pack( anchor = W)
        
        frameA.pack(side=LEFT,padx=5)
        
        ButtonFrame=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Button(ButtonFrame, text ="OK",     command  =  self.SelectStandardOKCallBack,width=6).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.SelectStandardCancelCallBack,width=6).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Help",   command  =  self.SelectStandardHelpCallBack,width=6).pack(side=TOP,pady=5)
        ButtonFrame.pack(side=LEFT)
        return        
        
class RunModes:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
        return
        
    def InitializeVariables(self):
        self.popUpWindow= None
        return

        
    def SelectRunModeCallBack(self):
        return
        
    def SelectRunModeOKCallBack(self):
        self.AcquireMode  = str(self.acquireMode)
        self.SaveRunMode  = str(self.saveRunMode)
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def SelectRunModeCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
    def popUpWindowXPressed(self):
        self.SelectRunModeCancelCallBack()
        return    
    def SelectRunModeHelpCallBack(self):
        return
        
    def TablePopUp(self):
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
             return
             
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                    
        self.popUpWindow.geometry('300x140')
        self.popUpWindow.title('Run Modes')
        self.popUpWindow.resizable(False, False)
        
        frameA = LabelFrame(self.popUpWindow,text="Acquire Mode")
        self.acquireMode = IntVar()
        self.acquireMode.set(1)
        R1 = Radiobutton(frameA, text="Manual", variable=self.acquireMode , value=1,
                  command=self.SelectRunModeCallBack)
        R1.pack( anchor = W )

        R2 = Radiobutton(frameA, text="Continious", variable=self.acquireMode , value=2,
                  command=self.SelectRunModeCallBack)
        R2.pack( anchor = W )

        R3 = Radiobutton(frameA, text="Repeat", variable=self.acquireMode , value=3,
                  command=self.SelectRunModeCallBack)
        R3.pack( anchor = W)
        
        R4 = Radiobutton(frameA, text="Remote", variable=self.acquireMode , value=4,
                  command=self.SelectRunModeCallBack)
        R4.pack( anchor = W)
        
        frameA.pack(side=LEFT,padx=5)

        frameB = LabelFrame(self.popUpWindow,text="Save Run Mode")
        self.saveRunMode = IntVar()
        self.saveRunMode.set(1)
        R1 = Radiobutton(frameB, text="Manual", variable=self.saveRunMode, value=1,
                  command=self.SelectRunModeCallBack)
        R1.pack( anchor = W )

        R2 = Radiobutton(frameB, text="Auto", variable=self.saveRunMode , value=2,
                  command=self.SelectRunModeCallBack)
        R2.pack( anchor = W )

        R3 = Radiobutton(frameB, text="OnAlarm", variable=self.saveRunMode , value=3,
                  command=self.SelectRunModeCallBack)
        R3.pack( anchor = W)
        
        frameB.pack(side=LEFT,padx=5)


        ButtonFrame=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Button(ButtonFrame, text ="OK",     command  =  self.SelectRunModeOKCallBack,width=6).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.SelectRunModeCancelCallBack).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Help",   command  =  self.SelectRunModeHelpCallBack).pack(side=TOP,pady=5)
        ButtonFrame.pack(side=LEFT)
        return


class Runs:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
        self.selectedRun = (0,)
        return
        
    def InitializeVariables(self):
        self.popUpWindow = None
        self.ListOfRuns = []
        self.SaveFile   = StringVar()
        self.SaveFile.set("None")
        record = {'Select' : 'No', 'Date' : '27-Nov-2021', 'Time': '16:41:10' , 'Comments' : 'For Testing'}
        self.ListOfRuns.append(record)
        record = {'Select' : 'No', 'Date' : '27-Nov-2021', 'Time': '18:41:10' , 'Comments' : 'For Testing'}
        self.ListOfRuns.append(record)
        return
        
    def SelectRunsOKCallBack(self):
        self.selectedRun  = self.listbox.curselection()
        if (len(self.selectedRun) != 0):
           self.runIndex = self.selectedRun[0] # First element in the tuple
           if (self.runIndex == -1):
               self.runIndex = 0

        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def SelectRunsCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def popUpWindowXPressed(self):
        SelectRunsCancelCallBack()
        return    
        
    def SelectRunsHelpCallBack(self):
        return
        
    
    def SelectRunPopUp(self):
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return
            
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                    
        self.popUpWindow.geometry('550x200')
        self.popUpWindow.title('Select Run')
        self.popUpWindow.resizable(False, False)
        headingRowFrame =Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Label(headingRowFrame, text='Select        Date               Time        Comments').pack(side=LEFT)
        headingRowFrame.pack(side=TOP,anchor=W)

        Frame1=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        self.listbox = Listbox(Frame1,selectmode=BROWSE,width=50)
        self.listbox.pack(side = LEFT)
        scrollbar = Scrollbar(Frame1)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        for record in self.ListOfRuns:
            recordStr =''
            recordStr = record['Select'] + "     " + record['Date'] + "     " + record['Time'] + "     " + record['Comments']
            self.listbox.insert(END, recordStr)
            
        self.listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.listbox.yview)
        Frame1.pack(side=LEFT)
        
        ButtonFrame=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Button(ButtonFrame, text ="OK",     command  =  self.SelectRunsOKCallBack,width=6).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.SelectRunsCancelCallBack).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Help",   command  =  self.SelectRunsHelpCallBack,width=6).pack(side=TOP,pady=5)
        ButtonFrame.pack(side=LEFT)
        return
        
    def EditRunsModeOKCallBack(self):
        self.record['Comments'] = self.text_area.get("1.0", tk.END)        
        self.ListOfRuns.pop(self.runIndex)  # Remove the old record 
        self.ListOfRuns.insert(self.runIndex,self.record) # Insert new record with new comments
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def EditRunsModeCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def popUpWindowXPressed(self):
        self.EditRunsModeCancelCallBack()
        return    
        
    def EditRunsModeHelpCallBack(self): 
        return

    def EditRunPopUp(self):
    
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return

        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                            
        self.popUpWindow.geometry('280x250')
        self.popUpWindow.title('Run Modes')
        self.popUpWindow.resizable(False, False)
        if (len(self.selectedRun) > 0):
           self.runIndex = self.selectedRun[0] # First element in the tuple
           if (self.runIndex == -1):
              self.runIndex = 0
        else:
           self.runIndex = 0
		   
        self.record=self.ListOfRuns[self.runIndex]
        
        FrameOne=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        
        # Show data and time and LabelFrame
        # Display an Edit box for updating comments
        # Update the contents of edit into the comment section of the selected Run
        dateAndTime = self.record['Date'] + '       ' + self.record['Time']
        
        Label(FrameOne, text=dateAndTime).pack(side=LEFT)
        FrameOne.pack(side=TOP,anchor=W)
       
        FrameTwo=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Label(FrameTwo, text="Comments").pack(side=LEFT)
        FrameTwo.pack(side=TOP,anchor=W)
        
        FrameThree=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        self.commentVar = StringVar()
        self.commentVar.set(self.record['Comments'])
        #entryField= Entry(FrameThree,relief=SUNKEN, textvariable=self.commentVar, width=20).pack(side=LEFT)
        self.text_area = ScrolledText(FrameThree,
                                 width  = 40, 
                                 height = 5, 
                                 font   = ("Times New Roman",15))
        self.text_area.insert(tk.INSERT,self.commentVar.get())                         
        self.text_area.pack(side=TOP,anchor=W)
        FrameThree.pack(side=TOP,anchor=W)             
        
        ButtonFrame=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
                
        
        Button(ButtonFrame, text ="OK",     command  =  self.EditRunsModeOKCallBack).pack(side=LEFT,pady=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.EditRunsModeCancelCallBack).pack(side=LEFT,pady=5)
        Button(ButtonFrame, text ="Help",   command  =  self.EditRunsModeHelpCallBack).pack(side=LEFT,pady=5)
        ButtonFrame.pack(side=TOP)
        return
        
    def SaveCalibrationResultsOKCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def SaveCalibrationResultsCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
    def popUpWindowXPressed(self):
        self.SaveCalibrationResultsCancelCallBack()
        return    
    def SaveCalibrationResultsHelpCallBack(self):
        return
        
    def SaveCalibrationResults(self):
    
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return

        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                            
        self.popUpWindow.geometry('550x160')
        self.popUpWindow.title('Run Modes')
        self.popUpWindow.resizable(False, False)
        headingRowFrame =Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Label(headingRowFrame, text='Select        Date               Time        Comments').pack(side=LEFT)
        headingRowFrame.pack(side=TOP,anchor=W)

        Frame1=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        self.listbox = Listbox(Frame1,selectmode=BROWSE,width=50)
        self.listbox.pack(side = LEFT)
        scrollbar = Scrollbar(Frame1)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        for record in self.ListOfRuns:
            recordStr =''
            recordStr = record['Select'] + "     " + record['Date'] + "     " + record['Time'] + "     " + record['Comments']
            self.listbox.insert(END, recordStr)
            
        self.listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.listbox.yview)
        Frame1.pack(side=LEFT)
        
        ButtonFrame=Frame(self.popUpWindow,borderwidth=4,relief=FLAT)
        Button(ButtonFrame, text ="OK",     command  =  self.SaveCalibrationResultsOKCallBack,width=6).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.SaveCalibrationResultsCancelCallBack).pack(side=TOP,pady=5)
        Button(ButtonFrame, text ="Help",   command  =  self.SaveCalibrationResultsHelpCallBack).pack(side=TOP,pady=5)
        ButtonFrame.pack(side=LEFT)

        return
    def ShowSaveFileBrowser(self,titleStr):
		
        filetypes = (
                     ('All files', '*.rwp'),
                     ('All files', '*.*')
                    )

        self.filename = fd.asksaveasfilename (
                        title=titleStr,filetypes=filetypes)
        if (self.filename == None):
		   # User has pressed cancel Button
           return
		   
        self.SaveFile.set(self.filename)
		
        # Get Raw peaks and save the data to file
        return    
		
    def SaveIntegrationResults(self):
        self.ShowSaveFileBrowser("Save Raw Peaks As file")
        


