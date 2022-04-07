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

plt.style.use('seaborn')

# create a plot object 
fig = plt.figure(figsize=(13,5))
ax = fig.add_subplot(111)

ax.set_title("Analog Live-Plotting")
ax.set_ylabel('Analog values')
ax.set_xlabel('Time in seconds')

canavas = FigureCanvasTkAgg(fig,master=top)
canavas.get_tk_widget().place(x=40, y =40)
canavas.draw()

values = []
x_values = []

ser = serial.Serial('COM3',9600)

def start_plot():
    
    canavas.get_tk_widget().pack_forget()
    start_time = time.time()
    while True:
        try:
            line = ser.readline()
            if line:
                string = line.decode()
                num = int(string)
                values.append(num)
                actual_time = time.time()-start_time
                x_values.append(actual_time) 
                line1, = ax.plot(x_values,values,'b-')
                
                line1.set_xdata(x_values)
                line1.set_ydata(values)
                
                canavas.draw()
                canavas.flush_events()
                
        except KeyboardInterrupt:
            print("Closing")
            plt.close("all")
            ser.close()
            break
    
        
def stop_plot():

    time.sleep(5)

def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        exit()

top.update()
btn = Button(top,text='Show the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: start_plot())
btn.place(x = 200, y = 600)
top.update()
btn1 = Button(top,text='Stop the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: stop_plot())
btn1.place(x = 600, y = 600)
btn2 = Button(top,text="Exit",command = onClick, bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold'))
btn2.place(x=1000,y=600)

top.mainloop()