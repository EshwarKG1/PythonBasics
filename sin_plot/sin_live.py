import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

fig = plt.figure(figsize=(12,10))

ax = fig.add_subplot(1,1,1)
ax.set_title("Sin function Graph")
ax.set_xlabel("Degree values")
ax.set_ylabel("Sin value of respective degree")

def animate(i):
    # for the first 200 values
    data = pd.read_csv("sin1.txt")
    # for the 10,000 values
    #data = pd.read_csv("sin_plot.txt")
    # for the 1,00,000 values
    #data = pd.read_csv("sin_plot1.txt")
    df = pd.DataFrame(data,columns=["degrees","values"])
    
    xs = df.loc[:,"degrees"]
    ys = df.loc[:,"values"]
    
    ax.clear()
    ax.plot(xs,ys)
    ax.set_title("Sin function Graph")
    ax.set_xlabel("Degree values")
    ax.set_ylabel("Sin value of respective degree")
    
ani = animation.FuncAnimation(fig,animate, interval = 500)
plt.show()     