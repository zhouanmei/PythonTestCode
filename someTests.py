import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

import matplotlib.pyplot as plt

plt.clf()  # 清空画布
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel("横轴",fontproperties=myfont)
plt.ylabel("纵轴",fontproperties=myfont)
plt.title("pythoner.com",fontproperties=myfont)
plt.legend(['图例'],prop=myfont)
plt.show()
