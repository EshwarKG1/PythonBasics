import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd


class FileMenuOptions:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
                
        return
    def InitializeVariables(self):
        self.SaveFile  = StringVar()
        self.SaveFile.set("None")
        self.LoadFile  = StringVar()
        self.LoadFile.set("None")
        self.MethodFlag = BooleanVar()
        self.DetectorFlag = BooleanVar()
        self.ComponentsFlag = BooleanVar()
        self.StandardsFlag = BooleanVar()
        self.GraphFlag = BooleanVar()
        self.TableFlag = BooleanVar()
        self.PrintToFileFlag = BooleanVar()
        self.TkDetectorChoosen = StringVar()
        self.TkPrintQualityChoosen = StringVar()
        self.PrintReportPopUpWindow = None
        return
        
    def FileMenuNew(self):
        return        
    def FileMenuOpen(self):
        self.ShowFileOpenBrowser()
        if (self.LoadFile.get() == "None"):
            return
        # Load Job file
        
    def FileMenuSave(self):
        if (self.SaveFile.get() == "None"):
            self.FileMenuSaveAs()
        #else:
            # Save file 
        return
    def FileMenuSaveAs(self):
        self.ShowSaveFileAsBrowser("Save JOB file As")
        if  (self.SaveFile.get() == None):
             return
        # Save the contents to JOB file     
        return
        
    def SaveReport(self):
        self.ShowSaveReportAsBrowser("Save Report as file")
        return     
        
    def PrintReport(self):
        return     
        
    def ShowSaveFileAsBrowser(self,titleStr):
		
        filetypes = (
                     ('All files', '*.JOB'),
                     ('All files', '*.*')
                    )

        self.filename = fd.asksaveasfile(
                        title=titleStr,filetypes=filetypes)
       
        if (self.filename == None):
		   # User has pressed cancel Button
           return
		   
        self.SaveFile.set(self.filename)
        return    
        
    def ShowFileOpenBrowser(self):
       filetypes = (
                     ('All files', '*.JOB'),
                     ('All files', '*.*')
                    )

       self.filename = fd.askopenfilename(
                     title='Load Job from a file',
                     initialdir='/',
                     filetypes=filetypes)
       if (self.filename == None):
            return
         
       self.LoadFile.set(self.filename)
        
       return    
       
    def ShowSaveReportAsBrowser(self,titleStr):
		
        filetypes = (
                     ('All files', '*.rtf'),
                     ('All files', '*.*')
                    )

        self.filename = fd.asksaveasfile(
                        title=titleStr,filetypes=filetypes)
       
        if (self.filename == None):
		   # User has pressed cancel Button
           return
		   
        self.SaveFileName.set(self.filename)
        
        return    
        
    def PrintReportPopUp(self):
        if (self.PrintReportPopUpWindow == None):
            self.PrintReportPopUpWindow= Toplevel(self.parentWindow)
        else:
            return
        
        self.PrintReportPopUpWindow.attributes('-topmost',True)
        self.PrintReportPopUpWindow.protocol("WM_DELETE_WINDOW", self.PrintReportPopUpWindowXPressed)                            
        self.PrintReportPopUpWindow.geometry("250x275")
        self.PrintReportPopUpWindow.resizable(False, False)
        self.PrintReportPopUpWindow.title("Print Report")
        FirstFrame  = Frame(self.PrintReportPopUpWindow,borderwidth=4,relief=FLAT)
        Label(FirstFrame, text='Printer').pack(side=LEFT,anchor=W,padx=5)
        Label(FirstFrame, text='Cannon Ink Jet Printer').pack(side=LEFT)
        SecondFrame = LabelFrame(self.PrintReportPopUpWindow,text='Print Items')        

        SecondFrameLeftSideFrame  = Frame(SecondFrame,borderwidth=4,relief=FLAT)
        SecondFrameRightSideFrame  = Frame(SecondFrame,borderwidth=4,relief=FLAT)
        
        detectorChoosen = ttk.Combobox(SecondFrameLeftSideFrame, width = 10, 
                            textvariable = self.TkDetectorChoosen)
        detectorChoosen['values'] = ('DetectorA', 'DetectorB')
        detectorChoosen.pack(side=TOP)                 
        detectorChoosen.current(1) 

        
        Checkbutton(SecondFrameLeftSideFrame, variable=self.MethodFlag,text='Method').pack(side=TOP,anchor=W)
        Checkbutton(SecondFrameLeftSideFrame, variable=self.DetectorFlag,text='Detector').pack(side=TOP,anchor=W)
        Checkbutton(SecondFrameLeftSideFrame, variable=self.ComponentsFlag,text='Components').pack(side=TOP,anchor=W)
        Checkbutton(SecondFrameLeftSideFrame, variable=self.StandardsFlag,text='Standards').pack(side=TOP,anchor=W)        
        SecondFrameLeftSideFrame.pack(side=LEFT)
        

        Checkbutton(SecondFrameRightSideFrame, variable=self.GraphFlag,text='Graph').pack(side=TOP,anchor=W)
        Checkbutton(SecondFrameRightSideFrame, variable=self.TableFlag,text='Table').pack(side=TOP,anchor=W)
        SecondFrameRightSideFrame.pack(side=LEFT)
        
        
        ThirdFrame  = Frame(self.PrintReportPopUpWindow,borderwidth=4,relief=FLAT)
        Label(ThirdFrame, text='Print Quality').pack(side=LEFT,anchor=W,padx=5)
        printQualityChoosen = ttk.Combobox(ThirdFrame, width = 10, 
                            textvariable = self.TkPrintQualityChoosen)
        printQualityChoosen['values'] = ('600 dpi', '300 dpi')
        printQualityChoosen.pack(side=LEFT,anchor=W)                 
        printQualityChoosen.current(1) 
        
        FourthFrame  = Frame(self.PrintReportPopUpWindow,borderwidth=4,relief=FLAT)
        Checkbutton(FourthFrame, variable=self.PrintToFileFlag,text='Print To file').pack(side=TOP,anchor=W)   
        
        ButtonFrame = Frame(self.PrintReportPopUpWindow,borderwidth=4,relief=FLAT)
        Button(ButtonFrame, text ="  OK  ", command  =  self.PrintReportOKCallBack,width=6).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.PrintReportCancelCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text =" Setup ", command  =  self.PrintSetupCallBack,width=6).pack(side=LEFT,ipadx=5)        
        
        FirstFrame.pack(side=TOP)
        SecondFrame.pack(side=TOP)
        ThirdFrame.pack(side=TOP,anchor=W)
        FourthFrame.pack(side=TOP,anchor=W)
        ButtonFrame.pack(side=TOP)
        return 
        
    def PrintReportOKCallBack(self):
        self.PrintReportPopUpWindow.destroy()    
        self.PrintReportPopUpWindow = None
        return
        
    def PrintReportCancelCallBack(self):
        self.PrintReportPopUpWindow.destroy()
        self.PrintReportPopUpWindow = None
        return        
        
    def PrintReportPopUpWindowXPressed(self):
        self.PrintReportCancelCallBack()
        return
        
    def PrintSetupCallBack(self):
        return
