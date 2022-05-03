import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd


class ViewMenuOptions:
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
        self.AxisForGraphPopUpWindow  = None
        return
        
        
    def AxisForGraphPopUp(self):
        if (self.AxisForGraphPopUpWindow == None):
            self.AxisForGraphPopUpWindow= Toplevel(self.parentWindow)
        else:
            return
        self.AxisForGraphPopUpWindow.geometry('200x290')
        self.AxisForGraphPopUpWindow.title('Axis for Graph A')
        self.AxisForGraphPopUpWindow.protocol("WM_DELETE_WINDOW", self.AxisForGraphPopUpWindowXPressed)                            
        self.AxisForGraphPopUpWindow.attributes('-topmost',True)
        self.AxisForGraphPopUpWindow.resizable(False, False)

        FrameOne   = LabelFrame(self.AxisForGraphPopUpWindow,text='X')  
        
        FrameOneLineOne = Frame(FrameOne,borderwidth=4,relief=FLAT)
        Label(FrameOneLineOne, text='Min').pack(side=LEFT)
        Entry(FrameOneLineOne,relief=SUNKEN, textvariable=self.xMin, width=20).pack(side=LEFT) 
        FrameOneLineOne.pack(side=TOP)
        
        FrameOneLineTwo = Frame(FrameOne,borderwidth=4,relief=FLAT)        
        Label(FrameOneLineTwo, text='Max').pack(side=LEFT)        
        Entry(FrameOneLineTwo,relief=SUNKEN, textvariable=self.xMax, width=20).pack(side=LEFT)  
        FrameOneLineTwo.pack(side=TOP)
        
        FrameOneLineThree = Frame(FrameOne,borderwidth=4,relief=FLAT)         
        Label(FrameOneLineThree, text='k').pack(side=LEFT)        
        Entry(FrameOneLineThree,relief=SUNKEN, textvariable=self.xK, width=20).pack(side=LEFT)        
        FrameOneLineThree.pack(side=TOP)
        
        FrameOneLineFour = Frame(FrameOne,borderwidth=4,relief=FLAT)
        Checkbutton(FrameOne, variable=self.xAxisAuto,text='Auto').pack(side=TOP,anchor=W) 
        FrameOneLineFour.pack(side=TOP)

        FrameTwo   = LabelFrame(self.AxisForGraphPopUpWindow,text='Y')
        
        FrameTwoLineOne = Frame(FrameTwo,borderwidth=4,relief=FLAT)
        Label(FrameTwoLineOne, text='Min').pack(side=LEFT)
        Entry(FrameTwoLineOne,relief=SUNKEN, textvariable=self.yMin, width=20).pack(side=TOP)        
        FrameTwoLineOne.pack(side=TOP)
        
        FrameTwoLineTwo = Frame(FrameTwo,borderwidth=4,relief=FLAT)
        Label(FrameTwoLineTwo, text='Max').pack(side=LEFT)
        Entry(FrameTwoLineTwo,relief=SUNKEN, textvariable=self.yMax, width=20).pack(side=TOP)        
        FrameTwoLineTwo.pack(side=TOP)
        
        FrameTwoLineThree = Frame(FrameTwo,borderwidth=4,relief=FLAT)
        Label(FrameTwoLineThree, text='k').pack(side=LEFT)
        Entry(FrameTwoLineThree,relief=SUNKEN, textvariable=self.yK, width=20).pack(side=TOP)    
        FrameTwoLineThree.pack(side=TOP)
        
        FrameTwoLineFour = Frame(FrameTwo,borderwidth=4,relief=FLAT)       
        Checkbutton(FrameTwoLineFour, variable=self.yAxisAuto,text='Auto').pack(side=TOP,anchor=W)        
        
        ButtonFrame = Frame(self.AxisForGraphPopUpWindow,borderwidth=4,relief=FLAT)        
        Button(ButtonFrame, text ="OK",     command = self.AxisForGraphOK).pack(side=LEFT,ipadx=4)             
        Button(ButtonFrame, text ="Cancel", command = self.AxisForGraphCancel).pack(side=LEFT,ipadx=4)             
        Button(ButtonFrame, text ="Help",   command = self.AxisForGraphHelp).pack(side=LEFT,ipadx=4)             
        
        FrameOne.pack(side=TOP)
        FrameTwo.pack(side=TOP)
        ButtonFrame.pack(side=TOP)
        return
        
    def AxisForGraphOK(self):
        self.AxisForGraphPopUpWindow.destroy()
        self.AxisForGraphPopUpWindow = None
        return
        
    def AxisForGraphCancel(self):
        self.AxisForGraphPopUpWindow.destroy()
        self.AxisForGraphPopUpWindow = None
        return
        
    def AxisForGraphPopUpWindowXPressed(self):
        self.AxisForGraphCancel()
        return    
        
    def AxisForGraphHelp(self):
    
        return
        