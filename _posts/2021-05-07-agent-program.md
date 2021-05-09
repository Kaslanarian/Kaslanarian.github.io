---
layout:     post
title:      栅格世界的决策算法
subtitle:   实验报告
date:       2021-05-07
author:     Welt Xing
header-img: img/Agent/prog.jpg
catalog:    true
tags:
    - 智能系统
---

## 前言

本文是对《智能系统设计与应用》第一次编程作业中所涉及的知识点介绍，以及编程想法的记录.

## 实验目的

在$10\times10$的栅格世界中，分别应用值迭代，高斯-赛德尔值迭代和策略迭代算法，使得$\text{Agent}$在这个栅格世界的每一个格子（也就是一个状态）都能获取到状态效用并找到最优决策$\pi^\star(s)$.

## 关于栅格世界

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

## 价值迭代算法

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

## 高斯-赛德尔价值迭代

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

## 策略迭代

我们发现，即使在效用函数估计不准确的情况下，仍有可能得到最优策略，如果前一个行动比其他所有行动都要好，那么涉及效用的计算不需要太准确，这一简介暗示除了价值迭代还存在另一种找到最优策略的方法，也就是策略迭代：

![policy_iteration](/img/Agent/policy_iter.png)
<center>策略迭代就是策略评估和策略提升的迭代</center>

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
&\qquad\qquad unchanged\gets\text{False}
&\quad\textbf{until }\delta\lt\dfrac{\epsilon(1-\gamma)}{\gamma}\\
&\quad\textbf{until }unchanged
&\textbf{return }\pi
\end{aligned}
$$

注意到这里循环终止的条件是策略相关，即只要策略不再变化，我们就停止迭代，但并不代表效用值函数收敛，我们会在后面看到这一论断是正确的.

## 程序框架的构建

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

## 值迭代算法的实现

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

## 策略迭代的算法实现

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

不同于收敛效用，只用14次迭代便收敛，我们调用`display_action`方法来观察两种终止条件下的策略，发现最优策略是相同的：

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

## 结语

至此我们已经用`Python`实现了价值迭代和策略迭代，虽然刚入手的时候觉得难度很大，但只要解决了其中一个任务，后面的任务只是程序框架中一些细节的改动. 这次程序作业也加深我对强化学习的认识（相比于上学期只是了解一些术语），相比于朴素的样本学习，强化学习不需要带标签的输入输出对，同时也无需对非最优解的精确地纠正。这是最令我惊叹的地方。
