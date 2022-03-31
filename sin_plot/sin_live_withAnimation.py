import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

theta = 0

# This function is called periodically from FuncAnimation
def animate(i):
    global theta
   
    theta_in_radians = math.radians(theta)
    x = math.sin(theta_in_radians)

    xs.append(theta)
    ys.append(round(x,4))

    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Sin Function')
    plt.ylabel('Sin values')
    plt.xlabel('degrees')
    theta = theta+1

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
