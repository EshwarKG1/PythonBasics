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

top.geometry("%dx%d"% (w,h))

#top.configure(bg ='white')

#top.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

ser = serial.Serial('COM3',9600)
time.sleep(0.01)

values = []
x_values = []

global count

def live_function():
    count = 0
    if count == 0:
        plt.ion()
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        plt.style.use('seaborn')
        plt.ylabel('Analog values')
        plt.xlabel('Time in seconds')
        plt.title('Analog values vs Time')
        #plt.show()
        start_time = time.time()
        canavas = FigureCanvasTkAgg(fig,master=top)
        while True:
            line = ser.readline()
            if line:
                string = line.decode()
                num = int(string)
                #print(num)
                values.append(num)
                actual_time = time.time()-start_time
                x_values.append(actual_time)    
                line1, = ax.plot(x_values,values,'b-')
                line1.set_data(x_values,values)
                plt.pause(0.001)
                #canavas.draw()
                canavas.get_tk_widget().place(x=400, y =50)
                count = 1

def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        plt.close()
        exit()
        
btn = Button(top,text='Show the live plotting',command = live_function,height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange').place(x = 80, y = 80)
btn1 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold')).place(x=80,y=200)
top.mainloop()