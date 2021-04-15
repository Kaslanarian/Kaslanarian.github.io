---
layout:     post
title:      Matrix Cookbook Notebook
subtitle:   求导与其他运算
date:       2021-04-15
author:     Welt Xing
header-img: img/matrix.jpg
catalog:    true
tags:
    - 数学
---

## 引言

由于在机器学习中，我们会常常遇到对矩阵，向量的求导，虽然在《最优化方法》中耳濡目染了一些技巧，但仍缺少系统性总结，故作此文以记录.

本文是对[Matrix CookBook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)的翻译和提炼总结.

## 基本符号

### 矩阵

- $\textbf{A}$是矩阵；
- $(\textbf{A})_{ij}$和$A_{ij}$都是取矩阵的第$i$行第$j$列元素.
- $[\textbf{A}]_{ij}$是删去第$i$行和第$j$列的子矩阵.
- $\textbf{0}$，全零矩阵；
- $\textbf{I}$，对角矩阵；
- $\textbf{J}^{ij}$,单元素矩阵，除了$(i,j)$为$1$，其余为$0$.
- $\bm{\Sigma}$,正定矩阵.
- $\Lambda$，对角矩阵.

### 向量

- $\textbf{a}$是向量；
- $a_i$是向量$\textbf{a}$的第$i$个元素.

### 标量

- $a$是标量.

### 运算子

- $\det(\textbf{A})$表示行列式；
- $\text{Tr}(\textbf{A})$表示迹；
- $\text{diag}(\textbf{A})$是“$\textbf{A}$的对角矩阵”（但我不明白它的意思）
- $\text{eig}(A)$是矩阵的特征值(eigenvalues)
- $\text{vec}(\textbf{A})$是“矩阵的向量形式”：

$$
\textbf{A}=\begin{bmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}\\
\end{bmatrix}\quad\text{vec}(\textbf{A})=\begin{bmatrix}
A_{11}\\
A_{21}\\
A_{12}\\
A_{22}\\
\end{bmatrix}
$$

- $\textbf{A}^{-T}$就是$(\textbf{A}^{-1})^T$,或者是$(\textbf{A}^{T})^{-1}$

## 基础运算规则

### 迹运算

$$
\begin{aligned}
\text{Tr}(\textbf{A})
&=\sum_{i}A_{ii}\\
&=\sum_{i}\lambda_i,\quad\lambda_i=\text{eig}(\textbf{A})\\
&=\text{Tr}(\textbf{A}^T)
\end{aligned}
$$

$$
\text{Tr}(\textbf{AB})=\text{Tr}(\textbf{BA})
$$

$$
\text{Tr}(\textbf{A+B})=\text{Tr}(\textbf{A})+\text{Tr}(\textbf{B})
$$

$$\textbf{a}^T\textbf{a}=\text{Tr}(\textbf{aa}^T)$$

### 行列式运算

$$
\det(\textbf{I}+\textbf{uv}^T)=1+\textbf{u}^T\textbf{v}
$$

## 求导

求导通式：

$$
\dfrac{\partial X_{kl}}{\partial X_{ij}}=\delta_{ik}\delta_{lj}
$$

比如

$$
\bigg[\dfrac{\partial\boldsymbol{x}}{\partial y}\bigg]_i=\dfrac{\partial x_i}{\partial y}\quad\bigg[\dfrac{\partial{x}}{\partial \boldsymbol{y}}\bigg]_i=\dfrac{\partial x}{\partial y_i}\quad\bigg[\dfrac{\partial{x}}{\partial y}\bigg]_{ij}=\dfrac{\partial x_i}{\partial y_j}
$$
