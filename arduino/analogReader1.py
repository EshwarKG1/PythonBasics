import matplotlib.pyplot as plt
import serial
from tkinter import *
import tkinter.messagebox
import numpy as np

top = Tk()

w = top.winfo_screenwidth()
h = top.winfo_screenheight()

top.title("Analog function")

top.geometry("500x400")

#top.configure(bg ='white')

top.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

ser = serial.Serial('COM3',9600)

values = []

def live_plotter(y1_data,line1,pause_time=0.01):     
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1
 
def live_plotting():
    line1 = []
    # use ggplot style for more sophisticated visuals
    plt.style.use('ggplot')

    size = 100
    x_vec = np.linspace(0,10,size+1)[0:-1]
    y_vec = np.random.randn(len(x_vec))
    
    plt.ion()
    fig = plt.figure(figsize=(13,6))
    ax = fig.add_subplot(111)
    # create a variable for the line so we can later update it
    line1, = ax.plot(y_vec,'b-')        
    #update plot label/title
    plt.ylabel('Analog values')
    plt.xlabel('Time')
    plt.title('Analog values function')
    plt.show()

    while True:
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)       
            y_vec[-1] = num
            line1 = live_plotter(y_vec,line1)
            y_vec = np.append(y_vec[1:],0.0)
            
def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        plt.close('all')
        exit()        

btn = Button(top,text='Show the live plotting',command = live_plotting,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange').place(x = 80, y = 80)
btn1 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold')).place(x=80,y=250)
top.mainloop()