# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

# 直线图
x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.show()