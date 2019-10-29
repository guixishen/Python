# encoding = utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 饼图
plt.style.use('Solarize_Light2')

slices = [23207,179984,247743]
labels = ['first industry','second industry','third industry']
explode = [0,0,0]

plt.pie(slices,labels=labels,explode=explode,shadow=False,startangle=120,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})

plt.title('Preliminary GDP Accounting Data of China in the First Half of 2019')
plt.tight_layout()
plt.show()
