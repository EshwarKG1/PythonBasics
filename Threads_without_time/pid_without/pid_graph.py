from tkinter import *
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import ttk
import tkinter as tk
import matplotlib as mpl
import time
import pandas as pd
from scipy.interpolate import make_interp_spline
import sys
from daqhats import hat_list, HatIDs, mcc118
import threading
from pid_menu_oo import myReadValues
from pid_menu_oo import myReadValuesB
from pid_menu_oo import Loadcallback_plot as lc
from pid_menu_oo import Stopcallback
from sys import stdout
#import pid_menu_oo
#from pid_menu_oo import Localcallback
#print(gc_values)
"""
global channel_number,channel_number1,X,Y
channel_number = 0
channel_number1 = 1

board_list = hat_list(filter_by_id = HatIDs.ANY)
if board_list[0].id == HatIDs.MCC_118:
    board = mcc118(board_list[0].address)
   
global StopAcquire
StopAcquire = pid_menu_oo.StopAcquire
#print(StopAcquire)

def LoadcallbackA(my_direc):
    a_values = []
    dire =  my_direc # "/home/acufore/Eshwar/New/pid_with_threads/log_files/detectA.JOB" #my_direc
    with open(dire,"r") as file:
        data = file.readlines()
        values_i = 1
        for k in data:
            #print(k)
            l = k.split(",")
            if values_i == 1:
                l.pop(0)
                values_i = 2
            elif l[0] == '\n':
                l.remove('\n')
            else:
                a_values.append(l[0])       
    return a_values

def LoadcallbackB(my_direc):
    b_values = []
    dire = my_direc #"/home/acufore/Eshwar/New/pid_with_threads/log_files/detectB.JOB"
    with open(dire,"r") as file:
        data = file.readlines()
        values_i = 1
        for k in data:
            #print(k)
            l = k.split(",")
            if values_i == 1:
                l.pop(0)
                values_i = 2
            elif l[0] == '\n':
                l.remove('\n')
            else:
                b_values.append(l[0])       
    return b_values
"""
def Loadcallback(my_direc):
    a_values = []
    b_values = []
    only_graphAB = 0
    dire = my_direc # "/home/acufore/Eshwar/New/pid_with_threads/log_files/working_AA.JOB"
    with open(dire,"r") as f:
        data = f.readlines()
        for k in data:
            l = k.split(",")
            if l[0] == 'Detector A' and l[1] == 'Detector B':
                only_graphAB = 1
                #print("1")
            elif l[0] == 'Detector A':
                only_graphAB = 2
                #print("2")
            elif l[0] == 'Detector B':
                only_graphAB = 3
                #print("3")
    if only_graphAB == 1 :
        with open(dire,"r") as file:
            dataAB = file.readlines()
            valuesAB_i = 1
            for k_AB in dataAB:
                try:
                    l_AB = k_AB.split(",")
                    #print(l[0],l[1])
                    if valuesAB_i == 1:
                        l_AB.pop(0)
                        l_AB.pop(0)
                        valuesAB_i = 2
                    if l_AB[0] == '\n':
                        l_AB.remove('\n')
                    else:
                        a_values.append(l_AB[0])
                        b_values.append(l_AB[1])
                except IndexError:
                    pass
        return a_values,b_values
    elif only_graphAB == 2 :
        with open(dire,"r") as fileA:
            dataA = fileA.readlines()
            valuesA_i = 1
            for k_A in dataA:
                #print(k)
                l_A = k_A.split(",")
                if valuesA_i == 1:
                    l_A.pop(0)
                    valuesA_i = 2
                elif l_A[0] == '\n':
                    l_A.remove('\n')
                else:
                    a_values.append(l_A[0])       
        return a_values,b_values
    elif only_graphAB == 3:
        with open(dire,"r") as fileB:
            dataB = fileB.readlines()
            valuesB_i = 1
            for k_B in dataB:
                #print(k)
                l_B = k_B.split(",")
                if valuesB_i == 1:
                    l_B.pop(0)
                    valuesB_i = 2
                elif l_B[0] == '\n':
                    l_B.remove('\n')
                else:
                    b_values.append(l_B[0])       
        return a_values,b_values
    else:
        return a_values,b_values
"""
def SmoothPlot(x,y):
    model = make_interp_spline(x,y)
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = model(X_)
    return X_, Y_
"""
class PlotGraphClass:
  def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        #self.listOfPoints =  #[0.01,0.02,0.03,0.05,0.06,0.03,0.03,0.04,0.04,0.02,0.01,0.01,0,0.01,0.02,0.02,0.02,0.02,0.03,0.03,0.09,0.5,0.09,0.06,0.05,0.02,0.01]
        #self.listOfPointsB = [0.01,0.02,0.03,0.05,0.06,0.03,0.03,0.04,0.04,0.7,0.01,0.01,0,0.01,0.02,0.03,0.25,0.02,0.03,0.03,0.09,0.3,0.09,0.06,0.05,0.02,0.01]
        self.GraphAPopUpWindow = None
        self.GraphBPopUpWindow = None
        self.TopFrame          = None
        self.BottomFrame       = None
        
        self.TableAPopUpWindow = None
        self.TableBPopUpWindow = None
        self.TableA            = None
        self.TableB            = None
        self.TableAData        = []
        self.TableBData        = []
        self.TopLeftRootX      = 0
        self.TopLeftRootY      = 0
        self.BottomRightRootX  = 1199 
        self.BottomRightRootY  = 599

  def PushPlotsAndTableDown(self):
        if (self.GraphAPopUpWindow != None):
           self.GraphAPopUpWindow.attributes('-topmost',False)
        if (self.GraphBPopUpWindow != None):   
           self.GraphBPopUpWindow.attributes('-topmost',False)
        if (self.TableAPopUpWindow != None):
           self.TableAPopUpWindow.attributes('-topmost',False)
        if (self.TableBPopUpWindow != None):
           self.TableBPopUpWindow.attributes('-topmost',False)  
        return
        
  def PushPlotsAndTableUp(self):
        if (self.GraphAPopUpWindow != None):
           self.GraphAPopUpWindow.attributes('-topmost',True)
        if (self.GraphBPopUpWindow != None):   
           self.GraphBPopUpWindow.attributes('-topmost',True)
        if (self.TableAPopUpWindow != None):
           self.TableAPopUpWindow.attributes('-topmost',True)
        if (self.TableBPopUpWindow != None):
           self.TableBPopUpWindow.attributes('-topmost',True)  
        return        
        
  def UpdateTopLeftCoordsOfRootWindow(self,event):
      self.topLeftX = event.x
      self.topLeftY = event.y
      
      # Following are absolute locations on the screen
      # and not the x,y relative to root.
      #self.TopLeftRootX = event.x 
      #self.TopLeftRootY = event.y
      
      self.TopLeftRootX = self.parentWindow.winfo_x()
      self.TopLeftRootY = self.parentWindow.winfo_y()
      
      self.BottomRightRootX = self.parentWindow.winfo_x()+1199
      self.BottomRightRootY = self.parentWindow.winfo_y()+599

      #print("UpdateTopLeftCoordsOfRootWindow:","x= ",self.TopLeftRootX,"y=",self.TopLeftRootY)
      
      if (self.GraphAPopUpWindow != None):      
        self.GraphAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+70))))
        
      if (self.TableAPopUpWindow != None):        
        self.TableAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+70))))  
        
      if (self.GraphBPopUpWindow != None):            
        self.GraphBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+325))))   
        
      if (self.TableBPopUpWindow != None):            
        self.TableBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+325))))             
                    
      return
        
  def SetTableAData(self,data):
      self.TableAData =[
                   ['Hydrogen','5.094H','2587', '0.35','171560','0.13','0:75'],
                   ['Oxygen','17.4H','113252', '44.86','48041832','37.41','0:83'],
                   ['Nitrogen','66.005H','253840', '34.32','54625328','42.54','1:14'],
                   ['Carbon Dioxide','9.670H','38112', '5.15','8813312','6.86','1:75'],
                   ['Argon','5.094H','2587', '0.35','171560','0.13','2:05'],   
                   ['Carbon Monodioxide','9.670H','38112', '5.15','8813312','6.86','2:25'],
                   ['Methane','66.005H','253840', '34.32','54625328','42.54','2:44'],
                   ['Octane','17.4H','113252', '44.86','48041832','37.41','2:83'],
                   ['Pentane','66.005H','253840', '34.32','54625328','42.54','3:14'],
                   ['Nonane','9.670H','38112', '5.15','8813312','6.86','3:25'],
                   ['Propane','5.094H','2587', '0.35','171560','0.13','3:75'],   
                   ['Heptane','9.670H','38112', '5.15','8813312','6.86','4:30'],
                   ['Hexane','66.005H','253840', '34.32','54625328','42.54','4:50']                   
                   ]
      return

  def SetTableBData(self,data):
      self.TableBData =[
                   ['Benzene','5.094H','2587', '0.35','171560','0.13','0:75'],
                   ['Chloroform ','17.4H','113252', '44.86','48041832','37.41','0:83'],
                   ['Ethane','66.005H','253840', '34.32','54625328','42.54','1:14'],
                   ['Ethylene','9.670H','38112', '5.15','8813312','6.86','1:75'],
                   ['Methyl Acetate','5.094H','2587', '0.35','171560','0.13','2:75'],   
                   ['Carbon Monodioxide','9.670H','38112', '5.15','8813312','6.86','2:85'],
                   ['Methylene Chloride','66.005H','253840', '34.32','54625328','42.54','3:14']]
      return
    
  def plotA_running(self,stopA):
      figure = Figure(figsize=(15, 10))
      figure.patch.set_facecolor('#ECF0F1')  # The region our side plot get a different color
      subplot = figure.subplots()
      subplot.set_facecolor("#000001") # Region inside the plot      
      subplot.grid()
      canvas = FigureCanvasTkAgg(figure, master=self.GraphAPopUpWindow)
      subplot.set_title("Graph  A")
      canvas.draw()
      canvas.get_tk_widget().pack(side=TOP)
      while True:
          #from pid_menu_oo import gc_values
          #print(gc_values)
          #actual_time = time.time()-start_time
          #X.append(actual_time)
          #print("x = ",X)
          #print("values = ",myReadValues())  
          subPlotHandle, = subplot.plot(myReadValues()[0],myReadValues()[1], color='#FF6700')
          #print("values = ",myReadValues())          
          subPlotHandle.set_data(myReadValues()[0],myReadValues()[1])
          #print("values = ",myReadValues())
          canvas.draw()
          canvas.flush_events()
          if stopA():
              break
      return
    
  def plotA(self):
      global stop_threadsA,myPlotA_thread
      stop_threadsA = False
      myPlotA_thread = threading.Thread(target=self.plotA_running,args =(lambda : stop_threadsA, ))
      myPlotA_thread.start()
      return
    
  def stop_threading_A(self):
      global stop_threadsA,myPlotA_thread
      stop_threadsA = True
      #myPlotA_thread.join()
      return
        
  def plotB_running(self,stopB):
      global stop_threadsB
      figure = Figure(figsize=(15, 10))
      figure.patch.set_facecolor('#ECF0F1')  # The region our side plot get a different color
      subplot = figure.subplots()
      subplot.set_facecolor("#000001") # Region inside the plot      
      subplot.grid()
      canvas = FigureCanvasTkAgg(figure, master=self.GraphBPopUpWindow)
      subplot.set_title("Graph  B")
      canvas.draw()
      canvas.get_tk_widget().pack(side=TOP)
      #StopAcquire = pid_menu_oo.Stopcallback.StopAcquire
      while True:
          #from pid_menu_oo import gc_values
          #print(gc_values)
          #actual_time = time.time()-start_time
          #X.append(actual_time)
          #print("x = ",X)
          #print("values = ",myReadValues())  
          subPlotHandle, = subplot.plot(myReadValuesB()[0],myReadValuesB()[1], color='#00B5FF')
          #print("values = ",myReadValues()) 
          subPlotHandle.set_data(myReadValuesB()[0],myReadValuesB()[1])
          #print("values = ",myReadValues()) 
          canvas.draw()
          canvas.flush_events()
          if stopB():
              break
      return
    
  def plotB(self):
      global stop_threadsB,myPlotB_thread
      stop_threadsB = False
      myPlotB_thread = threading.Thread(target=self.plotB_running,args =(lambda : stop_threadsB, ))
      myPlotB_thread.start()
      #time.sleep(1)
      #stop_threads = True
      #myPlotB_thread.join()
      #Stopcallback.stop_threads
      return
   
  def stop_threading_B(self):
      global stop_threadsB,myPlotB_thread
      stop_threadsB = True
      #myPlotB_thread.join()
      return
  """    
  def waste():
      # Python program killing
    # threads using stop
    # flag

    import threading
    import time

    def run(stop):
        while True:
            print('thread running')
            if stop():
                    break
                    
    def main():
            stop_threads = False
            t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
            t1.start()
            time.sleep(1)
            stop_threads = True
            t1.join()
            print('thread killed')
    main()
  """
  def plotA_Cons(self,cons_filename):
      yA_cons_values = []
      yB_cons_values = []
      #xA_cons = range(50)
      yA_cons_values,yB_cons_values = Loadcallback(cons_filename)
      #print(yB_cons_values)
      #yA_cons_values = LoadcallbackA(cons_filename)
      #yA_cons_values.pop(0),yB_cons_values
      #print(yA_cons_values[1:20])
      if yA_cons_values != []:
          figure = Figure(figsize=(15, 10))
          figure.patch.set_facecolor('#ECF0F1')  # The region our side plot get a different color
          subplot = figure.subplots()
          subplot.set_facecolor("#000001") # Region inside the plot      
          subplot.grid()
          canvas = FigureCanvasTkAgg(figure, master=self.GraphAPopUpWindow)
          subplot.set_title("Graph  A")
          canvas.draw()
          canvas.get_tk_widget().pack(side=TOP)
          
          yA_cons_valuesF = []
          for i in range(len(yA_cons_values)):
              yA_cons_valuesF.append(float(yA_cons_values[i]))
          #print(yA_cons_values)
          #xA_cons = range(len(yA_cons_values)xA_cons,)
          subplot.plot(yA_cons_valuesF,color='#FF6700')
          #canvas.draw()
      else:
          #self.GraphAPopUpWindow.destroy()
          pass
      return
  def plotB_Cons(self,cons_filename):
      yA_cons_values = []
      yB_cons_values = []
      yA_cons_values,yB_cons_values = Loadcallback(cons_filename)
      #print(yB_cons_values)
      #yB_cons_values = LoadcallbackB(cons_filename)
      if yB_cons_values != [] :
          figure = Figure(figsize=(15, 10))
          figure.patch.set_facecolor('#ECF0F1')  # yA_cons_values, The region our side plot get a different color
          subplot = figure.subplots()
          subplot.set_facecolor("#000001") # Region inside the plot      
          subplot.grid()
          canvas = FigureCanvasTkAgg(figure, master=self.GraphBPopUpWindow)
          subplot.set_title("Graph  B")
          canvas.draw()
          canvas.get_tk_widget().pack(side=TOP)
          
          yB_cons_valuesF = []
          for i in range(len(yB_cons_values)):
              yB_cons_valuesF.append(float(yB_cons_values[i]))
          #print(yA_cons_values)
          subplot.plot(yB_cons_valuesF,color='#00B5FF')
          #canvas.draw()
      else:
          #self.GraphBPopUpWindow.destroy()
          pass
      return
      
  def onClosingA(self):
      #print("Onclosing A")
      self.GraphAPopUpWindow.destroy()
      self.GraphAPopUpWindow = None
      return
      
  def onClosingB(self):
      #print("Onclosing B")
      self.GraphBPopUpWindow.destroy()
      self.GraphBPopUpWindow = None
      return
      
  def PopUpAWindowMove(self,event):
      
      '''
      print("PopUpAWindowMove", "event.height" , event.height, 
                                "event.width",event.width,
                                "event.x", event.x,
                                "event.y", event.y)
      '''
      
      return

  def PopUpGraphA_Cons(self,cons_filename):
    #if (self.TopFrame != None):
    #    # Close the tiled charts
    #    self.TopFrame.destroy()
    #   self.TopFrame = None 
    self.SetTableAData("x")
    if (self.GraphAPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 
        
    #print(self.GraphAPopUpWindow)
    self.GraphAPopUpWindow= Toplevel(self.parentWindow)
    self.GraphAPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingA)
    self.GraphAPopUpWindow.geometry("592x220")
    self.GraphAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+70))))
    string = "+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+100))
    #print("PopUpGraphA:GraphAPopUpWindow:",string)    

    #self.GraphAPopUpWindow.transient(self.parentWindow)
    self.GraphAPopUpWindow.attributes('-topmost',True)
    #title_bar = Frame(self.GraphAPopUpWindow, relief='raised', bd=6)
    #title_bar.pack(expand=1, fill=X)
    #title_bar.pack(expand=1, fill=X)
    #print(dir(self.GraphAPopUpWindow))
    self.GraphAPopUpWindow.title("GraphA")
    #windowWidth   = self.GraphAPopUpWindow.winfo_reqwidth()
    #windowHeight  = self.GraphAPopUpWindow.winfo_reqheight()
    #positionRight = int(self.GraphAPopUpWindow.winfo_screenwidth()/4 - windowWidth/2)
    #positionDown  = int(self.GraphAPopUpWindow.winfo_screenheight()/4 - windowHeight/2)
    #print("Position Right=",positionRight, "Position Down= ",positionDown)
    #self.GraphAPopUpWindow.geometry("+{}+{}".format(positionRight, positionDown))
    
    #self.GraphAPopUpWindow.resizable(False, False)
    self.GraphAPopUpWindow.bind('<Configure>', self.PopUpAWindowMove)
    #self.GraphAPopUpWindow.lift() 
    self.plotA_Cons(cons_filename)
   
  def PopUpGraphB_Cons(self,cons_filename):
  
    if (self.BottomFrame != None):
        self.BottomFrame.destroy()   
        self.BottomFrame = None
        
    if (self.GraphBPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 
    self.SetTableBData("x")    
    self.GraphBPopUpWindow= Toplevel(self.parentWindow)
    self.GraphBPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingB)
    self.GraphBPopUpWindow.geometry("592x220")
    self.GraphBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+325))))    
    self.GraphBPopUpWindow.title("GraphB")
    #self.GraphBPopUpWindow.transient(self.parentWindow)
    self.GraphBPopUpWindow.attributes('-topmost',True)
    self.GraphBPopUpWindow.bind('<Configure>', self.PopUpBWindowMove)
    #title_bar = Frame(self.GraphBPopUpWindow, bg='red', relief='raised', bd=6)
    #title_bar.pack(expand=1, fill=X)    
    #print(dir(self.GraphAPopUpWindow))
    #self.GraphBPopUpWindow.transient(self.parentWindow)
    #windowWidth   = self.GraphBPopUpWindow.winfo_reqwidth()
    #windowHeight  = self.GraphBPopUpWindow.winfo_reqheight()
    #positionRight = int(self.GraphBPopUpWindow.winfo_screenwidth()/3 - windowWidth/2)
    #positionDown  = int(self.GraphBPopUpWindow.winfo_screenheight()/3 - windowHeight/2)
    #self.GraphBPopUpWindow.geometry("+{}+{}".format(positionRight, positionDown))    
    self.plotB_Cons(cons_filename)
    
  def PopUpGraphA(self):
    #if (self.TopFrame != None):
    #    # Close the tiled charts
    #    self.TopFrame.destroy()
    #   self.TopFrame = None 
    self.SetTableAData("x")
    if (self.GraphAPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 
        
    #print(self.GraphAPopUpWindow)
    self.GraphAPopUpWindow= Toplevel(self.parentWindow)
    self.GraphAPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingA)
    self.GraphAPopUpWindow.geometry("592x220")
    self.GraphAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+70))))
    string = "+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+100))
    #print("PopUpGraphA:GraphAPopUpWindow:",string)    

    #self.GraphAPopUpWindow.transient(self.parentWindow)
    self.GraphAPopUpWindow.attributes('-topmost',True)
    #title_bar = Frame(self.GraphAPopUpWindow, relief='raised', bd=6)
    #title_bar.pack(expand=1, fill=X)
    #title_bar.pack(expand=1, fill=X)
    #print(dir(self.GraphAPopUpWindow))
    self.GraphAPopUpWindow.title("GraphA")
    #windowWidth   = self.GraphAPopUpWindow.winfo_reqwidth()
    #windowHeight  = self.GraphAPopUpWindow.winfo_reqheight()
    #positionRight = int(self.GraphAPopUpWindow.winfo_screenwidth()/4 - windowWidth/2)
    #positionDown  = int(self.GraphAPopUpWindow.winfo_screenheight()/4 - windowHeight/2)
    #print("Position Right=",positionRight, "Position Down= ",positionDown)
    #self.GraphAPopUpWindow.geometry("+{}+{}".format(positionRight, positionDown))
    
    #self.GraphAPopUpWindow.resizable(False, False)
    self.GraphAPopUpWindow.bind('<Configure>', self.PopUpAWindowMove)
    #self.GraphAPopUpWindow.lift() 
    self.plotA()
    
  def PopUpBWindowMove(self,event):

      '''
      print("PopUpBWindowMove", "event.height" , event.height, 
                                "event.width",event.width,
                                "event.x", event.x,
                                "event.y", event.y)
      '''
      
      return
    
  def PopUpGraphB(self):
  
    if (self.BottomFrame != None):
        self.BottomFrame.destroy()   
        self.BottomFrame = None
        
    if (self.GraphBPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 
    self.SetTableBData("x")    
    self.GraphBPopUpWindow= Toplevel(self.parentWindow)
    self.GraphBPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingB)
    self.GraphBPopUpWindow.geometry("592x220")
    self.GraphBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+325))))    
    self.GraphBPopUpWindow.title("GraphB")
    #self.GraphBPopUpWindow.transient(self.parentWindow)
    self.GraphBPopUpWindow.attributes('-topmost',True)
    self.GraphBPopUpWindow.bind('<Configure>', self.PopUpBWindowMove)
    #title_bar = Frame(self.GraphBPopUpWindow, bg='red', relief='raised', bd=6)
    #title_bar.pack(expand=1, fill=X)    
    #print(dir(self.GraphAPopUpWindow))
    #self.GraphBPopUpWindow.transient(self.parentWindow)
    #windowWidth   = self.GraphBPopUpWindow.winfo_reqwidth()
    #windowHeight  = self.GraphBPopUpWindow.winfo_reqheight()
    #positionRight = int(self.GraphBPopUpWindow.winfo_screenwidth()/3 - windowWidth/2)
    #positionDown  = int(self.GraphBPopUpWindow.winfo_screenheight()/3 - windowHeight/2)
    #self.GraphBPopUpWindow.geometry("+{}+{}".format(positionRight, positionDown))    
    self.plotB()    
    
  def TileHorizontalA(self):
    '''
    if (self.GraphAPopUpWindow != None):
        self.onClosingA()
        
    if (self.TopFrame != None):
        return
        
    self.TopFrame = Frame(self.parentWindow,borderwidth=4,relief=GROOVE)
    self.plotA("tile")    
    self.TopFrame.pack(side=TOP)
    '''
    return
  def TileHorizontalB(self):
    '''
    if (self.GraphBPopUpWindow != None):
       self.onClosingB()
       
    if (self.BottomFrame != None):
        return
        
    self.BottomFrame = Frame(self.parentWindow,borderwidth=4,relief=GROOVE)
    self.plotB("tile")  
    self.BottomFrame.pack(side=TOP)
    '''
    return
    
  def TileHorizontal(self):
    self.TileHorizontalA()
    self.TileHorizontalB()

  def CloseAll(self):
  
    if (self.BottomFrame != None):
        self.BottomFrame.destroy()   
        self.BottomFrame = None
        
    if (self.TopFrame != None):
        self.TopFrame.destroy()   
        self.TopFrame = None

    if (self.GraphAPopUpWindow != None):
        self.GraphAPopUpWindow.destroy()
        self.GraphAPopUpWindow = None
        
    if (self.GraphBPopUpWindow != None):
        self.GraphBPopUpWindow.destroy()
        self.GraphBPopUpWindow = None
        
    if (self.TableAPopUpWindow != None):
        self.TableAPopUpWindow.destroy()
        self.TableAPopUpWindow = None

    if (self.TableBPopUpWindow != None):
        self.TableBPopUpWindow.destroy()
        self.TableBPopUpWindow = None
        
  def ShowTableA(self,ParentWindow):
        frame=ParentWindow
        columns = ('name', 'concentration1', 'height', 'percentage1', 'area', 'percentage2', 'time')
        self.TableA = ttk.Treeview(frame, columns=columns, show='headings',height=10)
        frame.pack(side=TOP)
        style = ttk.Style(ParentWindow)
        style.theme_use("clam")
        style.configure(self.TableA.heading, background="black", foreground="white")
        # Create Headings
        self.TableA.heading('name', text='Name')
        self.TableA.column('name', minwidth=0, width=200, stretch=True)
        
        self.TableA.heading('concentration1', text='Conc')
        self.TableA.column('concentration1', minwidth=0, width=60,stretch=True)
        self.TableA.heading('height', text='Height')
        self.TableA.column('height', minwidth=0, width=60,stretch=True)
        self.TableA.heading('percentage1', text='%')
        self.TableA.column('percentage1', minwidth=0, width=50,stretch=True)
        self.TableA.heading('area', text='Area')
        self.TableA.column('area', minwidth=0, width=80,stretch=True)
        self.TableA.heading('percentage2', text='%')
        self.TableA.column('percentage2', minwidth=0, width=70,stretch=True)
        self.TableA.heading('time', text='Time')
        self.TableA.column('time', minwidth=0, width=50, stretch=True)
        #self.TableA.bind('<Double-1>', self.ItemSelectedInTableA)
        #self.TableA.bind('<<TreeviewSelect>>', self.ItemFocusedInTableA)
        self.TableA.pack(side=LEFT)
      
        # Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.TableA.yview)
        self.TableA.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
      
        # add data to the treeview
        for entry in self.TableAData:
           self.TableA.insert('', tk.END, values=entry)
        
        return
        
  def ShowTableB(self,ParentWindow):
        frame=ParentWindow
        columns = ('name', 'concentration1', 'height', 'percentage1', 'area', 'percentage2', 'time')
        self.TableB = ttk.Treeview(frame, columns=columns, show='headings',height=10)
        frame.pack(side=TOP)
        style = ttk.Style(ParentWindow)
        style.theme_use("clam")
        style.configure(self.TableB.heading, background="black", foreground="white")

        # Create Headings
      
        self.TableB.heading('name', text='Name')
        self.TableB.column('name', minwidth=0, width=200, stretch=True)
        
        self.TableB.heading('concentration1', text='Conc')
        self.TableB.column('concentration1', minwidth=0, width=60,stretch=True)
        
        self.TableB.heading('height', text='Height')
        self.TableB.column('height', minwidth=0, width=60,stretch=True)
        
        self.TableB.heading('percentage1', text='%')
        self.TableB.column('percentage1', minwidth=0, width=50,stretch=True)
        
        self.TableB.heading('area', text='Area')
        self.TableB.column('area', minwidth=0, width=80,stretch=True)
        
        self.TableB.heading('percentage2', text='%')
        self.TableB.column('percentage2', minwidth=0, width=50,stretch=True)
        
        self.TableB.heading('time', text='Time')
        self.TableB.column('time', minwidth=0, width=70, stretch=True)
        
        #self.TableA.bind('<Double-1>', self.ItemSelectedInTableA)
        #self.TableA.bind('<<TreeviewSelect>>', self.ItemFocusedInTableA)
        self.TableB.pack(side=LEFT)
      
        # Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.TableB.yview)
        self.TableB.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
      
        # add data to the treeview
        for entry in self.TableBData:
           self.TableB.insert('', tk.END, values=entry)

        return
        
  def onClosingTableA(self):
      self.TableAPopUpWindow.destroy()
      self.TableAPopUpWindow = None
      
  def onClosingTableB(self):
      self.TableBPopUpWindow.destroy()
      self.TableBPopUpWindow = None
      
  def TableAPopUpWindowMove(self,event): 
        
      #print("TableAPopUpWindowMove:", "event.height" , event.height, 
      #                          "event.width",event.width,
      #                          "event.x", event.x,
      #                          "event.y", event.y)  
      
      return
      
  def CreateTableA(self):
  
     if (self.TableAPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 

     
     self.TableAPopUpWindow= Toplevel(self.parentWindow)    
     self.TableAPopUpWindow.attributes('-topmost',True)
     self.TableAPopUpWindow.geometry("592x220")
     self.TableAPopUpWindow.resizable(False, False)
     self.TableAPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingTableA)
     self.TableAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+70))))
     self.TableAPopUpWindow.title("TableA")
     self.TableAPopUpWindow.lift()
     frame=Frame(self.TableAPopUpWindow)

     #self.TableAPopUpWindow.bind('<Configure>', self.TableAPopUpWindowMove)
     self.ShowTableA(frame)

     return
     
  def CreateTableB(self):
  
     if (self.TableBPopUpWindow != None):
        # We do not want to open multiple windows of the same chart
        return 
        
     self.TableBPopUpWindow= Toplevel(self.parentWindow)
     self.TableBPopUpWindow.attributes('-topmost',True)
     self.TableBPopUpWindow.geometry("592x220")     
     self.TableBPopUpWindow.resizable(False, False)     
     self.TableBPopUpWindow.protocol("WM_DELETE_WINDOW", self.onClosingTableB)
     self.TableBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+325))))     
     self.TableBPopUpWindow.title("TableB")
          
     
     #self.TableBPopUpWindow.lift()
     frame=Frame(self.TableBPopUpWindow)
     self.ShowTableB(frame)
     
  def ArrageAll(self):
  
      if (self.GraphAPopUpWindow != None):         
        self.GraphAPopUpWindow.lift()
        self.GraphAPopUpWindow.attributes('-topmost',True)
        self.GraphAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+70))))
        #print("ArrangeAll GraphAPopUpWindow:",self.TopLeftRootX,self.TopLeftRootY)
        string = "+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+100))
        #print("ArrangeAll GraphAPopUpWindow:",string)
        
      if (self.TableAPopUpWindow != None):
        self.TableAPopUpWindow.lift()
        self.TableAPopUpWindow.attributes('-topmost',True)
        self.TableAPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+70))))        
        #print("ArrangeAll TableAPopUpWindow:",(self.TopLeftRootX+603),(self.TopLeftRootY+100))
        
      if (self.GraphBPopUpWindow != None):
        self.GraphBPopUpWindow.lift()
        self.GraphBPopUpWindow.attributes('-topmost',True)
        self.GraphBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+5),(self.TopLeftRootY+325))))    
        #print("ArrangeAll GraphBPopUpWindow:",(self.TopLeftRootX+5),(self.TopLeftRootY+320))
        
      if (self.TableBPopUpWindow != None):
        self.TableBPopUpWindow.lift()
        self.TableBPopUpWindow.attributes('-topmost',True)
        self.TableBPopUpWindow.geometry(("+{0}+{1}".format((self.TopLeftRootX+603),(self.TopLeftRootY+325))))     
        #print("ArrangeAll TableBPopUpWindow:",(self.TopLeftRootX+603),(self.TopLeftRootY+320))
        
      return         
        
  

