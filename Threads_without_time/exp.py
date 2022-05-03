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

main_page = Tk()
lst1 = []
lst2 = []
listOfPoints = [lst1,lst2]

def plotA(channel_number):
  # Step 1: Create a set of close points when ploted will give a smooth curve
  y = np.array(listOfPoints[0])
  Y = []
  #xlables = list(range(len(y))) 
  x = np.array(listOfPoints[1])
  X = []
  #X, Y = SmoothPlot(x,y)
  
  # Step 2: Plot those points on Figure
  figure = Figure(figsize=(15, 10))
  figure.patch.set_facecolor('#ECF0F1')  # The region our side plot get a different color
  subplot = figure.subplots()
  # color='#FF6700')  # Actual plot    
  #subplot.set_facecolor("#000001") # Region inside the plot      
  #subplot.grid() # Draws Grid lines
  
  # Step 3: Put the plot on to a Canvas
  canvas = FigureCanvasTkAgg(figure, master = main_page)# master=self.GraphAPopUpWindow)
  subplot.set_title("Graph  A")
  canvas.draw()
  canvas.get_tk_widget().pack(side=TOP)
  
  board_list = hat_list(filter_by_id = HatIDs.ANY)
  if board_list[0].id == HatIDs.MCC_118:
    board = mcc118(board_list[0].address)
    
  start_time = time.time()
  while True:
    try:
        print(board.a_in_read(channel_number))
        Y.append(board.a_in_read(channel_number))
        #np.append(Y,board.a_in_read(channel_number))
        print("Y",Y)
        actual_time = time.time()-start_time
        X.append(actual_time)
        print("X",X)
        #np.append(X,actual_time)
        subPlotHandle, =subplot.plot(X,Y)
        subPlotHandle.set_data(X,Y)
        canvas.draw()
        canvas.flush_events()
    except KeyboardInterrupt:
        subplot.close()
        break
  
  return
Button(text="clickme",command = plotA(7)).pack()
main_page.mainloop()