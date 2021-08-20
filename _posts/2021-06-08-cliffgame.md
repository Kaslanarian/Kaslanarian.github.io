---
layout:     post
title:      强化学习应用
subtitle:   用强化学习方法去悬崖行走
date:       2021-06-08
author:     Welt Xing
header-img: img/Agent/cliff.jpg
catalog:    true
tags:
    - 强化学习
---

## <center>引言

悬崖行走是一个无折扣的情节式游戏：

![game](/img/Agent/cliffwalk.png)

Agent从S开始，只能进行上、下、左和右四个动作，并且是确定性转移($p(s'\vert s,a)=0$或$1$). 对于每一次不会坠入悬崖的行动，我们都会有一个-1的奖赏（也就是1的惩罚），如果坠入悬崖，也就是图中的"Cliff"，会有-100的奖赏，并会退回到起始点S；到达终点G后，情节结束。

本文将基用Python的`gym`库的`cliffwalking`模块模拟悬崖行走的环境，并使用强化学习中的常用算法（Sarsa、Q-learning等）去让我们的Agent拥有智能，从而成功完成悬崖行走。

## <center>算法浅析

这次实验我们使用到的算法有：

1. Sarsa：同策略的时序差分控制；
2. n步Sarsa：Sarsa算法的拓展；
3. Sarsa($\lambda$)：使用累计迹的Sarsa；
4. Q-learning：异策略的时序差分控制.

我们先介绍Sarsa算法及其延伸.

### Sarsa算法

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

### Q-learning算法

我们把在推导sarsa算法迭代式中用到的贝尔曼期望方程换成贝尔曼最优方程，那么就可以得到Q-learning算法的迭代公式：

$$
Q(S_{t},A_{t})\gets Q(S_t,A_t)+\alpha\big[ R_t+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\big]
$$

从而我们有伪代码：

![q-learning](/img/Agent/qlearning.png)

注意到我们用于行动选择时用到的策略是$\epsilon$-贪心策略，但是在评估$Q$值的时候使用的是贪心策略，因此Q-learning也被称作异策略的时序差分控制。

在了解算法大致流程后，我们就可以开始设计我们的实验代码了。

## <center>代码框架的构建

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

## <center>方法补全

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

## <center>效果展示

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

### Q-learning和Sarsa算法的比较

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

### 不同$n$值下的Sarsa算法

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

### 不同$\lambda$的Sarsa$(\lambda)$算法

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

## <center>从奖赏角度进行模型比较

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

## <center>遇到的问题

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

## <center>总结

我们分别通过Sarsa、Q-learning、n步Sarsa、Sarsa$(\lambda)$算法去玩悬崖行走这样一个情节式游戏，并都获得了成功，进而验证了强化学习算法的可行性：无模型的完成复杂的游戏等任务。
