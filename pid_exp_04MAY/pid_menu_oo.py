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
from daqhats import hat_list, HatIDs, mcc118
import threading
import os
import csv
from threading import Lock
from scipy.integrate import simps
import numpy as np
import pandas as pd


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
                              command=new_fun)
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

def new_fun():
    global acquireButton,stopButton,read_values
    global A_Flag,B_Flag
    #,x_gc,gc_values,x_gcB,gc_valuesB,start_time
    #start_time = time.time()
    PIDGraphObject.CloseAll()
    acquireButton["state"] = ACTIVE
    stopButton["state"] = DISABLED
    #print(detectorAObject.detectorOnOffFlag)
    #print(detectorAObject.OnOffFlag)
    A_Flag = 0
    B_Flag = 0
    detectorAObject.OnOffFlag.set(False)
    detectorBObject.OnOffFlag.set(False)
    read_values = True
    #print(detectorAObject.myOnOff())
    #print(detectorBObject.OnOffFlag())
    return

def FileOpenWrapper():
   # def FileOpenWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.FileMenuOpen()
    PIDGraphObject.PushPlotsAndTableUp()
    Jobfilename = FileMenuOptionsObject.LoadFile.get()
    #print(Jobfilename)
    acquireButton["state"] = DISABLED
    f = open(Jobfilename)
    data = json.load(f)
    if data['Detector A'] == "ON" :
        detectorAObject.OnOffFlag.set(True)
    else:
        detectorAObject.OnOffFlag.set(False)
        
    if data['Detector B'] == "ON" :
        detectorBObject.OnOffFlag.set(True)
    else:
        detectorBObject.OnOffFlag.set(False)
    if detectorAObject.OnOffFlag.get():
        PIDGraphObject.aX_Save_values = []
        PIDGraphObject.aY_Save_values = []
        with open(data['Detector-A-Data'],'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                row_A0 = float(row[0])
                row_A1 = float(row[1])
                #PIDGraphObject.aX_values.append(row[0])
                #PIDGraphObject.aY_values.append(row[1])
                PIDGraphObject.aX_Save_values.append(row_A0)
                PIDGraphObject.aY_Save_values.append(row_A1)
                #print(PIDGraphObject.aX_values)
        PIDGraphObject.PopUpGraphA_Cons()
        curve_calculationA()
    else:
        pass
    if detectorBObject.OnOffFlag.get():
        PIDGraphObject.bX_Save_values = []
        PIDGraphObject.bY_Save_values = []
        with open(data['Detector-B-Data'],'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                row_B0 = float(row[0])
                row_B1 = float(row[1])
                #PIDGraphObject.bX_values.append(row[0])
                #PIDGraphObject.bY_values.append(row[1])
                PIDGraphObject.bX_Save_values.append(row_B0)
                PIDGraphObject.bY_Save_values.append(row_B1)
                #oneB_peak = PIDGraphObject.bY_Save_values
        PIDGraphObject.PopUpGraphB_Cons()
    else:
        pass
    return

def FindCompoundName(retention_time):
    #print(retention_time)
    rows = []
    fields = []
    #retention_time_str = str(retention_time)
    with open("ComponentA.csv", 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        #print("Total no. of rows: %d"%(csvreader.line_num))
    for row in rows:
        row_int = float(row[2])
        if row_int-1.5 < retention_time < row_int+1.5:
            return row[0]
    return "Unknown"

def compoundPercentage():
    return

def curve_calculationA():
    curve_ListA = []
    data_ListA = []
    data_List_aY = []
    data_List_aX = []
    curveList_aY = PIDGraphObject.aY_Save_values
    curveList_aX = PIDGraphObject.aX_Save_values
    for curveValue_aX,curveValue_aY in zip(curveList_aX,curveList_aY):
        if curveValue_aY != 0:
            data_ListA.append((curveValue_aX,curveValue_aY))
            data_List_aX.append(curveValue_aX)
            data_List_aY.append(curveValue_aY)
        elif not data_ListA == []:
            #print(data_List)
            max_data = data_List_aY[0]
            for i,j in zip(data_List_aX,data_List_aY):
                if j>max_data:
                    max_data = j
                    peak_rt = round(i,2)
            peak_heightA = max_data - 0.1
            peak_areaA = simps(data_List_aY,dx=0.2)
            compound_name = FindCompoundName(peak_rt)
            #print(compound_name)
            compoundPercentage()            
            curve_ListA.append(dict(dataList = data_ListA,peak_height = peak_heightA,peak_area = peak_areaA,peak_RT=peak_rt,CompoundName =compound_name))
            data_ListA = []
            data_List_aY = []
            data_List_aX = []
        else:
            pass

    for curve in curve_ListA:
        print("Curve Data: ",curve["dataList"])
        print("Curve Peak Height: ",curve["peak_height"])
        print("Curve Peak Area: ",curve["peak_area"])
        print("Curve Peak Retension Time: ",curve["peak_RT"])
        print("Curve Compound Name:",curve["CompoundName"])
        print()
 
    '''
    for i,j in zip(peak_aX,peak_aY):
        while j!=0:
            xy_list = []
            xy_list.append(i)
            xy_list.append(j)
            peak_list.append(xy_list)
            #print("1 - Not equal to zero",i,"time",j,"value")
            break
            #print("1 - Not equal to zero",i,"time",j,"value")
        else:
            print("Equal to zero",i,"time",j,"value")
    print(peak_list)
    '''
    #areaA = simps(oneA_y, dx=0.2)
    #print("area A =", areaA)
    """
    for i in oneB_peak:
        if i>0:
            oneB_y.append(i)
    areaB = simps(oneB_y, dx=0.2)
    print("area B =",areaB)
    for i in oneA_peak:
    if i!=0:
        while i==0:
            oneA_y.append(i)
    """

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
                              command=PIDGraphObject)
    WindowsMenu.menu.add_command(label='Graph B Detector B', 
                              underline=0, 
                              font=(fontString, fontSize),
                              command=PIDGraphObject)
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
    global value_AA,start_time,gc_values,read_values
    #gc_valuesB = []
    #board1 = board.a_in_scan_start(1)
    g_var1, actual_time = 0, 0
    if value_AA == 1:
        start_time = time.time()
        value_AA = 2
    if read_values:        
        g_var = board.a_in_read(2)
        g_var1 = round(g_var,6)
        if g_var1 < 0.1:
            g_var1 = 0
    gc_values.append(g_var1)
    actual_time = time.time()-start_time
    actual_time = round(actual_time,6)
    x_gc.append(actual_time)
    if PIDGraphObject.plotValuesFlagA == 0:
        PIDGraphObject.plotValuesFlagA = -1
        PIDGraphObject.aX_plot_values.append(actual_time)
        PIDGraphObject.aY_plot_values.append(g_var1)
        PIDGraphObject.plotValuesFlagA = 0
    return x_gc,gc_values

def ReadValuesChannelA():
    global startAcquire,start_time,value_AA
    start_time = time.time()
    while startAcquire:
        myReadValues()
        time.sleep(0.2)
    PIDGraphObject.aX_plot_values = []
    PIDGraphObject.aY_plot_values = []
    return
"""
global value_AA,start_time
value_AA = 1
start_time = time.time()
def plotValuesA(obj, lock, operation, arg_x=0,arg_y=0):
    #global lock
        #obj.plotLock.acquire()
    print("Lock inside plotValuesA :",lock)
    with lock:
        if operation == 'update':
            obj.aX_plot_values.append(arg_x)
            obj.aY_plot_values.append(arg_y)
        elif operation == 'plot' :
            return (obj.aX_plot_values,obj.aY_plot_values)
        #obj.plotLock.release()

def ReadValuesChannelA(lock):
    global startAcquire,start_time,value_AA
    start_time = time.time()
    while startAcquire:
        g_var = board.a_in_read(2)
        g_var1 = round(g_var,6)
        actual_time = time.time()-start_time
        actual_time = round(actual_time,6)
        with lock:
            PIDGraphObject.aX_plot_values.append(actual_time)
            PIDGraphObject.aY_plot_values.append(g_var1)
            #lock.release()
        #plotValuesA( obj = PIDGraphObject, lock = PIDGraphObject.plotLock, operation='update', arg_x = actual_time, arg_y = g_var1 )
    PIDGraphObject.aX_plot_values = []
    PIDGraphObject.aY_plot_values = []
    return
"""
global value_BB,start_timeB,read_values
value_BB = 1
read_values = True
start_timeB = time.time()
def myReadValuesB():
    global value_BB,start_timeB,gc_valuesB,read_values
    g_varB1, actual_timeB = 0, 0
    if value_BB == 1:
        start_timeB = time.time()
        value_BB = 2
    if read_values:        
        g_varB = board.a_in_read(3)
        g_varB1 = round(g_varB,6)
        if g_varB1 < 0.1:
            g_varB1 = 0
    gc_valuesB.append(g_varB1)
    actual_timeB = time.time()-start_timeB
    actual_timeB = round(actual_timeB,6)
    x_gcB.append(actual_timeB)
    if PIDGraphObject.plotValuesFlagB == 0:
        PIDGraphObject.plotValuesFlagB = -1
        PIDGraphObject.bX_plot_values.append(actual_timeB)
        PIDGraphObject.bY_plot_values.append(g_varB1)
        PIDGraphObject.plotValuesFlagB = 0
    return x_gcB,gc_valuesB

def ReadValuesChannelB():
    global gc_valuesB,startAcquire,start_timeB,x_gcB,value_BB
    start_timeB = time.time()
    while startAcquire:
        myReadValuesB()
        time.sleep(0.2)
    #value_BB = 1
    PIDGraphObject.bX_plot_values = []
    PIDGraphObject.bY_plot_values = []
    return


global yA_values_forSavefile,yB_values_forSavefile,A_Flag,B_Flag,xA_values_forSavefile,xB_values_forSavefile
yA_values_forSavefile = []
yB_values_forSavefile = []
xA_values_forSavefile = []
xB_values_forSavefile = []
B_Flag = 0
A_Flag = 0

global acquire_value,acquireButton #,acquireIcon_state
acquire_value = 1
#acquireIcon_state = ACTIVE

def AcquireIconCallback():
    #print(detectorAObject.myOnOff())
    global values_thread_A,values_thread_B, lock
    global A_Flag,B_Flag,startAcquire,yA_values_forSavefile,yB_values_forSavefile,acquire_value,xA_values_forSavefile,xB_values_forSavefile,acquireIcon_state,acquireButton
    xA_values_forSavefile = []
    yA_values_forSavefile = []
    xB_values_forSavefile = []
    yB_values_forSavefile = []
    #acquireIcon_state = DISABLED
    startAcquire = True
    #Button(IconLevelMenuBar,image = acquireIcon,command = AcquireIconCallback,state=acquireIcon_state).pack(side=LEFT)
    
    if detectorAObject.OnOffFlag.get():
        try:
            acquireButton["state"] = DISABLED
            stopButton["state"] = ACTIVE
            values_thread_A = threading.Thread(target = ReadValuesChannelA)
            values_thread_A.start()
            #values_thread_A.join()
            PIDGraphObject.PopUpGraphA()
            A_Flag = 1
            xA_values_forSavefile.append(myReadValues()[0])
            yA_values_forSavefile.append(myReadValues()[1])

        except RuntimeError:
            pass
    
    if detectorBObject.OnOffFlag.get():
        try:
            acquireButton["state"] = DISABLED
            stopButton["state"] = ACTIVE
            values_thread_B = threading.Thread(target = ReadValuesChannelB)
            values_thread_B.start()
            #values_thread_B.join()
            PIDGraphObject.PopUpGraphB()
            B_Flag = 1
            xB_values_forSavefile.append(myReadValuesB()[0])
            yB_values_forSavefile.append(myReadValuesB()[1])

        except RuntimeError:
            pass
    else:
        pass
    
    return

def log_function(myO_stringA,myO_stringB):
    log_stringA = myO_stringA
    log_stringB = myO_stringB

    if A_Flag == 1 and B_Flag == 1:
        
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
    else:
        pass

def log_function_json():
    
    global my_stringA,my_stringB,my_string1
    my_file1 = FileMenuOptionsObject.filename
    my_string1 = my_file1.name
    
    if A_Flag == 1 and B_Flag == 1:
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {
                'Detector A':"ON",'Detector B':"ON",
                "Detector-A-Data": my_stringA,"Detector-B-Data": my_stringB,
                "Detector-A-Label":detectorAObject.detectorLabelStr,"Detector-B-Label":detectorBObject.detectorLabelStr,
                "Detector-A-Log":detectorAObject.detectorLogFlag,"Detector-B-Log":detectorBObject.detectorLogFlag,
                "Detector-A-External":detectorAObject.detectorExternalFlag,"Detector-B-External":detectorBObject.detectorExternalFlag,
                "Detector-A-Invert":detectorAObject.detectorInvertFlag,"Detector-B-Invert":detectorBObject.detectorInvertFlag,
                "Detector-A-Time":detectorAObject.detectorTimeStr,"Detector-B-Time":detectorBObject.detectorTimeStr,
                "Detector-A-Length":detectorAObject.detectorLengthStr,"Detector-B-Length":detectorBObject.detectorLengthStr,
                "Detector-A-Min Area":detectorAObject.detectorMinArea,"Detector-B-Min Area":detectorBObject.detectorMinArea,
                "Detector-A-Min Height":detectorAObject.detectorMinHeight,"Detector-B-Min Height":detectorBObject.detectorMinHeight,
                "Detector-A-Segment Width":detectorAObject.detectorSegmentWidth,"Detector-B-Segment Width":detectorBObject.detectorSegmentWidth,
                "Detector-A-Detector Units":detectorAObject.detectorUnits,"Detector-B-Detector Units":detectorBObject.detectorUnits,
                "Detector-A-Peak Algorithm":detectorAObject.detectorPeaksAlgorithm,"Detector-B-Peak Algorithm":detectorBObject.detectorPeaksAlgorithm,
                "Detector-A-Detect Method":detectorAObject.detectorDetectMethod,"Detector-B-Detect Method":detectorBObject.detectorDetectMethod, 
                "Detector-A-Data To Excel":detectorAObject.detectorDataToExcelFlag,"Detector-B-Data To Excel":detectorBObject.detectorDataToExcelFlag,    
                "Detector-A-Lamp Save":detectorAObject.detectorLampSaveFlag,"Detector-B-Lamp Save":detectorBObject.detectorLampSaveFlag,    
                "Detector-A-Auto":detectorAObject.detectorAutoFlag,"Detector-B-Auto":detectorBObject.detectorAutoFlag,
                "Detector-A-Range Selection":detectorAObject.detectorRangeSelection,"Detector-B-Range Selection":detectorBObject.detectorRangeSelection,
                }
        xAB_json = json.dumps(x_AB,indent = 2)
        my_file1.write(xAB_json)
        return my_stringA,my_stringB
        
    elif A_Flag == 1 and B_Flag == 0:
        
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {
                'Detector A':"ON",'Detector B':"OFF",
                "Detector-A-Data": my_stringA,
                "Detector-A-Label":detectorAObject.detectorLabelStr,
                "Detector-A-Log":detectorAObject.detectorLogFlag,
                "Detector-A-External":detectorAObject.detectorExternalFlag,
                "Detector-A-Invert":detectorAObject.detectorInvertFlag,
                "Detector-A-Time":detectorAObject.detectorTimeStr,
                "Detector-A-Length":detectorAObject.detectorLengthStr,
                "Detector-A-Min Area":detectorAObject.detectorMinArea,
                "Detector-A-Min Height":detectorAObject.detectorMinHeight,
                "Detector-A-Segment Width":detectorAObject.detectorSegmentWidth,
                "Detector-A-Detector Units":detectorAObject.detectorUnits,
                "Detector-A-Peak Algorithm":detectorAObject.detectorPeaksAlgorithm,
                "Detector-A-Detect Method":detectorAObject.detectorDetectMethod,
                "Detector-A-Data To Excel":detectorAObject.detectorDataToExcelFlag,
                "Detector-A-Lamp Save":detectorAObject.detectorLampSaveFlag,
                "Detector-A-Auto":detectorAObject.detectorAutoFlag,
                "Detector-A-Range Selection":detectorAObject.detectorRangeSelection,
                }
        xAB_json = json.dumps(x_AB,indent = 2)
        my_file1.write(xAB_json)
        return my_stringA,my_stringB
    
    elif A_Flag == 0 and B_Flag == 1:
        
        my_stringA = os.path.splitext(my_string1)[0]
        my_stringA = my_stringA + '-Detector-A.csv'
        my_stringB = os.path.splitext(my_string1)[0]
        my_stringB = my_stringB + '-Detector-B.csv'
        x_AB = {
            'Detector A':"OFF",'Detector B':"ON",
            "Detector-B-Data": my_stringB,
            "Detector-B-Label":detectorBObject.detectorLabelStr,
            "Detector-B-Log":detectorBObject.detectorLogFlag,
            "Detector-B-External":detectorBObject.detectorExternalFlag,
            "Detector-B-Invert":detectorBObject.detectorInvertFlag,
            "Detector-B-Time":detectorBObject.detectorTimeStr,
            "Detector-B-Length":detectorBObject.detectorLengthStr,
            "Detector-B-Min Area":detectorBObject.detectorMinArea,
            "Detector-B-Min Height":detectorBObject.detectorMinHeight,
            "Detector-B-Segment Width":detectorBObject.detectorSegmentWidth,
            "Detector-B-Detector Units":detectorBObject.detectorUnits,
            "Detector-B-Peak Algorithm":detectorBObject.detectorPeaksAlgorithm,
            "Detector-B-Detect Method":detectorBObject.detectorDetectMethod, 
            "Detector-B-Data To Excel":detectorBObject.detectorDataToExcelFlag,    
            "Detector-B-Lamp Save":detectorBObject.detectorLampSaveFlag,    
            "Detector-B-Auto":detectorBObject.detectorAutoFlag,
            "Detector-B-Range Selection":detectorBObject.detectorRangeSelection, 
            }
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
    global values_thread_A,values_thread_B,read_values,A_Flag,B_Flag
    global x_gc,gc_values,x_gcB,gc_valuesB,startAcquire,StopAcquire,main_stoping_thread,values_thread_B
    x_gc = []
    gc_values = []
    x_gcB = []
    gc_valuesB = []
    startAcquire = False
    if A_Flag == 1:
        PIDGraphObject.stop_threading_A()
        values_thread_A.join()
    if B_Flag == 1:
        PIDGraphObject.stop_threading_B()
        values_thread_B.join()
    read_values = False
    stopButton["state"] = DISABLED
    #print(x_gc,gc_values,x_gcB,gc_valuesB)
    

def CreateStatusBar(top):
        statusBar = ttk.Label(root, text="Oven=829C ,    Det 823C A:10, B:10, Flow: 0.0", relief=GROOVE, anchor=W)
        statusBar.pack(side=BOTTOM, fill=X)
        
#global cons_filename
def Loadcallback_plot():
    #def FileOpenWrapper():
    PIDGraphObject.PushPlotsAndTableDown()
    FileMenuOptionsObject.FileMenuOpen()
    PIDGraphObject.PushPlotsAndTableUp()
    Jobfilename = FileMenuOptionsObject.LoadFile.get()
    #print(Jobfilename)
    acquireButton["state"] = DISABLED
    f = open(Jobfilename)
    data = json.load(f)
    if data['Detector A'] == "ON" :
        detectorAObject.OnOffFlag.set(True)
    else:
        detectorAObject.OnOffFlag.set(False)
        
    if data['Detector B'] == "ON" :
        detectorBObject.OnOffFlag.set(True)
    else:
        detectorBObject.OnOffFlag.set(False)
    if detectorAObject.OnOffFlag.get():
        PIDGraphObject.aX_Save_values = []
        PIDGraphObject.aY_Save_values = []
        with open(data['Detector-A-Data'],'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                row_A0 = float(row[0])
                row_A1 = float(row[1])
                #PIDGraphObject.aX_values.append(row[0])
                #PIDGraphObject.aY_values.append(row[1])
                PIDGraphObject.aX_Save_values.append(row_A0)
                PIDGraphObject.aY_Save_values.append(row_A1)
                #print(PIDGraphObject.aX_values)
        PIDGraphObject.PopUpGraphA_Cons()
    else:
        pass
    if detectorBObject.OnOffFlag.get():
        PIDGraphObject.bX_Save_values = []
        PIDGraphObject.bY_Save_values = []
        with open(data['Detector-B-Data'],'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                row_B0 = float(row[0])
                row_B1 = float(row[1])
                #PIDGraphObject.bX_values.append(row[0])
                #PIDGraphObject.bY_values.append(row[1])
                PIDGraphObject.bX_Save_values.append(row_B0)
                PIDGraphObject.bY_Save_values.append(row_B1)
        PIDGraphObject.PopUpGraphB_Cons()
    else:
        pass
    return
    
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
    
    global acquireButton,stopButton
    acquireButton = Button(IconLevelMenuBar,image = acquireIcon,command = AcquireIconCallback,state = ACTIVE)
    acquireButton.pack(side=LEFT)

    
    scaleNoIcon=PhotoImage(file=r'SCALE_NO.png')
    scaleNoIcon  = scaleNoIcon.subsample(1,1)  
    Button(IconLevelMenuBar,image = scaleNoIcon,command = callback).pack(side=LEFT)

    stopIcon =PhotoImage(file=r'STOP.png')
    stopIcon = stopIcon.subsample(1,1)  
    stopButton = Button(IconLevelMenuBar,image = stopIcon,command = Stopcallback,state = DISABLED)
    stopButton.pack(side=LEFT)

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
		
def ActivateAcquire():
    global acquireButton
    acquireButton["state"] = ACTIVE
    return

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
  
  # Creating Threading Lock to access plotting variables
  #PIDGraphObject.plotLock = Lock()
  #print("Lock_1:", PIDGraphObject.plotLock)
  
  CreateTopLevelMenuBar()
  root.bind("<Button 1>",GetMousePointsOfRoots)
  root.bind('<Configure>',PIDGraphObject.UpdateTopLeftCoordsOfRootWindow)
  root.geometry(("+{0}+{1}".format(100,100)))
  root.resizable(False, False)
  root.mainloop()


if __name__ == '__main__':
  #global lock
  main()
