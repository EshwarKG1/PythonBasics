# Import the required modules needed
from tkinter import *
import pandas as pd 
import tkinter.messagebox
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk

# accessing the data using pandas
data = pd.read_csv('plotting_parameters.csv')

df = pd.DataFrame(data,columns=['JS Status','JS X-Coord','JS Y-Coord','DAC X-value','DAC Y-value','HPC-1 RPM','HPC-2 RPM'])

# main window 
top = Tk()

w = top.winfo_screenwidth()
h = top.winfo_screenheight()

top.title("JoyStick - DAC - RPM Motor")

top.geometry("%dx%d" % (w,h))

top.configure(bg ='white')

#top.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

"""   
    new = Toplevel(top)
    new.title("JS Plotting")
    new.geometry("%dx%d" % (w,h))
    new.configure(bg = 'white')
    
    new1 = Toplevel(top)
    new1.title("HPC Plotting")
    new1.configure(bg = 'white')
    new1.geometry("%dx%d" % (w,h))
    
    new2 = Toplevel(top)
    new2.title("JS vs RPM Plotting")
    new2.configure(bg = 'white')
    new2.geometry("%dx%d" % (w,h))
"""   


# JoyStick working with graphs 
def matplot_basic():
     
    fig = Figure(figsize = (9,6),dpi = 100)#, facecolor = 'grey')

    x = df.loc[:,'JS X-Coord']
    y = df.loc[:,'JS Y-Coord']

    x1 = df.loc[:,'DAC X-value']
    y1 = df.loc[:,'DAC Y-value']

    x2 = df.loc[:,'HPC-1 RPM']
    y2 = df.loc[:,'HPC-2 RPM']

    # plotting the graphs
    plot1 = fig.add_subplot(131)
    plot1.set_xlabel('JS X-Coord',font ='calibri', size = 15)
    plot1.set_ylabel('JS Y-Coord',font ='calibri', size = 15)
    plot1.plot(x,y,color = 'blue', linewidth=3)
    #plot1.legend(['blue'],loc = 'lower right')
    plot1.set_title("JS Coord",font ='calibri', size = 20)
    plot1.set_facecolor('grey')

    plot2 = fig.add_subplot(132)
    plot2.set_xlabel('DAC X-value',font ='calibri', size = 15)
    plot2.set_ylabel('DAC Y-value',font ='calibri', size = 15)
    plot2.plot(x1,y1,color = 'blue', linewidth=3)
    #plot2.legend(['blue'],loc = 'lower right')
    plot2.set_title("DAC Values",font ='calibri', size = 20)
    plot2.set_facecolor('grey')

    plot3 = fig.add_subplot(133)
    plot3.set_xlabel('HPC-1 RPM',font ='calibri', size = 15)
    plot3.set_ylabel('HPC-2 RPM',font ='calibri', size = 15)
    plot3.scatter(x2,y2,color = 'blue')
    #plot3.legend(['blue'],loc = 'lower right')
    plot3.set_title("HPC RPM",font ='calibri', size = 20)
    plot3.set_facecolor('grey')

    fig.tight_layout()
    canavas = FigureCanvasTkAgg(fig,master=top)
    canavas.draw()
    canavas.get_tk_widget().place(x = 410, y =50)

# HPC1 Vs HPC2 with spliting as first 100 and remaining.
def matplot_basic1():
    
    fig1 = Figure(figsize = (9,6),dpi = 100)#,facecolor = 'violet')

    x11 = df.loc[:100,'HPC-1 RPM']
    y11 = df.loc[:100,'HPC-2 RPM']
    x12 = df.loc[101:,'HPC-1 RPM']
    y12 = df.loc[101:,'HPC-2 RPM']
    
    # plotting the graph
    plot11 = fig1.add_subplot(111)
    plot11.set_xlabel('HPC-1 RPM',size = 20,font ='calibri')
    plot11.set_ylabel('HPC-2 RPM',size = 20,font ='calibri')
    plot11.set_title('HPC RPM Motors',size = 25,font ='calibri')
    plot11.set_ylim(ymin = 0, ymax = max(y12))
    plot11.set_xlim(xmin = 0, xmax = max(x12))
    plot11.scatter(x11,y11, label = 'First 100 values',color = 'red')
    plot11.scatter(x12,y12, label = 'Remaining values',color = 'blue')
    plot11.legend(loc = 'upper left')
    plot11.set_facecolor("grey")

    canavas1 = FigureCanvasTkAgg(fig1,master=top)
    canavas1.draw()
    canavas1.get_tk_widget().place(x = 410, y =50)

# JS-Y Vs HPC1 and HPC2 
def matplot_basic2():
    
    fig2 = Figure(figsize = (9,6),dpi = 100)#,facecolor = 'grey')

    y2 = df.loc[:,'JS Y-Coord']

    x22 = df.loc[:,'HPC-1 RPM']
    y22 = df.loc[:,'HPC-2 RPM']
    
    # plotting the graphs
    plot12 = fig2.add_subplot(111)
    plot12.set_ylabel('RPM',font ='calibri', size = 20)
    plot12.set_xlabel('JS Y-Coord',font ='calibri', size = 20)
    plot12.set_ylim(ymin = 0, ymax = max(y22))
    plot12.set_xlim(xmin = 0, xmax = max(y2))
    plot12.scatter(y2,x22,label = '1-RPM',color = 'red')
    plot12.scatter(y2,y22,label = '2-RPM',color = 'blue')
    plot12.legend(loc = 'upper left')
    plot12.set_title("JoyStick Y-Coord vs RPM Motor",font ='calibri', size = 25)
    plot12.set_facecolor("grey")

    fig2.tight_layout()
    canavas2 = FigureCanvasTkAgg(fig2,master=top)
    canavas2.draw()
    canavas2.get_tk_widget().place(x = 410, y =50)
    
def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        

# button to perform the respective works
btn1 = Button(top,text='Display the JS plotting',command=matplot_basic,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'grey', borderwidth = 0).place(x = 0, y = 90)

btn2 = Button(top,text='Display the RPM Split plotting',command=matplot_basic1,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'grey',borderwidth = 0).place(x = 0, y = 135)

btn3 = Button(top,text='Display the JS-Y vs RPM plotting',command=matplot_basic2,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'grey', borderwidth = 0).place(x = 0, y = 180)

btn4 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold'), borderwidth = 0).place(x=0,y=225)

top.mainloop()