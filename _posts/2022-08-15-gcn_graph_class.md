---
layout:     post
title:      将GCN应用到图分类任务
subtitle:   From GCN to Graph Classification
date:       2022-08-15
author:     Welt Xing
header-img: img/gnn.jpg
catalog:    true
tags:
    - 图神经网络
---

前篇：<https://welts.xyz/2022/08/13/gcn_implementation/>. 在那里，我们实现了GCN层并应用到简单的图节点分类任务。本文我们将继续使用自实现的GCN模块，进行**图分类**任务。

图分类的数据单位不再是节点，而是一个图，即一个图对应一个标签。因此，我们需要用一个特征向量来描述一张图。而将图节点的多个向量转换成图的表示向量的操作，被称作READOUT。READOUT的方式不唯一，最简单的是将最后一层GCN的输出，即节点的向量表示取平均；也有将各个GCN层的输出（包括最开始的输入）取平均后加权求和，如下图所示（图源李宏毅老师的讲义）：

<img src="/img/image-20220814200250094.png" alt="image-20220814200250094" style="zoom: 50%;" />

## Data & PyG

我们这次用的数据集是ENZYMES，ENZYMES数据集包含着600张图，每张图有一个label，label共有6种可能的属性，分别是0-5。我们通过PyG来获取该数据集，这是一个基于PyTorch的图神经网络软件包，里面的数据的都是以PyTorch的张量形式存储，便于操作。PyG的安装可以参考[官方手册](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html)。

加载数据，获取数据集中图的信息

```python
from torch_geometric.datasets import TUDataset

dataset = TUDataset(root='./ENZYMES', name='ENZYMES')

len(dataset)              # 数据集大小 600
dataset.num_classes       # 图的类别数 6 (用于图分类)
dataset.num_features      # 图节点特征数 3
dataset.num_node_labels   # 图节点的类别数 3 (用于图节点分类)
dataset.num_edge_labels   # 边的类别数 0 (用于边分类)
dataset.num_edge_features # 边的特征数 0 (用于边分类)
```

我们可以通过索引来获取具体的图：

```python
g = dataset[0]
print(g) # Data(edge_index=[2, 168], x=[37, 3], y=[1])
```

图`g`对应PyG的`torch_geometric.data.Data`类，它包括

- `edge_index`，一个$2\times$边数的Long型张量，对应边索引；
- `x`，一个节点数$\times$节点特征数的张量，对应节点特征；
- `y`，一个单元素张量，对应点标签。

还有`edge_attr`等属性，用于边分类场景。图分类任务只需要上面三个属性即可。

我们可以将`g`绘制出来：

```python
import networkx as nx

graph = nx.Graph()
graph.add_edges_from(dataset[0].edge_index.numpy().T)
nx.draw(graph)
```

<img src="/img/image-20220814220851226.png" alt="image-20220814220851226" style="zoom:67%;" />

发现比之前的空手道俱乐部关系图复杂得多，而这只是600张图之一。

## Baseline Model

我们用上之前自设计的`GCNConv`层，来设计图分类网络：

```python
import torch
from torch import nn

num_classes = dataset.num_classes
num_features = dataset.num_features

class GCN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.gcn = GCNConv(num_features, 16)
        self.fc = nn.Linear(16, num_classes)

    def forward(self, x, edge_index):
        # 将节点特征取均值得到图特征
        x = torch.relu(self.gcn(x, edge_index).mean(0))
        return self.fc(x)
```

设计数据集：

```python
from tqdm import tqdm

# 节点特征数据集，邻接矩阵数据集，标签数据集
X, edge, y = [], [], []

for i in tqdm(range(L), desc='Load dataset'):
    X.append(dataset[i].x)
    y.append(dataset[i].y.numpy())
    edge_index = dataset[i].edge_index
    A = torch.zeros((X[-1].shape[0], X[-1].shape[0]))
    A[edge_index[0], edge_index[1]] = 1
    edge.append(A)

y = torch.tensor(np.array(y)).long()
```

注意到这里的`X`和`edge`，因为每张图的节点数都不同的缘故，所以我们只能用列表去存储，无法形成高维数组，也就是无法批处理。这也导致我们接下来的训练必须是逐样本输入网络。

我们这里是在全部数据集上训练，只看训练准确率：

```python
gcn = GCN()
optimizer = torch.optim.Adam(gcn.parameters(), lr=0.01)

acc_list = []
loss_list = []
L = len(dataset)

for i in range(1000):
    # 输入整张图
    gcn.train()
    loss = sum([
        F.cross_entropy(
            gcn(X[j], edge[j]).reshape(1, n_label),
            y[j],
        ) for j in range(L)
    ]) / L # 求平均损失
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    gcn.eval()
    correct = 0
    for j in range(L):
        output = gcn(X[j], edge[j])
        correct += int(output.detach().numpy().argmax() == y[j])
    print("epoch {:3d} : acc {:.4f}, loss {}".format(
        i + 1,
        100 * correct / L,
        loss.item(),
    ))
    acc_list.append(correct / L)
    loss_list.append(loss.item())
```

训练1000轮，绘制出损失和准确率图像：

<img src="/img/image-20220815110429965.png" alt="image-20220815110429965" style="zoom:80%;" />

训练准确率为35%不到。看到这么“差”的表现，我们有两个可能的解释：

1. 模型实现有问题；
2. 数据集确实很“难”。

搜索该数据集的[Leaderboard](https://paperswithcode.com/sota/graph-classification-on-enzymes)，我们发现这确实是一个很难的数据集：

![image-20220815105732593](/img/image-20220815105732593.png)

所以我们的实现至少是没有大问题的。

## Improvement

我们考虑更宽和更深的网络，试图对Baseline的性能进行提升：

- 16的单隐层拓展为128单隐层；
- 16的单迎层拓展为64双隐层。

性能对比：

<img src="/img/image-20220815110340519.png" alt="image-20220815110340519" style="zoom: 80%;" />

发现加深和加宽网络都可带来分类性能的提升，尤其是加深，准确率能高达40%。

此外，因为是64双隐层，我们可以加入残差项训练。再考虑最上面提到的带权重的READOUT过程，我们也可以仿照这样的操作，但这样操作的前提是GCN层的输出和输入的维数相同：

```python
class GCN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.gcn1 = GCNConv(n_feature, n_feature)
        self.fc1 = nn.Linear(n_feature, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, n_label)
        # 可学习的权重参数
        self.w1 = nn.parameter.Parameter(torch.tensor(1.))
        self.w2 = nn.parameter.Parameter(torch.tensor(1.))

    def forward(self, x, edge_index):
        x = torch.relu(
            self.gcn1(x, edge_index).mean(0) * self.w1 + x.mean(0) * self.w2)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
```

训练结果总结：

<img src="/img/image-20220815112042672.png" alt="image-20220815112042672" style="zoom:80%;" />

我们发现残差确实带来性能提升，但不如修改READOUT策略，训练准确率能到达40%以上。

## Summary

我们在这里将GCN从节点分类任务拓展到了图分类任务，同时通过对网络的的改进提升分类效果。但我们在前面埋下了一个问题：即图神经网络训练中能否引入batch机制？对于小型图，batch机制能够实现一次计算多个图；对于大型图，batch机制能够单次计算图的一小部分。这也是我们后面尝试探究的内容。
