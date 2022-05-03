#! /usr/bin/python3
from tkinter import *
import json
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import ttk
import time
from tkinter import messagebox
import detectorpopup as DetectorClass
import methodedit as methodEditClass
import componentstable as ComponentsTable
import standardstable as StandardsTable
import pidpreferences as PIDPreferences
import runmenu as RunMenu
import pid_graph as PIDGraph
import filemenuoptions as FileMenuOptions
import viewmenuoptions as ViewMenuOptions
import helpClass       as HelpClass
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import sys
from sys import stdout
from daqhats import hat_list, HatIDs, mcc118
import threading
import os
import shutil

global x_gc,gc_values,x_gcB,gc_valuesB
x_gc = []
gc_values = []
x_gcB = []
gc_valuesB = []

board_list = hat_list(filter_by_id = HatIDs.ANY)
if board_list[0].id == HatIDs.MCC_118:
    board = mcc118(board_list[0].address)


global root 

 
global detectorAObject
global detectorBObject
global methodEditObject 
global componentsTableObject
global standardsTableObject
global PIDPreferencesObject
global RootWindowDetailsObject

fontString = 'Courier 10'
fontSize = 10


def stubedout():
    return
	
 
	
	
def DisplayHelp():
    # -------------------------------------------
    # Populate with the code to display help here
	# -------------------------------------------
    return
	
    
def MethodSavePopup():
    #global root
    #showinfo("Method Save", "Use SaveAs Option")
    return
	
def AboutCallBack():
    return
               
 

	
def CreateFileMenu(toplevel):
    FileMenu = Menubutton(toplevel, 
                          text='File', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    FileMenu.pack(side=LEFT, padx="2m")
    FileMenu.menu = Menu(FileMenu,tearoff=0)
    
    FileMenu.menu.add_command(label='New', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    FileMenu.menu.add_command(label='Open', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=FileOpenWrapper)
    FileMenu.menu.add_command(label='Save', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=FileSaveWrapper)
    FileMenu.menu.add_command(label='Save As', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=FileSaveAsWrapper)                              
    
    FileMenu.menu.add_separator()
    
    FileMenu.menu.add_command(label='Save Report', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=FileSaveReportWrapper)
    FileMenu.menu.add_command(label='Print Report', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=FilePrintReportWrapper)
    FileMenu.menu.add_separator()
    
    FileMenu.menu.add_command(label='Print Setup', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    FileMenu.menu.add_separator()
    FileMenu.menu.add_command(label='Page Setup', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    FileMenu.menu.add_separator()                          
    
    FileMenu.menu.add_command(label='Quit', 
                              underline=0, 
                              background='white', 
                              activebackground='green', 
                              command=FileMenu.quit)
                              
    FileMenu['menu'] = FileMenu.menu
	
    return FileMenu

def CreateEditMenu(toplevel):
    EditMenu = Menubutton(toplevel, 
                          text='Edit', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    EditMenu.pack(side=LEFT, padx="2m")
    EditMenu.menu = Menu(EditMenu,tearoff=0)
    
    EditMenu.menu.add_command(label='Copy', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    EditMenu.menu.add_command(label='Copy to File', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    EditMenu['menu'] = EditMenu.menu
    return EditMenu

    
def CreateViewMenu(toplevel):
    ViewMenu = Menubutton(toplevel, 
                          text='View', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    ViewMenu.pack(side=LEFT, padx="2m")
    ViewMenu.menu = Menu(ViewMenu,tearoff=0)
    
    ViewMenu.menu.add_command(label='Font', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    ViewMenu.menu.add_command(label='Axis', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=ViewMenuOptionsObject.AxisForGraphPopUp)
    ViewMenu.menu.add_command(label='Curve', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    ViewMenu.menu.add_command(label='Zoom+', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    ViewMenu.menu.add_command(label='Zoom-', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    ViewMenu.menu.add_command(label='Scale Peaks', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    ViewMenu.menu.add_command(label='No Scaling', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)


    ViewMenu['menu'] = ViewMenu.menu
    return ViewMenu


def CreateMethodMenu(toplevel):
    global detectorAObject
    global detectorBObject
    global methodEditObject 
   
    MethodMenu = Menubutton(toplevel, 
                          text='Method', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    MethodMenu.pack(side=LEFT, padx="2m")
    MethodMenu.menu = Menu(MethodMenu,tearoff=0)
    #--------------------------------------------
    MethodMenu.menu.add_command(label='Edit', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=methodEditObject.MethodEditEntry)
    MethodMenu.menu.add_separator()
    
    MethodMenu.menu.add_command(label='Detector A', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=detectorAObject.DetectorPopUp)
    MethodMenu.menu.add_command(label='Detector B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=detectorBObject.DetectorPopUp)
    MethodMenu.menu.add_separator()
    
    MethodMenu.menu.add_command(label='Components', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=componentsTableObject.TablePopUp)
    MethodMenu.menu.add_command(label='Standards', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=standardsTableObject.TablePopUp)
    MethodMenu.menu.add_separator()
    
    MethodMenu.menu.add_command(label='Save', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=MethodSavePopup)

 
    MethodMenu['menu'] = MethodMenu.menu
    return MethodMenu

# ------------------------------------- All Call back wrappers are defined below -------------------
# Some of the call back give rise to pop ups. These popups will not be seen when Graphs/Table are show
# So before calling any build in dialog where we do not have control over the TopLevel Attribute
# we use wrapped to push all graphs below and once the dialog is closed the graphs comes back
    
def SaveIntegrationResultsWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    RunMenuRunsObject.SaveIntegrationResults()
    PIDGraphObject.PushPlotsAndTableUp()
    return

def FileOpenWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.FileMenuOpen()
    PIDGraphObject.PushPlotsAndTableUp()
    return

def FileSaveAsWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.FileMenuSaveAs()
    PIDGraphObject.PushPlotsAndTableUp()
    return
    
def FileSaveReportWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.SaveReport()
    PIDGraphObject.PushPlotsAndTableUp()
    return
    
def FilePrintReportWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.PrintReportPopUp()
    PIDGraphObject.PushPlotsAndTableUp()
    return

    
def CreateRunMenu(toplevel):
    RunMenu = Menubutton(toplevel, 
                          text='Run', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    RunMenu.pack(side=LEFT, padx="2m")
    RunMenu.menu = Menu(RunMenu,tearoff=0)
  
    RunMenu.menu.add_command(label='Calibration Acquire', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=RunMenuCalibrationAcquireObject.TablePopUp)

    RunMenu.menu.add_command(label='Acquire Run', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    
   
    RunMenu.menu.add_command(label='Zero Gas Run', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Integrate Run', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Stop', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
                              
    RunMenu.menu.add_separator()
    
    RunMenu.menu.add_command(label='Save Integration Results', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=SaveIntegrationResultsWrapper)

    RunMenu.menu.add_command(label='Enable Oven', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    
   
    RunMenu.menu.add_command(label='Disable Oven', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Open Oven Door', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Close Oven Door', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    RunMenu.menu.add_separator()
    
    RunMenu.menu.add_command(label='Start Lamp A', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)

    RunMenu.menu.add_command(label='Stop Lamp A', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    
   
    RunMenu.menu.add_command(label='Start Lamp B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Stop Lamp B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    RunMenu.menu.add_separator()
    
    RunMenu.menu.add_command(label='Select Run', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=RunMenuRunsObject.SelectRunPopUp)
                              
    RunMenu.menu.add_command(label='Edit Run', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=RunMenuRunsObject.EditRunPopUp)

    RunMenu.menu.add_command(label='Save Calibration Results', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=RunMenuRunsObject.SaveCalibrationResults)
    
    RunMenu.menu.add_separator()
    
    RunMenu.menu.add_command(label='Run Modes', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=RunMenuRunModesObject.TablePopUp)
   
    RunMenu.menu.add_command(label='Shift Modes', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
   
    RunMenu.menu.add_command(label='Auto Zero', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    RunMenu.menu.add_command(label='Autozoft', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
                     
    
    
    RunMenu['menu'] = RunMenu.menu
    return RunMenu
    
def CreateOptionsMenu(toplevel):
    OptionsMenu = Menubutton(toplevel, 
                          text='Options', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    OptionsMenu.pack(side=LEFT, padx="2m")
    OptionsMenu.menu = Menu(OptionsMenu,tearoff=0)
    #===============================================
    OptionsMenu.menu.add_command(label='Preferences', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDPreferencesObject.PreferencesPopUp)
    OptionsMenu.menu.add_command(label='Save', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDPreferencesObject.PreferencesSaveOptionsPopUp)

    #===============================================
    OptionsMenu['menu'] = OptionsMenu.menu
    return OptionsMenu

def CreateWindowsMenu(toplevel):
    WindowsMenu = Menubutton(toplevel, 
                          text='Windows', 
                          font=(fontString, fontSize),
                          underline=0)
                          
    WindowsMenu.pack(side=LEFT, padx="2m")
    WindowsMenu.menu = Menu(WindowsMenu,tearoff=0)
    #===============================================
    WindowsMenu.menu.add_command(label='Cascade', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    WindowsMenu.menu.add_command(label='Tile Horizontal', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.TileHorizontal)
    WindowsMenu.menu.add_command(label='Tile Vertical', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    WindowsMenu.menu.add_command(label='Arrange All', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.ArrageAll)
    WindowsMenu.menu.add_command(label='Close All', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.CloseAll)
    WindowsMenu.menu.add_separator()

    WindowsMenu.menu.add_command(label='Graph A Detector A', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.PopUpGraphA)
    WindowsMenu.menu.add_command(label='Graph B Detector B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.PopUpGraphB)
    WindowsMenu.menu.add_command(label='Table A Detector A', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.CreateTableA)
    WindowsMenu.menu.add_command(label='Table B Detector B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject.CreateTableB)
    WindowsMenu.menu.add_command(label='Both Graph', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    WindowsMenu.menu.add_command(label='Run Graph', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    
    #===============================================    
    WindowsMenu['menu'] = WindowsMenu.menu
    return WindowsMenu
   
def CreateHelpMenu(toplevel):
    HelpMenu = Menubutton(toplevel, 
                          text='Help', 
                          font=(fontString, fontSize),
                          underline=0)
    
    HelpMenu.pack(side=LEFT, padx="2m")
    HelpMenu.menu = Menu(HelpMenu,tearoff=0)
    
    HelpMenu.menu.add_command(label='Contents F1', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=DisplayHelp)

    HelpMenu.menu.add_command(label='Using Help', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=stubedout)
    HelpMenu.menu.add_separator()
    
    HelpMenu.menu.add_command(label='About', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=HelpMenuObject.AboutCallBack)

    
    HelpMenu['menu'] = HelpMenu.menu
    return HelpMenu

def callback():
    return
	
global startAcquire,StopAcquire
startAcquire = False
StopAcquire = True

global value_AA,start_time
value_AA = 1
start_time = time.time()
def myReadValues():
    global value_AA,start_time
    if value_AA == 1:
        start_time = time.time()
        value_AA = 2

    g_var = board.a_in_read(0)
    #print(g_var)
    g_var1 = round(g_var,4)
    gc_values.append(g_var1)
    #print(gc_values)
    actual_time = time.time()- start_time
    actual_time = round(actual_time,4)
    x_gc.append(actual_time)
    return x_gc,gc_values

def ReadValuesChannelA():
    global gc_values,startAcquire,start_time
    #print(gc_values)
    start_time = time.time()
    while startAcquire:
        #g_var = board.a_in_read(0)
        #print(g_var)
        #gc_values.append(g_var)
        #print(gc_values)
        myReadValues()
    #print("Thread channel A exit")
    #sys.exit()
    return
"""
def start_timeB():
    global start_timeB
    start_timeB = time.time()
    return start_timeB
#start_timeB = time.time()
"""
global value_BB,start_timeB
value_BB = 1
start_timeB = time.time()
def myReadValuesB():
    # #start_timeB()
    global value_BB,start_timeB
    if value_BB == 1:
        start_timeB = time.time()
        value_BB = 2
    g_varB = board.a_in_read(1)
    #print(g_var)
    g_varB1 = round(g_varB,4)
    gc_valuesB.append(g_varB1)
    #print(gc_values)
    actual_timeB = time.time()- start_timeB
    actual_timeB = round(actual_timeB,4)
    x_gcB.append(actual_timeB)
    return x_gcB,gc_valuesB

def ReadValuesChannelB():
    global gc_valuesB,startAcquire,start_timeB
    #print(gc_values)
    start_timeB = time.time() #start_timeB()
    while startAcquire:
        #g_var = board.a_in_read(0)
        #print(g_var)
        #gc_values.append(g_var)
        #print(gc_values)
        myReadValuesB()
    #print("Thread channel B exit")
    #sys.exit()
    return

global yA_values_forSavefile,yB_values_forSavefile,A_Flag,B_Flag,xA_values_forSavefile,xB_values_forSavefile
yA_values_forSavefile = []
yB_values_forSavefile = []
xA_values_forSavefile = []
xB_values_forSavefile = []
B_Flag = 0
A_Flag = 0
"""
class MyThread(threading.Thread):
 
    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.
 
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
 
    # function using _stop function
    def stop(self):
        self._stop.set()
 
    def stopped(self):
        return self._stop.isSet()
 
    def run(self):
        while True:
            if self.stopped():
                return
            print("Hello, world!")
            time.sleep(1)
"""
global acquire_value
acquire_value = 1
def AcquireIconCallback():
    #print(detectorAObject.myOnOff())
    global A_Flag,B_Flag,startAcquire,yA_values_forSavefile,yB_values_forSavefile,acquire_value,xA_values_forSavefile,xB_values_forSavefile
    yA_values_forSavefile = []
    yB_values_forSavefile = []
    startAcquire = True
    if acquire_value == 1:
        acquire_value = 2
        if detectorAObject.myOnOff():
            try:
                values_thread_A = threading.Thread(target = ReadValuesChannelA)
                values_thread_A.start()
                #values_thread_A.join()
                PIDGraphObject.PopUpGraphA()
                A_Flag = 1
                #acquire_value = 2
                xA_values_forSavefile.append(myReadValues()[0])
                yA_values_forSavefile.append(myReadValues()[1])
                #values_thread_A.join()
                #print(detectorBObject.myOnOff())
            except RuntimeError:
                pass
        if detectorBObject.myOnOff():
            values_thread_B = threading.Thread(target = ReadValuesChannelB)
            values_thread_B.start()
            #values_thread_B.join()
            PIDGraphObject.PopUpGraphB()
            B_Flag = 1
            #acquire_value = 2
            xB_values_forSavefile.append(myReadValuesB()[0])
            yB_values_forSavefile.append(myReadValuesB()[1])
            #values_thread_B.join()
    else:
        pass
    return
"""
def AcquireIconCallback():
    #print(detectorAObject.myOnOff())
    global A_Flag,B_Flag,startAcquire,values_thread_A
    startAcquire = True
    if detectorAObject.myOnOff():
        values_thread_A = threading.Thread(target = ReadValuesChannelA)
        #values_thread_A.deamon = True
        values_thread_A.start()
        #values_thread_A.join()
        PIDGraphObject.PopUpGraphA()
        A_Flag = 1
        #x_values_forSavefile.append(myReadValues()[0])
        yA_values_forSavefile.append(myReadValues()[1])
        #values_thread_A.join()
    #print(detectorBObject.myOnOff())
    if detectorBObject.myOnOff():
        values_thread_B = threading.Thread(target = ReadValuesChannelB)
        values_thread_B.start()
        #values_thread_B.join()
        PIDGraphObject.PopUpGraphB()
        B_Flag = 1
        yB_values_forSavefile.append(myReadValuesB()[1])
        #values_thread_B.join()
"""
def log_function(myO_stringA,myO_stringB):
    
    #my_file = FileMenuOptionsObject.filename
    #my_file1 = FileMenuOptionsObject.filename
    #base = os.path.splitext(my_file1)[0]
    #os.rename(my_file1, base+'.json') 
    #print(my_file1)
    #print(json.dumps(my_file))
    #print(my_file)
    #with open(myfile,'w') as f: my_file = 'my_file.txt'
    #base = os.path.splitext(my_file)[0]
    #os.rename(my_file, base + '.bin')
        #print(json.dumps(f)) import os
    
    #my_string = my_file.name
    #my_string_values = '/home/acufore/Eshwar/Threads/pid_with_threads/logValues_files'
    #shutil.copytree(my_string,my_string_values)
    #base = os.path.splitext(my_string_values)[0]
    #base = base + '.csv'
    #print(base)
    log_stringA = myO_stringA
    log_stringB = myO_stringB

    if A_Flag == 1 and B_Flag == 1:
        #string_values = my_file1.readline()
        #print(string_values)
        #my_file = FileMenuOptionsObject.filename
        #my_file.write(string_values)
        with open(log_stringA,'a') as my_fileA:
            for itemA,itemAA in zip(xA_values_forSavefile,yA_values_forSavefile):
                my_fileA.write("Time A,Detector A,")
                my_fileA.write("\n")
                for i,j in zip(itemA,itemAA):
                    #print(i)
                    i = str(i)
                    my_fileA.write(i)
                    my_fileA.write(",")
                    j = str(j)
                    my_fileA.write(j)
                    my_fileA.write(",")
                    my_fileA.write("\n")
                    
        with open(log_stringB,'a') as my_fileB:
            for itemB,itemBB in zip(xB_values_forSavefile,yB_values_forSavefile):
                my_fileB.write("Time B,Detector B,")
                my_fileB.write("\n")
                for i,j in zip(itemB,itemBB):
                    #print(i)
                    i = str(i)
                    my_fileB.write(i)
                    my_fileB.write(",")
                    j = str(j)
                    my_fileB.write(j)
                    my_fileB.write(",")
                    my_fileB.write("\n")
           
            """
            for itemA,itemAA,itemB,itemBB in zip(xA_values_forSavefile,yA_values_forSavefile,xB_values_forSavefile,yB_values_forSavefile):
                my_file.write("Time A,Detector A,Time B,Detector B,")
                my_file.write("\n")
                for i,j,k,l in zip(itemA,itemAA,itemB,itemBB):
                    #print(i)
                    i = str(i)
                    my_file.write(i)
                    my_file.write(",")
                    j = str(j)
                    my_file.write(j)
                    my_file.write(",")
                    k = str(k)
                    my_file.write(k)
                    my_file.write(",")
                    l = str(l)
                    my_file.write(l)
                    my_file.write(",")
                    my_file.write("\n")
            """
    elif A_Flag == 1 and B_Flag == 0 :
        
        with open(log_stringA,'a') as my_fileA:
            for itemA,itemAA in zip(xA_values_forSavefile,yA_values_forSavefile):
                my_fileA.write("Time A,Detector A,")
                my_fileA.write("\n")
                for i,j in zip(itemA,itemAA):
                    #print(i)
                    i = str(i)
                    my_fileA.write(i)
                    my_fileA.write(",")
                    j = str(j)
                    my_fileA.write(j)
                    my_fileA.write(",")
                    my_fileA.write("\n")
        """
        for item,itemA in zip(xA_values_forSavefile,yA_values_forSavefile):
            my_file.write("Time A,Detector A,")
            my_file.write("\n")
            for i,j in zip(item,itemA):
                #print(i)
                i = str(i)
                my_file.write(i)
                my_file.write(",")
                j = str(j)
                my_file.write(j)
                my_file.write(",")
                my_file.write("\n")
        """     
    elif A_Flag == 0 and B_Flag == 1 :
        
        with open(log_stringB,'a') as my_fileB:
            for itemB,itemBB in zip(xB_values_forSavefile,yB_values_forSavefile):
                my_fileB.write("Time B,Detector B,")
                my_fileB.write("\n")
                for i,j in zip(itemB,itemBB):
                    #print(i)
                    i = str(i)
                    my_fileB.write(i)
                    my_fileB.write(",")
                    j = str(j)
                    my_fileB.write(j)
                    my_fileB.write(",")
                    my_fileB.write("\n")
        """
        for item,itemB in zip(xB_values_forSavefile,yB_values_forSavefile):
            my_file.write("Time B,Detector B,")
            my_file.write("\n")
            for i,j in zip(item,itemB):
                #print(i)
                i = str(i)
                my_file.write(i)
                my_file.write(",")
                j = str(j)
                my_file.write(j)
                my_file.write(",")
                my_file.write("\n")
        """
    else:
        pass
    """
    if B_Flag == 1:
        for itemB in yB_values_forSavefile:
            my_file.write("")
            my_file.write("\n")
            for i in itemB:
                #print(i)
                i = str(i)
                my_file.write(i)
                my_file.write(",")
                my_file.write("\n")
    else:
        pass
    """
def log_function_json():
    
    global my_stringA,my_stringB
    my_file1 = FileMenuOptionsObject.filename
    my_string1 = my_file1.name
    
    if A_Flag == 1 and B_Flag == 1:
        
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {'Detector A':'ON','Detector B':'ON',"Detector-A-Data": my_stringA,"Detector-B-Data": my_stringB}
        xAB_json = json.dumps(x_AB,indent = 2)
        my_file1.write(xAB_json)
        return my_stringA,my_stringB
    
    elif A_Flag == 1 and B_Flag == 0:
        
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {'Detector A':'ON','Detector B':'OFF',"Detector-A-Data": my_stringA,"Detector-B-Data": my_stringB}
        xAB_json = json.dumps(x_AB,indent = 2)
        my_file1.write(xAB_json)
        return my_stringA,my_stringB
    
    elif A_Flag == 0 and B_Flag == 1:
        
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {'Detector A':'OFF','Detector B':'ON',"Detector-A-Data": my_stringA,"Detector-B-Data": my_stringB}
        xAB_json = json.dumps(x_AB,indent = 2)
        my_file1.write(xAB_json)
        return my_stringA,my_stringB
    else:
        return my_stringA,my_stringB
    
def FileSaveWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.FileMenuSave()
    myO_stringA,myO_stringB = log_function_json()
    log_function(myO_stringA,myO_stringB)
    PIDGraphObject.PushPlotsAndTableUp()
    return

def Stopcallback():
    global startAcquire,StopAcquire
    startAcquire = False
    #StopAcquire = False
    PIDGraphObject.stop_threading_A()
    PIDGraphObject.stop_threading_B()
    #AcquireIconCallback()
    #stdout.flush()
    #sys.exit()
    #print("startAcquire to false")
    #PIDGraphObject.PopUpGraphB()
    #PIDGraphObject.onClosingA()
    #PIDGraphObject.onClosingB()

def CreateStatusBar(top):
  
        statusBar = ttk.Label(root, text="Oven=829C ,    Det 823C A:10, B:10, Flow: 0.0", relief=GROOVE, anchor=W)
        statusBar.pack(side=BOTTOM, fill=X)
        
#global cons_filename
def Loadcallback_plot():
    global cons_filename
    cons_filename = askopenfilename()
    #print(cons_filename)
    #return cons_filename
    PIDGraphObject.PopUpGraphA_Cons(cons_filename)
   
    #PIDGraphObject.PopUpGraphA_Cons()
    PIDGraphObject.PopUpGraphB_Cons(cons_filename)
    
def CreateIcons():
    global newIcon
    global loadIcon
    global saveIcon
    global printerIcon
    global exitIcon
    global acquireIcon
    global scaleNoIcon
    global stopIcon
    global runIcon
    global lampOnIcon
    global lampOffIcon
    global doorOpenIcon
    global closeIcon
    global az_bIcon
    
    IconLevelMenuBar = Frame(root, relief=FLAT, borderwidth=2)
   
    newIcon=PhotoImage(file=r'NEW.png')
    newIcon  = newIcon.subsample(1,1)
    Button(IconLevelMenuBar,image=newIcon,command = callback).pack(side=LEFT)
    
  
    loadIcon=PhotoImage(file=r'LOAD.png')
    loadIcon=loadIcon.subsample(1,1)   
    Button(IconLevelMenuBar,image = loadIcon,command = Loadcallback_plot).pack(side=LEFT)

    saveIcon=PhotoImage(file=r'SAVE.png')
    saveIcon  = saveIcon.subsample(1,1)
    Button(IconLevelMenuBar,image = saveIcon,command = callback).pack(side=LEFT)

    printerIcon=PhotoImage(file=r'PRINT.png')
    printerIcon  = printerIcon.subsample(1,1)
    Button(IconLevelMenuBar,image = printerIcon,command = callback).pack(side=LEFT)

    exitIcon=PhotoImage(file=r'EXIT.png')
    exitIcon  = exitIcon.subsample(1,1)
    Button(IconLevelMenuBar,image = exitIcon,command = callback).pack(side=LEFT)


    acquireIcon = PhotoImage(file=r'ACQUIRE.png')
    acquireIcon  = acquireIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = acquireIcon,command = AcquireIconCallback).pack(side=LEFT)

    
    scaleNoIcon=PhotoImage(file=r'SCALE_NO.png')
    scaleNoIcon  = scaleNoIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = scaleNoIcon,command = callback).pack(side=LEFT)

    stopIcon =PhotoImage(file=r'STOP.png')
    stopIcon = stopIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = stopIcon,command = Stopcallback).pack(side=LEFT)

    runIcon = PhotoImage(file=r'RUN.png')
    runIcon  = runIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = runIcon,command = callback).pack(side=LEFT)
	
    lampOnIcon=PhotoImage(file=r'LAMP_ON.png')
    lampOnIcon  = lampOnIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = lampOnIcon,command = callback).pack(side=LEFT)
	
    lampOffIcon=PhotoImage(file=r'LAMP_OFF.png')
    lampOffIcon = lampOffIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = lampOffIcon,command = callback).pack(side=LEFT)

    doorOpenIcon = PhotoImage(file=r'D_OPEN.png')
    doorOpenIcon = doorOpenIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = doorOpenIcon,command = callback).pack(side=LEFT)
	
    closeIcon=PhotoImage(file=r'D_CLOSE.png')
    closeIcon = closeIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = closeIcon,command = callback).pack(side=LEFT)
   
    az_bIcon=PhotoImage(file=r'AZ_B.png')
    az_bIcon= az_bIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = az_bIcon,command = callback).pack(side=LEFT)
    
    IconLevelMenuBar.pack(fill=X,side=TOP)
		
def CreateSplashScreen(parent):
    global SplashFrame
    global photoImageObj
    global splashLabel
    
    photoImageObj = PhotoImage(file="pid_analyzer.png")
    SplashFrame = Frame(root, relief=FLAT, borderwidth=2)
    EmptyFrame = Frame(root, relief=GROOVE, borderwidth=2)
    splashLabel = Label(SplashFrame,image=photoImageObj).pack()
    EmptyFrame.pack(side=TOP)
    SplashFrame.place(relx = 0.5, rely = 0.5, anchor = 'center')
    return		
    
def CreateTopLevelMenuBar():

    TopLevelMenuBar = Frame(root, relief=RAISED, borderwidth=2)
    TopLevelMenuBar.pack(fill=X,side=TOP)
    	
    FileMenu    = CreateFileMenu(TopLevelMenuBar)
    EditMenu    = CreateEditMenu(TopLevelMenuBar)
    ViewMenu    = CreateViewMenu(TopLevelMenuBar)
    MethodMenu  = CreateMethodMenu(TopLevelMenuBar)
    RunMenu     = CreateRunMenu(TopLevelMenuBar)
    OptionsMenu = CreateOptionsMenu(TopLevelMenuBar)
    WindowsMenu = CreateWindowsMenu(TopLevelMenuBar)
    HelpMenu    = CreateHelpMenu(TopLevelMenuBar)
    CreateIcons()
    CreateStatusBar(root)
    CreateSplashScreen(root)
    #TopLevelMenuBar.tk(FileMenu, EditMenu)
    return
    
    
def GetMousePointsOfRoots(event):
    #print("Root Window Mouse=", "x=", event.x, "y=",event.y)
    if (SplashFrame != None):
        SplashFrame.destroy()
    return



def main():
  global root
  global detectorAObject
  global detectorBObject
  global methodEditObject 
  global componentsTableObject
  global standardsTableObject
  global PIDPreferencesObject 
  global RunMenuCalibrationAcquireObject
  global RunMenuRunModesObject
  global RunMenuRunsObject
  global PIDGraphObject
  global FileMenuOptionsObject
  global ViewMenuOptionsObject
  global HelpMenuObject
 
  root = Tk()
  root.geometry("1200x600") 
  root.title('PID Analyzer')

  root.geometry(("+{0}+{1}".format(10,10)))

  
  detectorAObject                 = DetectorClass.Detector("A",root)
  detectorBObject                 = DetectorClass.Detector("B",root)
  methodEditObject                = methodEditClass.MethodEdit(root)
  componentsTableObject           = ComponentsTable.ComponentsTable(root)
  standardsTableObject            = StandardsTable.StandardsTable(root)
  PIDPreferencesObject            = PIDPreferences.PIDPreferences(root)
  RunMenuCalibrationAcquireObject = RunMenu.CalibrationAcquire(root)
  RunMenuRunModesObject           = RunMenu.RunModes(root)
  PIDGraphObject                  = PIDGraph.PlotGraphClass(root)
  FileMenuOptionsObject           = FileMenuOptions.FileMenuOptions(root)
  ViewMenuOptionsObject           = ViewMenuOptions.ViewMenuOptions(root)
  HelpMenuObject                  = HelpClass.HelpClass(root)
  
  # This following Object is for Select Run, Edit Run and Save Calibration Results
  RunMenuRunsObject = RunMenu.Runs(root)

  CreateTopLevelMenuBar()
  root.bind("<Button 1>",GetMousePointsOfRoots)
  root.bind('<Configure>',PIDGraphObject.UpdateTopLeftCoordsOfRootWindow)
  root.geometry(("+{0}+{1}".format(100,100)))
  root.resizable(False, False)
  root.mainloop()

if __name__ == '__main__':
  main()
