import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1 - x/2 + x**5 + y**3)*np.exp(- x**2 - y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),10,alpha=0.75,cmap=plt.cm.hot) #画点

C = plt.contour(X,Y,f(X,Y),10,colors='black',linewidths=0.5) #画线

plt.clabel(C,inline=True,fontsize=10) #写上等高线数值

plt.xticks(())
plt.yticks(())

plt.show()