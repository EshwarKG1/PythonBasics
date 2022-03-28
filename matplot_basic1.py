from tkinter import *
import pandas as pd 

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk

data = pd.read_csv('plotting_parameters1.csv')

df = pd.DataFrame(data,columns=['HPC-1 RPM','HPC-2 RPM'])

top = Tk()

top.title("HPC RPM plotting")

top.geometry("500x500")

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

fig = Figure(figsize = (10,10),dpi = 100)

x1 = df.loc[:100,'HPC-1 RPM']
y1 = df.loc[:100,'HPC-2 RPM']
x2 = df.loc[101:,'HPC-1 RPM']
y2 = df.loc[101:,'HPC-2 RPM']

#x2 = df.loc[:,'HPC-1 RPM']
#y2 = df.loc[:,'HPC-2 RPM']

plot1 = fig.add_subplot(111)
plot1.set_xlabel('HPC-1 RPM')
plot1.set_ylabel('HPC-2 RPM')
plot1.set_title('HPC RPM')
plot1.scatter(x1,y1, label = 'First 100 values')
plot1.scatter(x2,y2, label = 'Remaining values')
plot1.legend(loc = 'lower right')

"""
plot2 = fig.add_subplot(312)
plot2.plot(x1,y1)

plot3 = fig.add_subplot(313)
plot3.plot(x2,y2)
"""

canavas = FigureCanvasTkAgg(fig,master=top)
canavas.draw()
canavas.get_tk_widget().pack()

"""
    toolbar = NavigationToolbar2Tk(canavas,top)
    toolbar.update()
    canavas.get_tk_widget().pack()
    plt_btn = Button(top,text="plot",height = 2,width = 4,command = Plot)

    plt_btn.pack()
"""

top.mainloop()