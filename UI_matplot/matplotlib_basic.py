from tkinter import *
import pandas as pd 

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk

data = pd.read_csv('plotting_parameters.csv')

df = pd.DataFrame(data,columns=['JS Status','JS X-Coord','JS Y-Coord','DAC X-value','DAC Y-value','HPC-1 RPM','HPC-2 RPM'])

top = Tk()

top.title("JS plotting")

top.geometry("500x500")

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

"""
m1 = Message(top,text="JS Coord").pack()

m2 = Message(top,text="DAC Value").pack()

m3 = Message(top,text="HPC RPM").pack()
"""

fig = Figure(figsize = (12,8),dpi = 100)

x = df.loc[:,'JS X-Coord']
y = df.loc[:,'JS Y-Coord']

x1 = df.loc[:,'DAC X-value']
y1 = df.loc[:,'DAC Y-value']

x2 = df.loc[:,'HPC-1 RPM']
y2 = df.loc[:,'HPC-2 RPM']

plot1 = fig.add_subplot(131)
plot1.set_xlabel('JS X-Coord')
plot1.set_ylabel('JS Y-Coord')
plot1.plot(x,y)
#plot1.legend(['blue'],loc = 'lower right')
plot1.set_title("JS Coord")

plot2 = fig.add_subplot(132)
plot2.set_xlabel('DAC X-value')
plot2.set_ylabel('DAC Y-value')
plot2.plot(x1,y1)
#plot2.legend(['blue'],loc = 'lower right')
plot2.set_title("DAC Values")

plot3 = fig.add_subplot(133)
plot3.set_xlabel('HPC-1 RPM')
plot3.set_ylabel('HPC-2 RPM')
plot3.scatter(x2,y2)
#plot3.legend(['blue'],loc = 'lower right')
plot3.set_title("HPC RPM")

fig.tight_layout()
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
