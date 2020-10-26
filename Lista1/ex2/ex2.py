import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def getAvgs(xs):
    return list(map(lambda x: x.mean(), xs))

def getCovars(xs):
    return list(map(lambda x: x.cov(), xs))

def determinant(m):
    return np.linalg.det(m.to_numpy())

def transpose(m):
    return m.transpose()

def inverse(m):
    return pd.DataFrame(np.linalg.pinv(m.values), m.columns, m.index)

def prob(className, data):
    c = len(data[data['c'] == className])
    total = len(data)
    return c/total

# k eh o indice da classe, de 1 a 4
def lda_g_k(k, X):
    i = k - 1
    X = np.array(X)
    T1 = transpose(X).dot(covariance).dot(avgs[i])
    T2 = - (1/2) * transpose(avgs[i]).dot(inverse(covariance)).dot(avgs[i])
    T3 = math.log(prob(classes[i], data))

    return T1 + T2 + T3

# k eh o indice da classe, de 1 a 4
def qda_g_k(k, X):
    i = k - 1
    X = np.array(X)
    T1 = - (1/2) * transpose(X).dot(inverse(covars[i])).dot(X)
    T2 = + transpose(avgs[i]).dot(inverse(covars[i])).dot(X)
    T3 = - (1/2) * transpose(avgs[i]).dot(inverse(covars[i])).dot(avgs[i])
    T4 = - (1/2) * math.log(determinant(covars[i]))
    T5 = + math.log(prob(classes[i], data))

    return T1 + T2 + T3 + T4 + T5

# Plota os pontos previstos pela funcao discriminante (lda ou qda)
def plot(discriminant, ax):
    xs = np.arange(-10, 15, 0.2)
    ys = np.arange(-2, 10, 0.2)
    predicted = []
    for x in xs:
        for y in ys:
            d = dict()
            d['c1'] = discriminant(1, [x,y])
            d['c2'] = discriminant(2, [x,y])
            d['c3'] = discriminant(3, [x,y])
            d['c4'] = discriminant(4, [x,y])
            className = max(d, key=d.get)
            predicted.append([x, y, className])
    
    predicted = pd.DataFrame(data=predicted, columns=['x','y','c'])
    sns.scatterplot(data=predicted, x='x', y='y', hue='c', ax=ax)


if __name__ == "__main__":
    data = pd.read_csv('./uma_base.csv', sep=",")

    # fig 1
    # sns.set_theme()
    # sns.jointplot(data=data, x='x', y='y', hue='c', kind='kde')
    # plt.show()

    attributes = ['x','y']
    D = len(attributes)

    classes = ['c1', 'c2', 'c3', 'c4']
    nClasses = len(classes)
    
    xs = data[['x', 'y']]
    ys = data['c']
    covariance = xs.cov()
    
    xs = list(map(lambda classValue: data[data['c'] == classValue][attributes], classes))
    avgs, covars = getAvgs(xs), getCovars(xs)

    # Fig 2
    fig, axs = plt.subplots(ncols=2)
    plot(lda_g_k, axs[0])
    plot(qda_g_k, axs[1])
    plt.show()