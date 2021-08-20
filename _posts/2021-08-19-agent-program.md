---
layout:     post
title:      南京大学2021春季：智能系统设计与应用
subtitle:   实验报告
date:       2021-08-19
author:     Welt Xing
header-img: img/Agent/prog.jpg
catalog:    true
tags:
    - 强化学习
---

## 前言

本文是对《智能系统设计与应用》三次编程作业中所涉及的知识点介绍，以及编程想法的记录.

## 第一次作业：栅格世界的决策算法

### 实验目的

在$10\times10$的栅格世界中，分别应用值迭代，高斯-赛德尔值迭代和策略迭代算法，使得$\text{Agent}$在这个栅格世界的每一个格子（也就是一个状态）都能获取到状态效用并找到最优决策$\pi^\star(s)$.

### 关于栅格世界

栅格世界如下图所示：

![grid](/img/Agent/grid.png)

我们用$(x,y)$表示$\text{Agent}$位于栅格世界的第$x$行第$y$列，在这个世界中，有如下的规则：

1. 无论$\text{Agent}$在哪个格子，都可以向上、下、左、右移动；
2. 行动的效果是随机的，朝指定方向移动的概率为$0.7$，朝其余3个方向移动的概率各为$0.1$；
3. 如果与墙碰撞，则原地不动，且受到1的惩罚；
4. 进入指定格子（$(x,y)=(8,9),(x,y)=(3,8)$）后执行任意行动的奖赏分别为$+10,+3$,随后行动终止；
5. 进入指定格子（$(x,y)=(5,4),(x,y)=(8,4)$）后执行任一行动的奖赏分别为$-5,-10$.

每一个格子$(x,y)$，都有一个最佳行动**集合**和一个效用值，分别表示能够使后继状态的期望效用最大的行动集合，该状态的立即回报加上在下一个状态的期望折扣效用值.

最佳集合的定义：

$$
\pi^\star(s)=\mathop{\arg\max}\limits_{a\in\mathcal{A}(s)}\sum_{s'}P(s'\vert s,a)U(s')
$$

最佳行动集合便是$\pi^\star(s)$的集合，状态$s$的效用值定义：

$$
U(s)=\max_{a\in\mathcal{A}(s)}\big(R(s,a)+\gamma\sum_{s'}P(s'\vert s,a)U(s')\big)
$$

上式称作**贝尔曼最优方程**。 我们接下来的工作主要就是围绕上面的公式进行.

### 价值迭代算法

以我们的栅格世界为例，只要能够获取到每个格子对应的效用值，$\text{Agent}$的行动便被我们完全理解；但实际上，贝尔曼方程告诉我们，如果有$n$个可能的状态，就有$n$个贝尔曼方程，我们这里就是$100$个. 此外，贝尔曼方程因为$\max$算符的存在而成为非线性方程。我们的想法是用迭代法，从**任意**的初始效用值开始，算出方程的右边，再把它代入到左边，第$i$次迭代就是下面的操作：

$$
U_{i+1}(s)\gets \max_{a\in\mathcal{A}(s)}\big(R(s,a)+\gamma\sum_{s'}P(s'\vert s,a)U_i(s')\big)
$$

理论上（这里略去证明），不断的迭代会使得状态的效用值达到均衡，而且一定是贝尔曼方程组的唯一解，对应的策略也是最优的. 我们将上面的算法提炼成伪代码：

$$
\begin{aligned}
&\textbf{function }\text{VALUE-ITERATION}(mdp,\epsilon)\textbf{ returns }\text{a utility function}\\
&\quad\textbf{inputs}:mdp,\text{an MDP with states }s,\text{actions }A(s),\text{trainsition model }P(s'\vert s,a),\\&\qquad\qquad\qquad\text{rewards }R(s),\text{discount }\gamma.\\
&\quad\;\quad\qquad\quad\epsilon,\text{the maximum error allowed in the utility of any state}\\
&\quad\textbf{local variables}:U,U',\text{vectors of utilities for states in }S,\text{initially zero}\\&\qquad\qquad\qquad\qquad\quad\delta,\text{the maximum change in the utility of any state in an iteration}\\
&\quad\textbf{repeat}\\
&\qquad U\gets U';\delta\gets0\\
&\qquad\textbf{for each }\text{state }s\textbf{ in }S\textbf{ do}\\
&\qquad\quad U'[s]\gets\max_{a\in\mathcal{A}(s)}\big(R(s,a)+\gamma\sum_{s'}P(s'\vert s,a)U[s']\big)\\
&\qquad\quad\textbf{if }\vert U'[s]-U[s]\vert\gt\delta\textbf{ then }\delta\gets\vert U'[s]-U[s]\vert\\
&\quad\textbf{until }\delta\lt\dfrac{\epsilon(1-\gamma)}{\gamma}\\
&\textbf{return }U
\end{aligned}
$$

### 高斯-赛德尔价值迭代

上面的价值迭代算法是在每一轮迭代中，基于$U_k$，对所有状态计算$U_{k+1}$. 我们在这里提出异步值迭代：在每一轮迭代中，仅更新状态空间的**一个子集**。算法的框架与价值迭代相同，修改下细节即可：

$$
\begin{aligned}
&\textbf{function }\text{GAUSS-SEIDEL-ITERATION}(mdp,\epsilon)\textbf{ returns }\text{a utility function}\\
&\quad\textbf{inputs}:mdp,\text{an MDP with states }s,\text{actions }A(s),\text{trainsition model }P(s'\vert s,a),\\&\qquad\qquad\qquad\text{rewards }R(s),\text{discount }\gamma.\\
&\quad\;\quad\qquad\quad\epsilon,\text{the maximum error allowed in the utility of any state}\\
&\quad\textbf{local variables}:U,\text{vectors of utilities for states in }S,\text{initially zero}\\&\qquad\qquad\qquad\qquad\quad\delta,\text{the maximum change in the utility of any state in an iteration}\\
&\quad\textbf{repeat}\\
&\qquad \delta\gets0\\
&\qquad\textbf{for each }\text{state }s\textbf{ in }S\textbf{ do}\\
&\qquad\quad u\gets U[s]\\
&\qquad\quad U[s]\gets\max_{a\in\mathcal{A}(s)}\big(R(s,a)+\gamma\sum_{s'}P(s'\vert s,a)U[s']\big)\\
&\qquad\quad\textbf{if }\vert u-U[s]\vert\gt\delta\textbf{ then }\delta\gets\vert u-U[s]\vert\\
&\quad\textbf{until }\delta\lt\dfrac{\epsilon(1-\gamma)}{\gamma}\\
&\textbf{return }U
\end{aligned}
$$

注意到我们在遍历状态的同时改变状态的效用值，并且运用到下一个状态的效用值计算中.

### 策略迭代

我们发现，即使在效用函数估计不准确的情况下，仍有可能得到最优策略，如果前一个行动比其他所有行动都要好，那么涉及效用的计算不需要太准确，这一简介暗示除了价值迭代还存在另一种找到最优策略的方法，也就是策略迭代：

![policy_iteration](/img/Agent/policy_iter.png)
策略迭代就是策略评估和策略提升的迭代</center>

我们将上面的想法形式化为伪代码：

$$
\begin{aligned}
&\textbf{function }\text{POLICY-ITERATION}(mdp,\epsilon)\textbf{ returns }\text{a policy}\\
&\quad\textbf{inputs}:mdp,\text{an MDP with states }s,\text{actions }A(s),\text{trainsition model }P(s'\vert s,a),\\&\qquad\qquad\qquad\text{rewards }R(s),\text{discount }\gamma.\\
&\quad\textbf{local variables}:U,\text{vectors of utilities for states in }S,\text{initially zero}\\
&\qquad\qquad\qquad\qquad\quad\pi,\text{a policy vector indexed by state,initially random}\\
&\quad\textbf{repeat}\\
&\qquad U\gets\text{POLICY-EVALUATION}(\pi,U,mdp) \\
&\qquad unchanged\gets\text{True}\\
&\qquad\textbf{for each }\text{state }s\textbf{ in }S\textbf{ do}\\
&\qquad\quad\textbf{if } R(s,\pi[s])+\gamma\sum_{s'}P(s'\vert s,a)U[s']\lt\max_{a\in\mathcal{A}(s)}\big(R(s,\pi[s])+\gamma\sum_{s'}P(s'\vert s,\pi[s])U[s']\big)\\
&\qquad\qquad\pi[s]\gets\mathop{\arg\max}\limits_{a\in\mathcal{A}(s)}\big(R(s,a)+\gamma\sum_{s'}P(s'\vert s,a)U[s']\big)\\
&\qquad\qquad unchanged\gets\text{False}\\
&\quad\textbf{until }unchanged\\
\end{aligned}
$$

注意到这里循环终止的条件是策略相关，即只要策略不再变化，我们就停止迭代，但并不代表效用值函数收敛，我们会在后面看到这一论断是正确的.

### 程序框架的构建

在了解了同步值迭代、异步值迭代和策略迭代算法后，我们便可以着手用$\text{Python}$模拟这三种算法。首先我们建立算法的框架. 我们定义一个栅格世界类`GridWorld`，然后三种算法就是`GridWorld`类对象的方法，当我们使用迭代时，我们只需要调用方法即可：

```python
world = GridWorld()
world.value_iteration(0.9, 0.01) # 参数分别是γ和ε
world.gauss_seidel_iteration(0.9, 0.01)
world.policy_iteration(0.9)
```

为了观察到迭代结果，我们还提供了一些接口：用于输出效用值的`display`方法，将效用值用热力图可视化的`plot`方法，以及输出最优策略的`display_action`方法.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class GridWorld:
    def __init__(self):
        '''
        初始化栅格世界
        '''
        self.world = np.zeros((10, 10)) # 效用值表
    
    def display(self):
        '''
        将栅格世界的效用值情况输出
        '''
        for i in range(10):
            for j in range(10):
                print("%7.2f" % self.world[i][j], end='')
            print('\n')

    def plot(self, cmd=False):
        '''
        用热力图将栅格世界的情况绘制出来
        '''
        sns.heatmap(self.world)
        plt.xticks([])
        plt.yticks([])
        plt.show()

    def display_action(self):
        '''
        将最优策略可视化
        '''
        dir_map = ["↑", "↓", "←", "→"]
        for x in range(10):
            for y in range(10):
                print("%s   " % dir_map[self.policy[x][y]], end='')
            print('\n')

    def clear(self):
        '''
        将栅格世界的值清零
        '''
        self.world = np.zeros((10, 10))

    def value_iteration(self, gamma, epsilon):
        iteration_times = 0
        while True:
            ...
        return iteration_times

    def gauss_seidel_iteration(self, gamma, epsilon):
        iteration_times = 0
        while True:
            ...
        return iteration_times
    
    def policy_iteration(self, gamma, epsilon):
        iteration_times = 0
        while True:
            ...
        return iteration_times

    def __reward(self, x, y, a):
        '''
        返回Agent在(x, y)格子做出a动作的奖赏
        x : [0, 9];
        y : [0, 9];
        a : [0, 1, 2, 3], 分别表示上、下、左、右
        '''
        # 分情况讨论即可：边界，红色栅格，绿色栅格，其他

    def __next_position(self, x, y, a):
        '''
        返回(x, y)按照a动作移动后的坐标(x', y')
        '''
        # 分情况讨论即可：边界，红色栅格，绿色栅格，其他
```

### 值迭代算法的实现

为了节省篇幅，这里我们只介绍价值迭代的实现，两种值迭代算法只有两三行代码的差别.

```python
def value_iteration(self, gamma, epsilon):
    iteration_times = 0
    while True:
        delta = 0
        new_world = np.zeros((10, 10))
        utility_list = [0] * 4  # 四个方向的期望效用
        for x in range(10):
            for y in range(10):
                old_utility = self.world[x, y]
                if (x, y) == (7, 8):
                    new_world[x, y] = 10
                elif (x, y) == (2, 7):
                    new_world[x, y] = 3
                else:
                    for a in range(4):
                        other_action = list(range(4))
                        other_action.remove(a)  # 不确定性导致的其他动作
                        r = 0.1 * sum([
                            self.__reward(x, y, action)
                            for action in other_action
                        ]) + 0.7 * self.__reward(x, y, a)  # 期望奖赏
                        u = 0.1 * sum(self.world[new] for new in [
                            self.__next_position(x, y, action)
                            for action in other_action
                        ]) + 0.7 * self.world[self.__next_position(
                            x, y, a)]
                        utility_list[a] = r + gamma * u
                    new_world[x][y] = max(utility_list)
                distance = abs(old_utility - new_world[x, y])
                if distance > delta:
                    delta = distance
        self.world = new_world
        if delta < epsilon * (1 - gamma) / gamma:
            break
        iteration_times += 1
    return iteration_times
```

这里`r`和`u`的计算是算法的核心，用于计算状态期望效用：`utility = r + gamma * u`. 我们在遍历时规定，如果遇到绿色栅格，直接将效用值赋为对应奖赏，对应到达绿色栅格便停止行动的规则. 高斯赛德尔迭代的程序结构和上面相同，唯一的不同是什么时候将旧的效用替换成新的期望效用. 我们来看看两种迭代算法的结果，运行：

```python
world = GridWorld()
times = world.value_iteration(0.9, 0.01)
world.display()
```

输出：

```python
   0.41   0.74   0.96   1.18   1.43   1.71   1.98   2.11   2.39   2.09

   0.73   1.04   1.27   1.52   1.81   2.15   2.47   2.58   3.02   2.69

   0.86   1.18   1.45   1.76   2.15   2.55   2.97   3.00   3.69   3.32

   0.84   1.11   1.31   1.55   2.45   3.01   3.56   4.10   4.53   4.04

   0.91   1.20   1.08  -3.00   2.48   3.53   4.21   4.93   5.50   4.88

   1.10   1.46   1.79   2.24   3.42   4.20   4.97   5.85   6.68   5.84

   1.06   1.41   1.70   2.14   3.89   4.90   5.85   6.92   8.15   6.94

   0.92   1.18   0.70  -7.39   3.43   5.39   6.67   8.15  10.00   8.19

   1.09   1.45   1.75   2.18   3.89   4.88   5.84   6.92   8.15   6.94

   1.07   1.56   2.05   2.65   3.38   4.11   4.92   5.83   6.68   5.82
```

我们将这里的效用可视化：

![heat](/img/Agent/value_iter_heat.svg)

这里的实验效果和讲义上的结果完全一致. 我们再看看价值迭代算法的迭代次数：

```python
>>> print(times)
38
```

运行高斯赛德尔迭代，观察迭代次数：

```python
>>> world.clear()
>>> times = world.gauss_seidel_iteration(0.9, 0.01)
>>> print(times)
28
```

在验证两种迭代算法的结果相同后，我们还发现异步迭代次数确实明显小于同步迭代.

### 策略迭代的算法实现

不同于价值迭代的全部尝试，策略迭代在每个栅格里只需要按照给定的策略计算一次期望效用即可：

```python
class GridWorld:
    ...
    def policy_iteration(self, gamma, epsilon):
        # 随机初始化策略
        self.policy = np.random.randint(4, size=(10, 10))
        iteration_times = 0
        while True:
            delta = 0
            Uk = np.zeros((10, 10))
            # 计算Uk
            for x in range(10):
                for y in range(10):
                    if (x, y) == (7, 8):
                        Uk[x, y] = 10
                    elif (x, y) == (2, 7):
                        Uk[x, y] = 3
                    else:
                        # 计算指定策略的期望效用
                    distance = abs(self.world[x][y] - Uk[x][y])
                    if distance > delta:
                        delta = distance
            # 更新策略
            new_policy = np.zeros((10, 10))
            same_policy = True
            for x in range(10):
                for y in range(10):
                    utility_list = [
                        Uk[self.__next_position(x, y, a)] for a in range(4)
                    ]
                    new_policy[x][y] = utility_list.index(max(utility_list))
                    if new_policy[x][y] != self.policy[x][y]:
                        same_policy = False
                    self.policy[x][y] = new_policy[x][y]
            self.world = Uk
            if same_policy: 
                # 终止条件1：策略收敛
                break
            if delta < epsilon * (1 - gamma) / gamma: 
                # 终止条件2：效用收敛
                break
            iteration_times += 1
        return iteration_times
```

注意到我们这里还是加入了$\delta,\epsilon$，这是为了观察两种迭代终止条件的区别，根据我们之前提到的，“即使在效用函数估计不准确的情况下，仍有可能得到最优策略”，所以我们的终止条件1必然早于终止条件2，当我们将终止条件1注释掉后，运行策略迭代得到的效用正是值迭代得到的效用，而且迭代次数也是38，而我们采用终止条件1时，效用值是下面这样：

```python
   0.01   0.38   0.59   0.85   1.09   1.39   1.69   1.99   2.16   1.81

   0.37   0.66   0.93   1.17   1.48   1.79   2.24   2.51   2.86   2.48

   0.41   0.79   1.03   1.40   1.77   2.27   2.72   3.00   3.57   3.20

   0.31   0.55   0.87   1.10   2.16   2.72   3.40   3.99   4.46   3.97

   0.15   0.60   0.47  -3.34   2.16   3.36   4.07   4.87   5.45   4.84

   0.46   0.81   1.40   1.88   3.24   4.05   4.91   5.81   6.66   5.82

   0.33   0.92   1.26   1.93   3.73   4.83   5.80   6.91   8.14   6.94

   0.21   0.47   0.26  -7.64   3.33   5.32   6.65   8.14  10.00   8.18

   0.34   0.93   1.33   1.97   3.74   4.82   5.80   6.90   8.14   6.93

   0.35   0.96   1.65   2.37   3.22   4.01   4.86   5.80   6.67   5.81
```

我们调用`display_action`方法来观察两种终止条件下的策略，发现最优策略是相同的：

```text
→    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    ↓    

→    →    →    →    →    ↓    ↓    ↓    ↓    ↓    

→    →    →    →    →    ↓    ↓    ↓    ↓    ↓    

→    →    →    →    →    →    ↓    ↓    ↓    ↓    

→    ↓    ↓    →    →    →    ↓    ↓    ↓    ↓    

→    →    →    →    →    →    →    ↓    ↓    ↓    

→    →    →    →    →    →    →    →    ↓    ↓    

→    ↓    ↓    →    →    →    →    →    →    ←    

→    →    →    →    →    →    →    →    ↑    ↑    

→    →    →    →    →    →    ↑    ↑    ↑    ↑  
```

而策略收敛只需要迭代**14**次，由于两种值迭代算法，启发我们只需要求解最优策略时可以选择更快的策略迭代.

> 我们或许可以断言，值迭代只有在前期才会有策略的改变，之后则是效用值的收敛.

### 结语

至此我们已经用`Python`实现了价值迭代和策略迭代，虽然刚入手的时候觉得难度很大，但只要解决了其中一个任务，后面的任务只是程序框架中一些细节的改动. 这次程序作业也加深我对强化学习的认识（相比于上学期只是了解一些术语），相比于朴素的样本学习，强化学习不需要带标签的输入输出对，同时也无需对非最优解的精确地纠正。这是最令我惊叹的地方。

## 第二次作业：用蒙特卡罗搜索树玩2048

### 引言

我们尝试用蒙特卡洛树搜索方法设计和实现会玩2048游戏的智能程序。要求程序每1秒执行一个行动，并可视化智能程序玩2048游戏的过程。

> 2048游戏使用方向键让方块整体上下左右移动。如果两个带有相同数字的方块在移动中碰撞，则它们会合并为一个方块，且所带数字变为两者之和。每次移动时，会有一个值为2或者4的新方块出现，所出现的数字都是2的幂。当值为2048的方块出现时，游戏即胜利，该游戏因此得名。             ——[Wikipedia](https://en.wikipedia.org/wiki/2048_(video_game))

### 平台介绍

本实验程序于$\text{Ubuntu}20.04$上运行，实验代码所依赖的第三方$\text{Python}$库已经在`requirements.txt`文件中声明：

```python
# 获取代码后运行 pip install -r requirements.txt 以安装第三方库
gym
numpy
PyQt5
```

### 解读框架

我们拿到的文件（`game2048.py`）是一个随机决策的2048游戏框架：

```python
class Game2048Env(gym.Env):
    '''模拟2048游戏的内部逻辑，包括开始，移动，结束'''
    def __init__(self, render: bool = True):
        pass
	# ....
    
class Game2048GUI(QMainWindow):
    '''模拟游戏的外部逻辑，属于GUI内容，不需要我们修改'''
    def __init__(self, port, remote_port):
		pass
    # .....
    
if __name__ == '__main__':
    env = Game2048Env(True)
    env.seed(0)
    # render is automatically set to False for copied envs
    test_env = copy.deepcopy(env)
    test_env.setRender(True)
    # remember to call reset() before calling step()
    obs = env.reset()
    done = False
    while not done:
        # 每过0.2秒便在上下左右四个方向中随机选择一个作为action
        time.sleep(0.2)
        action = random.randint(0, 3)
        obs, rew, done, info = env.step(action)
        print(rew, done, info)
    env.close()
    test_env.setRender(False)
    test_env.close()
```

我们也可以删掉等待时间，手动输入`action`，自己去玩游戏；但我们的实验任务是让$\text{Agent}$根据现在的状态，选择出最优的`action`：

```python
action = Agent(env)
```

这里我们采用的是$\mathbb{UCT}$，也就是基于蒙特卡洛树搜索$(\text{MCTS})$和上置信界$\text{UCB}$的上置信区间搜索.

### $\mathbb{UCT}$算法相关

我们先来看看上置信区间搜索的前身：蒙特卡洛树搜索。它是$\text{Rémi Coulom}$在 2006 年于它的围棋人机对战引擎 「Crazy Stone」中首次发明并使用的的 ，并且取得了很好的效果。

这些树搜索算法其实和人类的思考方式有相似之处：当人在对弈或是玩2048这种游戏时，会根据感觉在大脑里大致筛选处几种**最可能**的走法，这其实就是MCTS算法的设计思路。

算法在有限的时间里（对弈时每一步都会有限制时间），不断进行下面的循环：

$$
\text{选择}\to\text{扩展}\to\text{仿真}\to\text{反向更新}
$$

> 在搜索树算法中，每一个节点都是游戏的一个状态，节点$a$与节点$b$之间的边表示从状态$a$到状态$b$的一个行动$action$.

![mct](https://i.stack.imgur.com/EieiQ.png)

#### 选择

算法从根节点（对弈/游戏的某一状态）开始，在搜索树$T$（初始为$\emptyset$）向下搜索，直到到达一个节点$s$满足$s\notin T$；在上述过程中，我们需要确定一个选择分支的准则，在$\mathbb{UCT}$中，我们采用的是上置信界作为判断依据：

$$
a\gets\mathop{\arg\max}\limits_{a\in\mathcal{A}(s)}\bigg(Q(s,a)+c\sqrt{\dfrac{\log N(s)}{N(s,a)}}\bigg)
$$

这里的$Q(s,a)$是在$s$状态选择$a$行动获得的收益，$N(s)$是我们在有限时间的树搜索里到达$s$节点的次数，类似的，$N(s,a)$就是选择$a$行动到达$s(a)$的次数：

$$
N(s)=\sum_{a\in\mathcal{A}(s)}N(s,a)
$$

一方面，我们希望在遍历搜索树时倾向于奖赏$Q(s,a)$更大的分支；另一方面，我们希望探索那些不常去的地方，常数$c$便是用来控制对$\text{exploitation}$和$\text{exploration}$，也就是“利用”和“探索”之间的权衡.

#### 扩展

上面的选择过程遇到一个不属于搜索树的节点便停止，原因是我们无法获取这个这个节点的信息，也就是无法根据上置信界判断最优行动；缺什么补什么，我们将这个节点“扩展”，也就是遍历该节点状态可行的行动，作为其子节点。这些节点是没被遍历过的，所以对任意的$a$有$N(s,a)=0$，而奖赏也是未知的，姑且设置为$0$. 最后我们将父节点加入到树里，因为可以根据子节点信息得到最优行动。

#### 仿真（评价）

如果搜索树只进行上面两个策略：

$$
\text{选择}\leftrightarrows\text{扩展}
$$

似乎也可以搜索到指定深度，但由于我们的$Q$都是设置为0，那么选择最优行动时的标准就变为了

$$
a\gets\mathop{\arg\max}\limits_{a\in\mathcal{A}(s)}\sqrt{\dfrac{\log N(s)}{N(s,a)}}
$$

完全由遍历次数决定，这显然是不合理的。所以，对于扩展出的子节点，也需要拥有$Q$值。这里，我们采用某个**默认策略**来选择行动，直到到达制定深度。默认策略也称为**滚轮策略**（$\text{rollout policy}$）。经典的默认策略是随机的（部分解释了该算法和“蒙特卡罗方法”的联系），它为专家提供了一种方式，使得搜索偏向有希望的区域。

$\textbf{function }\text{ROLLOUT}(s,d):$\\
$\quad\textbf{if }d=0$\\
$\qquad\textbf{return }0$\\
$\quad a\gets\text{random}(\mathcal{A}(s))$\\
$\quad(s',r)\gets s(a)$\\
$\quad\textbf{return }r+\gamma\text{ROLLOUT}(s',d-1)$

#### 反向更新

我们从新扩展的节点进行仿真，访问了一次该节点，得到了一个$Q$值，显然会对前面“选择”途中遍历节点的$Q$值和$N$产生影响，因此我们从新节点开始，依次向上更新这两个值。

#### 伪代码版本

$\textbf{function }\text{UCTSearch}(s_0):$\\
$\quad\text{create root node }v_0\text{ with state }s_0.$\\
$\quad\text{while not out of time}:$\\
$\qquad v_l\gets\text{TreePolicy}(v_0)$\\
$\qquad \Delta\gets\text{DefaultPolicy}(v_l)$\\
$\qquad \text{backup}(v,\Delta)$\\
$\textbf{returns }a(\text{BestChild}(v_0,0))$

其中的函数细节需要我们去实现。

### 代码实现

相比于从零实现，在别人代码基础上进行修改更为困难，我们定义这样的一个叶节点：

```python
class TreeNode:
    '''
    表示搜索树中的一个节点
    '''
    def __init__(self, env:Game2048Env, parent):
        '''
        Parameters
        ----------
        env : 存储状态
        parent : 父节点
        
        Variables
        ---------
        children : 存储子节点的字典
        N : 访问此处
        Q : 初始效用
        '''
        pass
    
   	def expandable(self):
        '''判断是否可以扩展'''
        pass
    
    def expand(self):
        '''扩展一个叶节点'''
        pass
```

$\text{TreePolicy}$基于以下规则：

$\textbf{while }v\text{ is not terminal }\textbf{do}$\\
$\quad\textbf{if }v\text{ is expandable}$\\
$\qquad\textbf{returns }\text{expansion of }v$\\
$\quad\textbf{else}$\\
$\qquad v\gets\text{BestChild}(v,c)$

其中对于一个可扩展的节点，我们选择一步步将其完全展开，如果不可扩展，则采用上面所说的选择方法：

$$
\text{BuildChild}(v,c):\textbf{return }\mathop{\arg\max}\limits_{a\in\mathcal{A}(s)}\bigg(Q(s,a)+c\sqrt{\dfrac{\log N(s)}{N(s,a)}}\bigg)
$$

$\text{DefaultPolicy}$就是简单的$\text{ROLLOUT}$。反向更新中，我们将访问次数和效用进行更新：

$\textbf{while }v\text{ is not root}:$\\
$\quad N(v)\gets N(v)+1$\\
$\quad Q(v)\gets Q(v)+1$\\
$\quad v\gets v.parent$

按照要求，每次决策小号的时间是1s，故我们的搜索算法：

```python
from time import time

def MCTS(env: Game2048Env, d: int = 10, c: int = 100):
    root = TreeNode(env, None)
    t = time()
    while True:
        v = treePolicy(root)
        q = defaultPolicy(v, d)
        backup(v, q)
        if time() - t >= 1:
            break
    return bestAction(root, 0)
```

### 效果测试

```python
if __name__ == '__main__':
    d, c = 10, 100
    env = Game2048Env(True)
    env.seed(0)
    test_env = copy.deepcopy(env)
    test_env.setRender(True)
    obs = env.reset()
    done = False
    while not done:
        env_copy = deepcopy(env)
        action = MCTS(env_copy, c, d)
        obs, rew, done, info = env.step(action)
        print(rew, done, info)
    env.close()
    test_env.setRender(False)
    test_env.close()
```

运行上面的代码，我们进行运行测试：

<img src="/img/2048result.png" alt="img" style="zoom:50%;" />

可以看到作为一个2048玩家，$\mathbb{UCT}$已经有很高的水平，但仍然有发展空间.

### 算法改进

经高人指导，我们修改了$\text{ROLLOUT}$策略：

![rollout](/img/Agent/rollout.png)

也就是`defaultPolicy`的修改：

```python
def defaultPolicy(env):
    reward = env.score for i in range(d): 
        _, _, done, _ = env.step(randint(0, 3)) 
        if done: 
            break reward = env.score
    return reward
```

让我们再次测试⼀下程序，结果如下：

![success](/img/Agent/2048success.png)

说明策略的修正是正确的，也说明算法的强大。

## 第三次作业：用强化学习方法模拟悬崖行走

悬崖行走是一个无折扣的情节式游戏：

![game](/img/Agent/cliffwalk.png)

Agent从S开始，只能进行上、下、左和右四个动作，并且是确定性转移($p(s'\vert s,a)=0$或$1$). 对于每一次不会坠入悬崖的行动，我们都会有一个-1的奖赏（也就是1的惩罚），如果坠入悬崖，也就是图中的"Cliff"，会有-100的奖赏，并会退回到起始点S；到达终点G后，情节结束。

本文将基用Python的`gym`库的`cliffwalking`模块模拟悬崖行走的环境，并使用强化学习中的常用算法（Sarsa、Q-learning等）去让我们的Agent拥有智能，从而成功完成悬崖行走。

### 算法浅析

这次实验我们使用到的算法有：

1. Sarsa：同策略的时序差分控制；
2. n步Sarsa：Sarsa算法的拓展；
3. Sarsa($\lambda$)：使用累计迹的Sarsa；
4. Q-learning：异策略的时序差分控制.

我们先介绍Sarsa算法及其延伸.

#### Sarsa算法

SARSA（State-Action-Reward-State-Action）是一个学习马尔可夫决策过程策略的算法，通常应用于机器学习和强化学习学习领域中。它由Rummery和Niranjan在技术论文“Modified Connectionist Q-Learning（MCQL）” 中介绍了这个算法，并且由Rich Sutton在注脚处提到了SARSA这个别名。

State-Action-Reward-State-Action这个名称清楚地反应了其学习更新函数依赖的5个值，分别是当前状态$S_1$，当前状态选中的动作$A_1$，获得的奖励Reward，$S_1$状态下执行$A_1$后取得的状态$S_2$及$S_2$状态下将会执行的动作$A_2$。我们取这5个值的首字母串起来可以得出一个词SARSA。

算法的核心是下面的迭代式：

$$
Q(S_{t},A_{t})\gets Q(S_t,A_t)+\alpha\big[ R_t+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)\big]
$$

它是由贝尔曼期望方程：

$$
Q^\pi(s,a)=\sum_{s',r}p(s',r\vert s,a)\bigg(R(s,a)+\gamma\sum_{a'\in\mathcal{A}}\pi(a'\vert s')Q^\pi(s',a')\bigg)
$$

和增量估计方程：

$$
Q(S_{t+1},A_{t+1})=Q(S_t,A_t)+\alpha(G_{t}-Q(S_t,A_t))
$$

通过时序差分：

$$
G_t=R_{t}+\gamma Q_{t+1}
$$

结合而成。各方程和时序差分的推导在此省略。我们直接给出Sarsa的伪代码：

![sarsa](/img/Agent/sarsa.png)

可以发现算法的流程和我们前面所介绍的契合。我们可以观察到，sarsa中**行动选择和价值评估所使用的的策略相同**，这也是为什么称sarsa为“同策略时序差分控制”。

我们看到sarsa里的时序差分是：

$$
G_t=R_{t}+\gamma Q_{t+1}
$$

这个可以进一步拓展成多步时序差分：

$$
G_{t:t+n}=\sum_{i=0}^{n-1}\gamma^i R_{t+i}+\gamma^nQ_{t+n}
$$

加入我们将这种扩展的时序差分代入我们的迭代公式：

$$
Q(S_{t},A_{t})\gets Q(S_t,A_t)+\alpha\big[G_{t:t+n}-Q(S_t,A_t)\big]
$$

这就是$n$步sarsa。直观地看，n步sarsa相比于sarsa(也就是单步sarsa)的优点在于它能够改变更大范围的行动值$Q$. 算法伪代码如下：

![sarsa_n](/img/Agent/sarsa_n.png)

至于使用累计迹的Sarsa，笔者只知其然，不知所以然。粗略地说，我们对任务中的每个状态赋予一个变量，这个变量会随时间发生变化，这一变量叫做“资格迹”。如果我们在时间$t$遍历到一次状态$S$，此时$S$的资格迹$Z_t(S)$就会发生更新（增加），否则就会随时间衰减。我们会使用资格迹中的一种：累积迹作为值函数的更新权重。应用这种方法的sarsa算法被称作sarsa($\lambda$). 我们直接来看伪代码，它和原始的sarsa没什么显著差别：

![sarsa_lambda](/img/Agent/sarsa_lambda.png)

#### Q-learning算法

我们把在推导sarsa算法迭代式中用到的贝尔曼期望方程换成贝尔曼最优方程，那么就可以得到Q-learning算法的迭代公式：

$$
Q(S_{t},A_{t})\gets Q(S_t,A_t)+\alpha\big[ R_t+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\big]
$$

从而我们有伪代码：

![q-learning](/img/Agent/qlearning.png)

注意到我们用于行动选择时用到的策略是$\epsilon$-贪心策略，但是在评估$Q$值的时候使用的是贪心策略，因此Q-learning也被称作异策略的时序差分控制。

在了解算法大致流程后，我们就可以开始设计我们的实验代码了。

### 代码框架的构建

和往常一样，对于这种单环境多算法的测试任务，我们采用面向对象的方法书写代码：

```python
# 省略import步骤
class CliffWalkingGame:
    def __init__(self):
        '''初始化gym环境和一个48*4的Q表'''
        self.env = gym.make('CliffWalking-v0')
        self.q_table = np.zeros((
            self.env.observation_space.n,
            self.env.action_space.n,
        ))

    def epsilon_greedy(self, state, epsilon):
        '''ε-贪心策略'''
        if random.random() < epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state, :])

    def Sarsa(self, alpha, gamma, episodes):
        '''
        模拟Sarsa过程
        
        Parameter
        ---------
        alpha:学习率
        gamma:折扣因子
        episodes:迭代次数
        '''
        ...
        
    def play(self):
        '''用于播放已经规划号的路线'''
        ...

    def Qlearning(self, alpha, gamma, episodes):
        '''
        模拟Q-learning过程，参数含义和``Sarsa``相同.
        '''
        ...

    def SarsaN(self, alpha, gamma, eposides, n=1):
        '''
        模拟n步Sarsa
        '''
        ...

    def Sarsaλ(self, alpha, gamma, eposides, λ):
        '''
        模拟Sarsa(λ)
        '''
        ...
```

我们接下来的任务就是补全上面的类方法，难度不小，但颇有玩味。

### 方法补全

我们以Sarsa为例：

```python
    def Sarsa(self, alpha, gamma, episodes):
        reward_list_sarsa = []
        epsilons = np.linspace(0.9, 0.1, eposides) # 设置逐渐减小的ε
        self.q_table = np.zeros((
            self.env.observation_space.n,
            self.env.action_space.n,
        ))
        for i in range(eposides):
            state = self.env.reset() # Initial S 
            epsilon = epsilons[i]
            # Choose A form S using ε-greedy
            action = self.epsilon_greedy(state, epsilon)
            r = 0
            while True:
                # Take action A, observe R and S'
                next_state, reward, done, _ = self.env.step(action)

                # Choose action A' from S' using ε-greedy
                next_action = self.epsilon_greedy(next_state, epsilon)

                Q_now = self.q_table[state, action]
                Q_next = self.q_table[next_state, next_action]
                G = reward + gamma * Q_next

                # update Q value
                Q_now = Q_now + alpha * (G - Q_now)

                self.q_table[state, action] = Q_now
                state = next_state
                action = next_action
                r += reward
                if done:
                    break

            reward_list_sarsa.append(r)
        # 下面是对Q值表的结果进行验证，理论上可以通过Q值表找到一条成功路径
        best_route_value = []
        best_action_list = []
        next_state = self.env.reset()
        best_route_value.append(next_state)
        while True:
            action = np.argmax(self.q_table[next_state, :])
            best_action_list.append(action)
            next_state, _, done, _ = self.env.step(action)
            best_route_value.append(next_state)
            if done:
                break
        # 定义成员变量：奖赏列表，状态路线，行动路线
        self.reward_list, self.best_route_value, self.best_action_list = reward_list_sarsa, best_route_value, best_action_list
```

类似的，我们可以通过伪代码实现其余的算法。

### 效果展示

由于我们在每个算法函数的后面都会添加一个寻路的步骤，如果迭代之后Agent仍然无法找到路径，程序就会陷入死循环；从而只要函数可以正常返回，就可以说明寻路的正确性。那么我们可以尝试观察不同方法下生成路径的不同。因此我们设计了一个`play`函数用于播放悬崖行走的过程：

```python
def play(self):
    while True:
        self.env.reset()
        self.env.render()
        time.sleep(1)
        for a in self.best_action_list:
            self.env.step(a)
            os.system("cls")
            self.env.render()
            time.sleep(1)
        choose = input("重播：Y 退出：E：")
        if choose == 'E':
            break
        self.env.reset()
```

这里我们在之前的sarsa算法等方法中会保存一个成员变量`best_action_list`，用来记录行动，从而我们可以播放这一过程；此外，我们设计了一个循环，用于重复播放。效果如下：

<!-- 此处插入视频 -->

但为了节省读者时间，后面的路径展示用静态的方向图表示。

#### Q-learning和Sarsa算法的比较

先定义一个游戏对象：

```python
game = CliffWalkingGame()
```

然后我们分别调用：

```python
game.Sarsa(0.8, 0.95, 600)
# 和
game.Qlearning(0.8, 0.95, 600)
```

也就是将$\alpha$设置为$0.8$，$\gamma$设置为$0.95，迭代$600$次，得到了不同的行动轨迹，先来看sarsa算法：

```text
      → → → → → → → → ↓
→ → → ↑               ↓
↑                     ↓
↑ C C C C C C C C C C G
```

然后是Q-learning:

```text
 
 
→ → → → → → → → → → → ↓
↑ C C C C C C C C C C G
```

可以发现两算法的一个显著区别是：sarsa寻找的是更加“安全”的路径，而Q-learning意图更快地到达终点。这一点可以从算法上解释：sarsa在评估值函数时使用的是$\epsilon$-贪心，而Q-learning使用的是贪心算法，因此它更有可能选择最短路径。

#### 不同$n$值下的Sarsa算法

接下来我们想比较的是不同步数sarsa算法的表现：

我们分别设置$n$为$1,3,5$，观察它们在寻找路线上的不同：

```python
game = CliffWalkingGame()
game.SarsaN(0.8, 0.95, 1000, 1)
game.SarsaN(0.8, 0.95, 1000, 3)
game.SarsaN(0.8, 0.95, 1000, 5)
```

观察到$n=1$时的轨迹：

```text
  → → → → → → → → → ↓
→ ↑                 → ↓
↑                     ↓
↑ C C C C C C C C C C G
```

而在$n=3$时，轨迹是下面这样：

```text

            → → → → → ↓
→ → → → → → ↑         ↓
↑                     ↓
↑ C C C C C C C C C C G
```

下面是$n=5$时的行动轨迹：

```text
    → → ↓   → → → ↓
→ → ↑   → → ↑     → → ↓
↑                     ↓
↑ C C C C C C C C C C G
```

迭代步数相同时，$n$步Sarsa的优势并没有体现出来；但可以看到，在$n=5$时路线出现了弯折。我们要知道的是，$n$步迭代解决的其实是一次迭代只能对一个状态的值进行更新的缺陷，从而加快学习，我们的目的其实是比较学习的速度，我们会在后面提及。

#### 不同$\lambda$的Sarsa$(\lambda)$算法

我们将$\lambda$设置成$0,0.5,1$三个值，并观察寻路的差别：

```python
(game1 := CliffWalkingGame()).Sarsaλ(0.8, 0.9, 500, 0)
(game2 := CliffWalkingGame()).Sarsaλ(0.8, 0.9, 500, 0.5)
(game3 := CliffWalkingGame()).Sarsaλ(0.8, 0.9, 500, 1)
```

- $\lambda=0$:
    ```
      → → → → → → → → ↓
    → ↑               → ↓
    ↑                   → ↓
    ↑ C C C C C C C C C C G
    ```
- $\lambda=0.5$:
    ```
    → → → → → → → → → → → ↓
    ↑                     ↓
    ↑                     ↓
    ↑ C C C C C C C C C C G
    ```
- $\lambda=1$:
    ```
              → → → → → → ↓
    → → → → → ↑           ↓
    ↑                     ↓
    ↑ C C C C C C C C C C G
    ```

我们发现，对于sarsa$(\lambda)$算法，$\lambda=0.5$时有较好效果，可以看到此时最契合sarsa算法思想：寻求更加安全的路径。此外，我们在$\lambda=1$的训练过程中发现了训练时间长，会遇到浮点数异常等问题。

### 从奖赏角度进行模型比较

观察生成路线只是模型评估的一种参考，我们还可以通过每次迭代获得的奖赏进行比较。先从sarsa和Q-learning开始：

```python
game1 = CliffWalkingGame()
game1.Sarsa(0.8, 0.95, 600)
game2 = CliffWalkingGame()
game2.Qlearning(0.8, 0.95, 600)

plt.plot(game1.reward_list, label="sarsa")
plt.plot(game2.reward_list, label="Q-learning")
plt.legend()
plt.show()
```

下面就是两种算法的迭代次数-奖赏图像：

![sarsa-qlearning](/img/Agent/sarsa_qlearning.png)

从上图可以看出刚开始探索率ε较大时Sarsa算法和Q-learning算法波动都比较大，都不稳定，随着探索率ε逐渐减小Q-learning趋于稳定，Sarsa算法相较于Q-learning仍然不稳定。

再来看看不同$n$值下$n$步sarsa的表现：

![sarsa_n_plot](/img/Agent/sarsa_n_plot.png)

这里为了提高可视性，我们等距抽样出横坐标进行绘图，可以发现随着$n$的增大，奖赏的收敛速度更快，符合我们前面对算法的解释。

### 遇到的问题

我们之前提到，使用累计迹的Sarsa算法存在运行时间长的问题，而事实上，一开始的算法会消耗更多的时间（一小时才能运行完$\lambda=1$的600轮迭代），经过排查，我们发现语句

```python
...
for s in range(q_table.shape[0]):
    for a in range(q_table.shape[1]):
        update Z and Q
...
```

在循环上会消耗大量时间（真正消耗时间的是大量的数组索引取值），借用numpy数组的广播性质，我们将二重循环缩减为：

```python
self.q_table += alpha * delta * z_table
z_table = gamma * λ * z_table
```

于是运行速度大幅度提升。

### 总结

我们分别通过Sarsa、Q-learning、n步Sarsa、Sarsa$(\lambda)$算法去玩悬崖行走这样一个情节式游戏，并都获得了成功，进而验证了强化学习算法的可行性：无模型的完成复杂的游戏等任务。
