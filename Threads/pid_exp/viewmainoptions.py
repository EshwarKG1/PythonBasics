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
        self.xAxisAuto = BooleanVar()
        self.yAxisAuto = BooleanVar()
        self.xMin      = StringVar()
        self.xMax      = StringVar()
        self.xK        = StringVar()
        self.yMin      = StringVar()
        self.yMax      = StringVar()
        self.yK        = StringVar()
        
        return
        
        
    def AxisForGraphPopUp(self):
        self.AxisForGraphPopUpWindow= Toplevel(self.parentWindow)
        self.AxisForGraphPopUpWindow.geometry('550x200')
        self.AxisForGraphPopUpWindow.title('Axis for Graph A')
        self.AxisForGraphPopUpWindow.resizable(False, False)

        FrameOne   = LabelFrame(self.AxisForGraphPopUpWindow,text='X')      
        Entry(FrameOne,relief=SUNKEN, textvariable=self.xMin, width=20).pack(side=TOP)        
        Entry(FrameOne,relief=SUNKEN, textvariable=self.xMax, width=20).pack(side=TOP)        
        Entry(FrameOne,relief=SUNKEN, textvariable=self.xK, width=20).pack(side=TOP)        
        
        Checkbutton(FrameOne, variable=self.xAxisAuto,text='Auto').pack(side=TOP,anchor=W)        

        FrameTwo   = LabelFrame(self.AxisForGraphPopUpWindow,text='Y')
        Entry(FrameTwo,relief=SUNKEN, textvariable=self.yMin, width=20).pack(side=TOP)        
        Entry(FrameTwo,relief=SUNKEN, textvariable=self.yMax, width=20).pack(side=TOP)        
        Entry(FrameTwo,relief=SUNKEN, textvariable=self.yK, width=20).pack(side=TOP)        
       
        Checkbutton(FrameTwo, variable=self.yAxisAuto,text='Auto').pack(side=TOP,anchor=W)        
        
        ButtonFrame = Frame(self.AxisForGraphPopUpWindow,borderwidth=4,relief=FLAT)        
        Button(ButtonFrame, text ="OK",     command = self.AxisForGraphOK).pack(side=LEFT,ipadx=4)             
        Button(ButtonFrame, text ="Cancel", command = self.AxisForGraphCancel).pack(side=LEFT,ipadx=4)             
        Button(ButtonFrame, text ="Help",   command = self.AxisForGraphHelp).pack(side=LEFT,ipadx=4)             
        
        FrameOne.pack(side=TOP)
        FrameTwo.pack(side=TOP)
        ButtonFrame.pack(side=TOP)
        return
        