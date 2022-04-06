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
fig = Figure(figsize=(9,6))
ax = fig.add_subplot(111)

ax.set_title("Analog Live-Plotting")
ax.set_ylabel('Analog values')
ax.set_xlabel('Time in seconds')
ax.set_xlim(0,100)
ax.set_ylim(0,1000)
lines = ax.plot([],[])[0]

canavas = FigureCanvasTkAgg(fig,master=top)
canavas.get_tk_widget().place(x=450, y =70)
canavas.draw()

values = []
x_values = []
con = False

def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        exit()

ser = serial.Serial('COM3',9600)
ser.reset_input_buffer()

def plot_data():
    global con,x_values,values
    if (con==True):
        start_time = time.time()
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
            #print(num)
            values.append(num)
            actual_time = time.time()-start_time
            x_values.append(actual_time) 
            lines.set_xdata(x_values)
            lines.set_ydata(values)
            canavas.draw()
    top.after(1,plot_data)

def start_plot():
    global con 
    con = True
    ser.reset_input_buffer()
        
def stop_plot():
    global con 
    con = False


top.update()
btn = Button(top,text='Show the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: start_plot())
btn.place(x = 80, y = 80)
top.update()
btn1 = Button(top,text='Stop the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: stop_plot())
btn1.place(x = 80, y = 200)
btn2 = Button(top,text="Exit",command = onClick, bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold'))
btn2.place(x=80,y=320)

top.after(1,plot_data)
top.mainloop()