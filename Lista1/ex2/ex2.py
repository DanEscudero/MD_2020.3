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

def qda_g_k(k, X):
    i = k-1
    X = np.array(X)
    T1 = - (1/2) * transpose(X) * inverse(covars[i]) * X
    T2 = + transpose(avgs[i]) * inverse(covars[i]) * X
    T3 = - (1/2) * transpose(avgs[i]) * inverse(covars[i]) * avgs[i]
    T4 = - (1/2) * math.log(determinant(covars[i]))
    T5 = + math.log(prob(classes[i], data))
    return T1 + T2 + T3 + T4 + T5

def lda_g_k(k, X):
    cov = xs.cov()
    i = k-1
    X = np.array(X)
    T1 = transpose(X) * cov * avgs[i]
    T2 = - (1/2) * transpose(avgs[i]) * inverse(cov)
    T3 = math.log(prob(classes[i], data))
    return T1 + T2 + T3

def plot(discriminant):
    xs = np.arange(-10, 15, 0.25)
    ys = np.arange(-2, 10, 0.25)
    predicted = []
    for x in xs:
        for y in ys:
            d = dict()
            d['c1'] = -determinant(discriminant(1, [x,y]))
            d['c2'] = -determinant(discriminant(2, [x,y]))
            d['c3'] = -determinant(discriminant(3, [x,y]))
            d['c4'] = -determinant(discriminant(4, [x,y]))
            _class = max(d, key=d.get)
            predicted.append([x,y,_class])
    
    predicted = pd.DataFrame(data=predicted, columns=['x','y','c'])
    sns.scatterplot(data=predicted, x='x', y='y', hue='c')
    plt.show()


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
    
    xis = list(map(lambda classValue: data[data['c'] == classValue][attributes], classes))
    avgs, covars = getAvgs(xis), getCovars(xis)

    X = [4, 4]

    print('QDA')
    # print(determinant(qda_g_k(1, X)))
    # print(determinant(qda_g_k(2, X)))
    # print(determinant(qda_g_k(3, X)))
    # print(determinant(qda_g_k(4, X)))

    plot(qda_g_k)

    # print('____')
    # print('LDA')
    # print(lda_g_k(1, X))
    # print(lda_g_k(2, X))
    # print(lda_g_k(3, X))
    # print(lda_g_k(4, X))