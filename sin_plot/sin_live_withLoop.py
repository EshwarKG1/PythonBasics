import matplotlib.pyplot as plt
import numpy as np
import math

# use ggplot style for more sophisticated visuals
#plt.style.use('ggplot')
try:
    def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.01):
        if line1==[]:
            # this is the call to matplotlib that allows dynamic plotting
            plt.ion()
            fig = plt.figure(figsize=(13,6))
            ax = fig.add_subplot(111)
            # create a variable for the line so we can later update it
            line1, = ax.plot(x_vec,y1_data)        
            #update plot label/title
            plt.ylabel('sin values')
            plt.xlabel('degree')
            plt.title('Sin function ')
            #ax.set_ylim(ymin = 0, ymax = max(y1_data))
            #ax.set_xlim(xmin = 0, xmax = max(x_vec))
            plt.show()
        
        # after the figure, axis, and line are created, we only need to update the y-data
        line1.set_data(x_vec,y1_data)
        plt.ylim(ymin = 0, ymax = max(y1_data))
        plt.xlim(xmin = 0, xmax = max(x_vec))
        # adjust limits if new data goes beyond bounds
        if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
           plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
        # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
        plt.pause(pause_time)
        
        # return line so we can update it again in the next iteration
        return line1

    theta = 0
    #size = 100
    x_vec = []
    y_vec = []
    line1 = []

    while True:
        theta_in_radians = math.radians(theta)
        rand_val = math.sin(theta_in_radians)
        x_vec.append(theta)
        y_vec.append(round(rand_val,4))
        line1 = live_plotter(x_vec,y_vec,line1)
        #y_vec = np.append(y_vec[1:],0.0)
        theta = theta + 1
        
except KeyboardInterrupt:
    print("program terminated")