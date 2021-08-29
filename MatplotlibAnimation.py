import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
np.random.seed(123)
x = np.random.randn(N)

absmax_x = np.ceil(np.max(np.abs(x)))
xmin, xmax = -absmax_x, absmax_x

def animate(nframe):
    plt.cla() # Axesオブジェクトのクリア
    plt.hist(x[:nframe], bins=20) # ヒストグラムの描画
    plt.xlim(xmin, xmax)
    plt.ylim(0, 100)
    plt.title('N=%s' % nframe)

fig = plt.figure()
# アニメーション関数のインスタンス化
# (Figureオブジェクト, 描画する関数, フレーム番号を指定)
anim = animation.FuncAnimation(fig, animate, np.arange(1, N+1))
anim.save('hist.gif', writer='imagemagick', fps=20)
plt.show()
