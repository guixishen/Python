from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('Solarize_Light2')
plt.xkcd()

# 风格曲线图
age_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(age_x,dev_y,'b--',label='All Devs')

py_dev_y = [48496,52680,69752,56550,73265,66254,82156,74938,73947,78448,88752]
plt.plot(age_x,py_dev_y,'r',label='Python')

js_dev_y = [42496,50000,51752,53320,60200,61000,70316,71928,73317,74748,80752]
plt.plot(age_x,js_dev_y,color='#3d3d79',label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()

plt.grid(True)
plt.tight_layout()

# plt.savefig('plot.png')
plt.show()