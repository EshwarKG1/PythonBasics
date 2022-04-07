import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import time

main_page = Tk()

w = main_page.winfo_screenwidth()
h = main_page.winfo_screenheight()

main_page.title("Analog function")

main_page.geometry("%dx%d"% (w,h))

#main_page.configure(bg ='white')

#main_page.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

main_page.iconphoto(True,icon)

plt.style.use('seaborn')

fig = Figure(figsize=(13,5))
ax = fig.add_subplot(111)

ax.set_title("Analog Live-Plotting")
ax.set_ylabel('Analog values')
ax.set_xlabel('Time in seconds')

canavas = FigureCanvasTkAgg(fig,master=main_page)
canavas.get_tk_widget().place(x=40, y =40, width = 1200, height = 500)
canavas.draw()

values = []
x_values = []
isStarted = 1

try: 
    ser = serial.Serial('COM3',9600)
except serial.SerialException:
    print("please check the ADC connections")
    pass

def plot_graph():
    if isStarted == 1:
        start_time = time.time()
        while True:        
            try:
                line = ser.readline()
                string = line.decode()
                num = int(string)
                values.append(num)
                actual_time = time.time()-start_time
                x_values.append(actual_time) 
                line1, = ax.plot(x_values,values,'b-')
                line1.set_xdata(x_values)
                line1.set_ydata(values)
                canavas.flush_events()
                canavas.draw()
            except KeyboardInterrupt:
                exit()
    else:
        canavas.flush_events()

def start_plot():
    isStarted = 1
    plot_graph()
    
def stop_plot():
    isStarted = 0
    plot_graph()

def onClick():
    result = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if result == 'yes' :
        main_page.destroy()
        exit()


start_button = Button(main_page,text='Show the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: start_plot())
start_button.place(x = 200, y = 600)

stop_button = Button(main_page,text='Stop the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: stop_plot())
stop_button.place(x = 600, y = 600)

exit_button = Button(main_page,text="Exit",command = onClick, bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold'))
exit_button.place(x=1000,y=600)

main_page.mainloop()