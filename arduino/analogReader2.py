import serial
import time 
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

top = Tk()

w = top.winfo_screenwidth()
h = top.winfo_screenheight()

top.title("Analog function")

top.geometry("500x400")

#top.configure(bg ='white')

#top.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

ser = serial.Serial('COM3',9600)
time.sleep(2)

values = []

plt.ion()
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
plt.style.use('ggplot')
global count

def live_function():
    count = 0
    if count == 0:
        while True:
            line = ser.readline()
            if line:
                string = line.decode()
                num = int(string)
                #print(num)
                values.append(num)
                
                line1, = ax.plot(values,'b-')
                line1.set_ydata(values)
                plt.ylabel('Analog values')
                plt.xlabel('Time')
                plt.title('Analog values vs Time')
                #plt.show()
                #plt.pause(0.01)
                fig.canvas.draw()
                fig.canvas.flush_events()
                count = 1 

def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        #top.destroy()
        plt.close()
        #exit()
        
btn = Button(top,text='Show the live plotting',command = live_function,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'grey', borderwidth = 0).place(x = 80, y = 80)
btn1 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold')).place(x=80,y=250)
top.mainloop()