import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

import serial
import time 

ser = serial.Serial('COM3',9600)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

values = []

while True:
    try:
        def animate(i):
            line = ser.readline()
            if line:
                string = line.decode()
                num = int(string)
                print(num)
                values.append(num)
            ax.clear()
            ax.plot(values)
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('analog Function')
            plt.ylabel('analog values')
            plt.xlabel('time')
        ani = animation.FuncAnimation(fig, animate, interval=1)
        plt.show(block = True)
        
    except KeyboardInterrupt:
        print("terminating")
        plt.close()
        ser.close()
        break