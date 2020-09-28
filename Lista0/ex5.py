import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def f():
    return 0.3 * np.random.normal(3,1) + 0.7 * np.random.normal(8,4)

def fs(xs):
    return 0.3 * norm.pdf(xs,3,1) + 0.7 * norm.pdf(xs,8,4)

def g():
    return np.random.normal(6,10)

def gs(xs):
    return norm.pdf(xs,6,10)

def plot(accepted):
    binWidth = 0.1
    N = 15
    xs = np.arange(0, N, binWidth)

    color1 = 'tab:blue'
    color2 = 'tab:red'

    _, sub1 = plt.subplots()
    sub1.hist(accepted, bins=xs, facecolor=color1)
    sub1.set_ylabel('Quantidade', color=color1)

    sub2 = sub1.twinx()
    sub2.plot(xs, fs(xs), color=color2)
    sub2.plot(xs, gs(xs), color=color2)
    sub2.set_ylabel('Valor das distribuições f e g', color=color2)

    plt.show()

# https://datasciencechalktalk.com/2019/09/22/understanding-rejection-sampling-method/
M = max(map(lambda _: f()/g(), range(1000)))

accepted = []
goalAccepted = 10000
while len(accepted) < goalAccepted:
    u = np.random.uniform()
    z = g()
    f1 = f()

    if (u < f1/(M*z)):
        accepted.append(z)
    
    M = max(M, f1/z)

plot(accepted)
