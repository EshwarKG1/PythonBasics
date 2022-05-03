import threading
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


global channel_number,channel_number1,X,Y,flag
channel_number = 0
channel_number1 = 1

board_list = hat_list(filter_by_id = HatIDs.ANY)
if board_list[0].id == HatIDs.MCC_118:
    board = mcc118(board_list[0].address)

Y = []
X = []
flag = 0

def values_read():
    Y_read = board.a_in_read(0)
    return (Y_read)

        
def values_plot():
   global flag 
   figure = Figure(figsize=(15, 10))
   figure.patch.set_facecolor('#ECF0F1')  # The region our side plot get a different color
   subplot = figure.subplots()
   subplot.set_facecolor("#000001") # Region inside the plot      
   subplot.grid()
   canvas = FigureCanvasTkAgg(figure, master=main_page)
   subplot.set_title("Graph  A")
   canvas.draw()
   canvas.get_tk_widget().pack(side=TOP)
   
   start_time = time.time()
   while True:
       actual_time = time.time()-start_time
       X.append(actual_time)
       Y.append(values_read())
       subPlotHandle, = subplot.plot(X,Y, color='#FF6700')
       subPlotHandle.set_data(X,Y)

       canvas.draw()
       canvas.flush_events()
       
values_thread = threading.Thread(target=values_read)
plotting_thread = threading.Thread(target=values_plot)

values_thread.start()
plotting_thread.start()

main_page.mainloop()
