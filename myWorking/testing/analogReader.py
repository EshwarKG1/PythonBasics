import matplotlib.pyplot as plt
import time
import serial
from tkinter import *
from matplotlib.figure import Figure
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

main_page = Tk()
main_page.title("Analog function")
main_page.geometry("500x400")
main_page.resizable(width = False,height = False)

values = []
x_values = []
isStarted = 1
start_flag = 1

global plot_count,plot_flag
plot_count = 1
plot_flag = 1

def stop_fun():
    start_flag = 1   
    if isStarted == 1:
        return 1
    else:
        return 0

def start_plot():
    global start_flag,isStop,isStarted,plot_count,plot_flag
    values = []
    x_values = []
    isStarted = 1
    if plot_count == 1 :
        newWindow = Toplevel(main_page)
        newWindow.title("Analog Reader")
        #newWindow.geometry("600x300")
        #w = main_page.winfo_screenwidth()
        #h = main_page.winfo_screenheight()
        newWindow.geometry("800x600")
        try: 
            ser = serial.Serial('/dev/ttyUSB0',9600)
        except serial.SerialException:
            print("please check the ADC connections")
            pass

        def on_closing():
            global plot_count
            if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
                plot_count = 1
                #canavas.flush_events()
                #plt.figure().clear()
                ax.clear()
                newWindow.destroy()
        
        newWindow.protocol("WM_DELETE_WINDOW", on_closing)
        plot_count = 2
        plot_flag = 0
        #newWindow.resizable(width=False,height=False)
        if start_flag == 1 :
            fig = plt.figure(figsize=(8,4))
            ax = fig.add_subplot(111)
            #ax.clear()
            #plt.figure().clear()
            ax.set_title("Analog Live-Plotting")
            ax.set_ylabel('Analog values')
            ax.set_xlabel('Time in seconds')
            
            canavas = FigureCanvasTkAgg(fig,master=newWindow)
            #canavas.get_tk_widget().pack_forget()
            canavas.get_tk_widget().place(x=10, y =40)
            #canavas.flush_events()
            canavas.draw()
            
            #canavas.get_tk_widget().pack_forget()
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
                            canavas.draw()
                            canavas.flush_events()  
                        else:
                            plot_count = 3
                            ser.close()
                            break
                        
                except KeyboardInterrupt:
                    print("Closing")
                    plt.close("all")
                    ser.close()
                    break
        else:
            pass
        
    elif plot_count == 3:
        tkinter.messagebox.showinfo('DisplayInfo','It stopped running')
    
    elif plot_count == 2:
        tkinter.messagebox.showinfo('DisplayInfo','It is already running')
    
def stop_plot():
    global isStarted
    isStarted = 0
    
def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        main_page.destroy()
        exit()

main_page.update()
start_button = Button(main_page,text='Show the live plotting',height = 1,width = 25,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: start_plot())
start_button.place(x = 70, y = 80)
main_page.update()
stop_button = Button(main_page,text='Stop the live plotting',height = 1,width = 25,font = ('calibri',15,'bold'), fg = 'white', bg = 'orange',command = lambda: stop_plot())
stop_button.place(x = 70, y = 200)
exit_button = Button(main_page,text="Exit",command = onClick, bg='red',fg='white',height=1,width=25,font=('calibri',15,'bold'))
exit_button.place(x=70,y=320)

main_page.mainloop()