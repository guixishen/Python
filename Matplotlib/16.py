from matplotlib import pyplot as plt
import numpy as np

# 多系列柱状图
plt.style.use('Solarize_Light2')
# plt.xkcd()

age_x = [25,26,27,28,29,30,31,32,33,34,35]

x_indexes = np.arange(len(age_x))
width = 0.25

dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.bar(x_indexes-width,dev_y,width=width,color='#338781',label='All Devs')

py_dev_y = [48496,52680,69752,56550,73265,66254,82156,74938,73947,78448,88752]
plt.bar(x_indexes,py_dev_y,width=width,color='#7a7a7a',label='Python')

js_dev_y = [42496,50000,51752,53320,60200,61000,70316,71928,73317,74748,80752]
plt.bar(x_indexes+width,js_dev_y,width=width,color='#3d3d79',label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.xticks(ticks=x_indexes,labels=age_x)

plt.grid(True)
plt.tight_layout()

plt.show()