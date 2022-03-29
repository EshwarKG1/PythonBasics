from tkinter import *
import pandas as pd 

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

data = pd.read_csv('plotting_parameters.csv')

df = pd.DataFrame(data,columns=['JS Status','JS X-Coord','JS Y-Coord','DAC X-value','DAC Y-value','HPC-1 RPM','HPC-2 RPM'])

top = Tk()

top.title("JS vs RPM plotting")

top.geometry("500x500")

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

fig = Figure(figsize = (12,8),dpi = 100)

y = df.loc[:,'JS Y-Coord']

x2 = df.loc[:,'HPC-1 RPM']
y2 = df.loc[:,'HPC-2 RPM']

plot1 = fig.add_subplot(111)
plot1.set_ylabel('RPM')
plot1.set_xlabel('JS Y-Coord')
plot1.scatter(y,x2,label = '1-RPM')
plot1.scatter(y,y2,label = '2-RPM')
plot1.legend(loc = 'lower right')
plot1.set_title("JS vs RPM")

fig.tight_layout()
canavas = FigureCanvasTkAgg(fig,master=top)
canavas.draw()
canavas.get_tk_widget().pack()

top.mainloop()