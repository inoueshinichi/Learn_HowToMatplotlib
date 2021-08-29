import matplotlib.pyplot as plt
#plt.rcParams(['font.size']) = 14

import numpy as np
np.random.seed(123)  # 乱数種を指定
N = 100  # 100点のデータを生成
x = np.random.rand(N)
y = 2 * x + np.random.randn(N)
plt.scatter(x, y)
plt.title('sample plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


N1 = 50
plt.plot(0 + 0.3 * np.random.rand(N), c='r', marker='o', linestyle='-', label='1')
plt.plot(0.5 + 0.3 * np.random.rand(N1), c='b', marker='x', linestyle='--', label='2')
plt.plot(1 + 0.3 * np.random.rand(N1), c='g', marker='s', linestyle=':', label='3')
plt.xlim(-1, 51)
plt.ylim(0, 2.0)
plt.legend(loc='upper right', prop={'size':10})
plt.grid()
plt.show()


N3 = 100
np.random.seed(71)
x = np.random.rand(N3)
y = 2 * x + np.random.randn(N3)
c = np.random.rand(N3)
fig = plt.figure(figsize=(8, 6))
plt.subplot(221)
plt.scatter(x, y, c=c, cmap=plt.cm.Accent)
plt.title('Accent')
plt.colorbar()
plt.subplot(222)
plt.scatter(x, y, c=c, cmap=plt.cm.Greens)
plt.title('Greens')
plt.colorbar()
plt.subplot(223)
plt.scatter(x, y, c=c, cmap=plt.cm.jet)
plt.title('jet')
plt.colorbar()
plt.subplot(224)
plt.scatter(x, y, c=c, cmap=plt.cm.RdBu)
plt.title('RdBu')
plt.colorbar()
plt.subplots_adjust(hspace=0.35)
plt.show()


np.random.seed(123)
fig = plt.figure() # Figureクラスのインスタンス化
ax = fig.gca() # Axesクラスのインスタンス化
ax.plot(np.random.rand(100))
plt.show()


np.random.rand(123)
fig1, fig2 = plt.figure(1), plt.figure(2)
plt.figure(1) # Figure1を選択
plt.plot(np.random.rand(100))
plt.figure(2)
plt.scatter(np.random.rand(100), np.random.rand(100))
plt.show()


fig, ax = plt.subplots(2, 2, figsize=(10, 8))
N4 = 100
np.random.seed(123)
nrow, ncol = ax.shape
for i in range(nrow):
    for j in range(ncol):
        x = np.random.rand(N4)
        y = 2 * x + np.random.randn(N4)
        ax[i,j].scatter(x, y)
        ax[i,j].set_title('[' + str(i) + ',' + str(j) + ']')
plt.show()


np.random.seed(123)
N5 = 100
x = np.random.rand(N5)
y = np.random.rand(N5)
plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.scatter(x, y, marker='o')
plt.subplot(222)
plt.scatter(x, y, marker='x')
plt.subplot(223)
plt.scatter(x, y, marker='s')
plt.subplot(224)
plt.scatter(x, y, marker='^')
plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.show()


fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(x,y)
ax2 = fig.add_subplot(2,2,2)
ax2.scatter(x,y)
ax3 = fig.add_subplot(2,2,3)
ax3.scatter(x,y)
ax4 = fig.add_subplot(2,2,4)
ax4.scatter(x,y, marker='x')
plt.show()

