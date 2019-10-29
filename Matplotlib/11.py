import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 多坐标系组合图
# subplot2grid
# plt.figure()
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# ax1.set_title('ax1_title')
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
# ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
# ax4 = plt.subplot2grid((3,3),(2,0))
# ax5 = plt.subplot2grid((3,3),(2,1))

# gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:2])
# ax3 = plt.subplot(gs[1:,2])
# ax4 = plt.subplot(gs[-1,0])
# ax5 = plt.subplot(gs[-1,-2])

f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

plt.tight_layout()
plt.show()