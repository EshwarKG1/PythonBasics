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

#top.geometry("%dx%d"% (w,h))

top.geometry("500x400")

#top.configure(bg ='white')

top.resizable(width=False,height=False)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

plt.style.use('seaborn')

values = []
x_values = []
isStarted = 1
start_flag = 1

global plot_count,plot_flag
plot_count = 1
plot_flag = 1

ser = serial.Serial('COM3',9600)

def stop_fun():

    start_flag = 1
    
    if isStarted == 1:
        return 1
    else:
        return 0

def on_closing():
    global plot_count
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        plot_count = 1
        newWindow.destroy()

def start_plot():

    global start_flag,isStop,isStarted,plot_count,plot_flag
    
    isStarted = 1
    
    
    if plot_count == 1 :
    
        newWindow = Toplevel(top)

        newWindow.title("Analog Reader")
        #newWindow.geometry("600x300")
        w = top.winfo_screenwidth()
        h = top.winfo_screenheight()

        newWindow.geometry("%dx%d"% (w,h))
        
        newWindow.protocol("WM_DELETE_WINDOW", on_closing)
        
        plot_count = 2
        plot_flag = 0

        #newWindow.resizable(width=False,height=False)

        if start_flag == 1 :
            
            fig = plt.figure(figsize=(13,5))
        
            ax = fig.add_subplot(111)

            ax.set_title("Analog Live-Plotting")
            ax.set_ylabel('Analog values')
            ax.set_xlabel('Time in seconds')
            
            canavas = FigureCanvasTkAgg(fig,master=newWindow)
            canavas.get_tk_widget().place(x=40, y =40)
            canavas.draw()
            canavas.flush_events()
            
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
                        #print(num)
                        
                        isStop = stop_fun()
                        #print(isStop)
                        
                        if isStop == 1:
                            #print(isStop)
                            line1, = ax.plot(x_values,values,'b-',linewidth = 1)
                            line1.set_xdata(x_values)
                            line1.set_ydata(values)
                            canavas.flush_events()
                            canavas.draw()
                        else:
                            plot_count = 3
                            break
                        
                except KeyboardInterrupt:
                    print("Closing")
                    plt.close("all")
                    ser.close()
                    break
        else:
            pass
    
    elif plot_count == 3:
        tkinter.messagebox.showinfo('Display message','It stopped running')
    
    elif plot_count == 2:
        tkinter.messagebox.showinfo('Display message','It is already running')

def stop_plot():

    global isStarted
    isStarted = 0
    

def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        exit()

top.update()
btn = Button(top,text='Show the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: start_plot())
btn.place(x = 80, y = 80)
top.update()
btn1 = Button(top,text='Stop the live plotting',height = 1,width = 30,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: stop_plot())
btn1.place(x = 80, y = 200)
btn2 = Button(top,text="Exit",command = onClick, bg='red',fg='white',height=1,width=30,font=('calibri',15,'bold'))
btn2.place(x=80,y=320)

top.mainloop()