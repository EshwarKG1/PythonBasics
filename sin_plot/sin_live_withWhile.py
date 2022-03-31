"""
# Geeksforgeeks code 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')

for phase in np.linspace(0, 10*np.pi, 100):
	line1.set_ydata(np.sin(0.5 * x + phase))
	fig.canvas.draw()
	fig.canvas.flush_events()

"""

import matplotlib.pyplot as plt
import math
import numpy as np

x_list = []
y_list = []
theta = 0
  
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
#line1, = ax.plot(x_list, y_list, 'b-')
  
while True :
    theta_in_radians = math.radians(theta)
    x = math.sin(theta_in_radians)
    x_list.append(theta)
    y_list.append(round(x,4))
    line1, = ax.plot(x_list, y_list, 'b-')
    line1.set_data(x_list,y_list)
    plt.pause(0.1)
    fig.canvas.draw()
    fig.canvas.flush_events()
    theta = theta + 1