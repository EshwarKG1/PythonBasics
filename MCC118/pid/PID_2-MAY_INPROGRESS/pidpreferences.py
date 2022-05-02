from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import ttk
import json

class PIDPreferences:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.environmentFlag   = False
        self.WindowFlag            = False
        self.DesktopFlag           = False
        self.MethodFlag            = False
        self.ShowAutoDialogFlag    = False 
        self.RestoreWindowFlag     = False
        self.LoadFile              = StringVar()
        self.port                  = "None"
        
        self.TkenvironmentFlag     = BooleanVar()
        self.TkWindowFlag          = BooleanVar()
        self.TkDesktopFlag         = BooleanVar()
        self.TkMethodFlag          = BooleanVar()
        self.TkShowAutoDialogFlag  = BooleanVar()
        self.TkRestoreWindowFlag   = BooleanVar()
        self.TkPort                = StringVar()
        
        self.TkSaveOptionsEnvironmentFlag       = BooleanVar()
        self.TkSaveOptionsWindowsFlag           = BooleanVar()
        self.TkSaveOptionsDesktopFlag           = BooleanVar()
        
        self.SaveOptionsEnvironmentFlag       = False
        self.SaveOptionsWindowsFlag           = False
        self.SaveOptionsDesktopFlag           = False
        
        self.popUpWindow  = None
        self.SaveOptionspopUpWindow = None
        
        return
        
    def ShowFileBrowser(self):
        filetypes = (
                     ('All files', '*.txt'),
                     ('All files', '*.*')
                    )

        self.filename = fd.askopenfilename(
                     title='Open a file',
                     initialdir='/',
                     filetypes=filetypes)
        self.LoadFile.set(self.filename)
        
        return    
        
    def PreferenceOK(self):
        self.environmentFlag       = self.TkenvironmentFlag.get()   
        self.WindowFlag            = self.TkWindowFlag.get()        
        self.DesktopFlag           = self.TkDesktopFlag.get()       
        self.MethodFlag            = self.TkMethodFlag.get()        
        self.ShowAutoDialogFlag    = self.TkShowAutoDialogFlag.get()
        self.RestoreWindowFlag     = self.TkRestoreWindowFlag.get() 
        self.port                  = self.TkPort.get()
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def PreferenceCancel(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
        
    def popUpWindowXPressed(self):
        self.PreferenceCancel()
        return    
        
    def PreferenceHelp(self):
    
        return
    
    def PreferencesPopUp(self):
        if (self.popUpWindow == None):
           self.popUpWindow= Toplevel(self.parentWindow)
        else:
           return 
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                            
        self.popUpWindow.geometry("350x270")
        self.popUpWindow.resizable(False, False)
        self.popUpWindow.title("Preference")
        RowOneFrame = Frame(self.popUpWindow,borderwidth=1,relief=FLAT)
        autoSaveFrame = LabelFrame(RowOneFrame,text='Auto Save')
        
        autoSaveFrameRowOne = Frame(autoSaveFrame,borderwidth=1,relief=FLAT)
        
        Checkbutton(autoSaveFrameRowOne, variable=self.TkenvironmentFlag,text='Environment').pack(side=TOP,anchor=W)
        autoSaveFrameRowOne.pack(side=TOP)
        
        autoSaveFrameRowTwo = Frame(autoSaveFrame,borderwidth=1,relief=SOLID)
        Checkbutton(autoSaveFrameRowOne, variable=self.TkWindowFlag,text='Window').pack(side=TOP,anchor=W)
        autoSaveFrameRowTwo.pack(side=TOP)
        
        autoSaveFrameRowThree = Frame(autoSaveFrame,borderwidth=1,relief=SOLID)
        Checkbutton(autoSaveFrameRowOne, variable=self.TkDesktopFlag,text='Desktop').pack(side=TOP,anchor=W)
        autoSaveFrameRowThree.pack(side=TOP)
        
        autoSaveFrameRowFour = Frame(autoSaveFrame,borderwidth=1,relief=SOLID)
        Checkbutton(autoSaveFrameRowOne, variable=self.TkMethodFlag,text='Method').pack(side=TOP,anchor=W)
        autoSaveFrameRowFour.pack(side=TOP)
        autoSaveFrame.pack(side=LEFT,anchor=W,padx=10) 
        
        communicationsFrame = LabelFrame(RowOneFrame,text='Communications')
        Label(communicationsFrame, text='Port').pack(side=LEFT)
        portChoosen = ttk.Combobox(communicationsFrame, width = 10, 
                            textvariable = self.TkPort)
        portChoosen['values'] = ('COM1', 
                          'COM2',
                          'COM3',
                          'COM4',
                          'COM5')
        portChoosen.pack(side=TOP)                 
        portChoosen.current(1) 
        communicationsFrame.pack(side=LEFT,anchor=W)
        
        RowOneFrame.pack(side=TOP,anchor=W)
        
        RowTwoFrame = Frame(self.popUpWindow,borderwidth=1,relief=FLAT)
        AtStartupFrame = LabelFrame(RowTwoFrame,text='At StartUp')
        
        AtStartupFrameRowOne   = Frame(AtStartupFrame,borderwidth=1,relief=FLAT)
        Label(AtStartupFrameRowOne, text='Load File').pack(side=LEFT,anchor=W)
        entry= Entry(AtStartupFrameRowOne,relief=SUNKEN, textvariable=self.LoadFile, 
                     width= 20).pack(side=LEFT,anchor=E)
        Button(AtStartupFrameRowOne, text ="Browse", command = self.ShowFileBrowser).pack(side=RIGHT,ipadx=4)             
        AtStartupFrameRowOne.pack(side=TOP,anchor=W)
        
        AtStartupFrameRowTwo   = Frame(AtStartupFrame,borderwidth=1,relief=FLAT)
        Checkbutton(AtStartupFrameRowTwo, variable=self.TkShowAutoDialogFlag,text='Show Auto Dialog').pack(side=LEFT,anchor=W)
        AtStartupFrameRowTwo.pack(side=TOP,anchor=W)
        
        AtStartupFrameRowThree = Frame(AtStartupFrame,borderwidth=1,relief=FLAT)
        Checkbutton(AtStartupFrameRowThree, variable=self.TkRestoreWindowFlag,text='Restore Window').pack(side=LEFT,anchor=W)
        AtStartupFrameRowThree.pack(side=TOP,anchor=W)
        
        AtStartupFrame.pack(side=TOP)
        RowTwoFrame.pack(side=TOP)
        
        RowThreeFrame = Frame(self.popUpWindow,borderwidth=1,relief=FLAT)        
        Button(RowThreeFrame, text ="OK",     command = self.PreferenceOK).pack(side=LEFT,ipadx=4)             
        Button(RowThreeFrame, text ="Cancel", command = self.PreferenceCancel).pack(side=LEFT,ipadx=4)             
        Button(RowThreeFrame, text ="Help",   command = self.PreferenceHelp).pack(side=LEFT,ipadx=4)             
        RowThreeFrame.pack(side=TOP, pady=5)

        return
    def SaveOptionsOK(self):
        self.SaveOptionsEnvironmentFlag  = self.TkSaveOptionsEnvironmentFlag.get()
        self.SaveOptionsWindowsFlag      = self.TkSaveOptionsWindowsFlag.get()    
        self.SaveOptionsDesktopFlag      = self.TkSaveOptionsDesktopFlag.get()            
        self.SaveOptionspopUpWindow.destroy()
        self.SaveOptionspopUpWindow = None
        return
        
    def SaveOptionsCancel(self):
        self.SaveOptionspopUpWindow.destroy()
        self.SaveOptionspopUpWindow = None
        return
    def SaveOptionspopUpWindowXPressed(self):
        self.SaveOptionsCancel()
        return    
        
    def SaveOptionsHelp(self):
    
        return
        
    def PreferencesSaveOptionsPopUp(self):
        if (self.SaveOptionspopUpWindow == None):
            self.SaveOptionspopUpWindow= Toplevel(self.parentWindow)
        else:
            return
        self.SaveOptionspopUpWindow.attributes('-topmost',True)
        self.SaveOptionspopUpWindow.protocol("WM_DELETE_WINDOW", self.SaveOptionspopUpWindowXPressed)                    
        self.SaveOptionspopUpWindow.geometry("200x125")
        self.SaveOptionspopUpWindow.resizable(False, False)
        self.SaveOptionspopUpWindow.title("Save Option")
        #self.menubar.entryconfig("Test2", state="disabled")
        FirstFrame = LabelFrame(self.SaveOptionspopUpWindow,text='Save Options')
        Checkbutton(FirstFrame, variable=self.TkSaveOptionsEnvironmentFlag,text='Environment').pack(side=TOP,anchor=W)
        Checkbutton(FirstFrame, variable=self.TkSaveOptionsWindowsFlag,text='Windows').pack(side=TOP,anchor=W)
        Checkbutton(FirstFrame, variable=self.TkSaveOptionsDesktopFlag,text='Desktop').pack(side=TOP,anchor=W)
        FirstFrame.pack(side=LEFT,anchor=W)
        
        ButtonFrame = Frame(self.SaveOptionspopUpWindow,borderwidth=1,relief=FLAT)
        Button(ButtonFrame, text ="OK",     command = self.SaveOptionsOK,width=6).pack(side=TOP,ipadx=4)             
        Button(ButtonFrame, text ="Cancel", command = self.SaveOptionsCancel,width=6).pack(side=TOP,ipadx=4)             
        Button(ButtonFrame, text ="Help",   command = self.SaveOptionsHelp,width=6).pack(side=TOP,ipadx=4)             
        ButtonFrame.pack(side=LEFT)

        
    def SavePreferences(self):
         pref = {
              "Environment_Flag"    : self.environmentFlag,
              "Window_Flag"         : self.WindowFlag,
              "Desktop_Flag"        : self.DesktopFlag,
              "Method_Flag"         : self.MethodFlag,
              "ShowAutoDialog_Flag" : self.ShowAutoDialogFlag,
              "RestoreWindow_Flag"  : self.RestoreWindowFlag,
              "LoadFile"            : self.LoadFile.get(),
              "Port"                : self.port
             }
         #y = json.dumps(pref)
         out_file = open("preference.json", "w") 
    
         json.dump(pref, out_file, indent = 6) 
    
         out_file.close() 
         
         return