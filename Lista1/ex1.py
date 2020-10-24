import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def filterMaxAge ():
    # data['age'].max() = 60667, indicando um possível erro nos dados;
    # Estabelecendo um limite de idade; Dados com idade > 100 serão desconsideradas
    # O valor limite vêm do artigo original https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-020-1023-5/tables/1
    return data[data['age'] < 100]

def getLayout(cols):
    return (2, math.ceil(len(cols)/2))

def plotBooleanCounts(data, cols):
    nrows, ncols = getLayout(cols)
    _, ax = plt.subplots(nrows, ncols, sharey=True)
    for col, subplot in zip(cols, ax.flatten()):
        sns.countplot(x=data[col], ax=subplot)

def plotNumericalCounts(data, cols):
    data[cols].hist(bins=15, figsize=(15, 6), layout=getLayout(cols))


def plotBoxPlots(data, cols, x):
    nrows, ncols = getLayout(cols)
    _, ax = plt.subplots(nrows, ncols)
    for col, subplot in zip(cols, ax.flatten()):
        sns.boxplot(x=x, y=col, data=data, ax=subplot)

if __name__ == "__main__":
    data = pd.read_csv('./data.tsv', sep="\t")
    data = filterMaxAge()

    numerical = ['age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
    categorical = ['anaemia', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']

    # Agrupa idades por faixa etária. O número de bins 11 foi escolhido de forma a gerar intervalos de 5 anos
    data['faixa_etaria'] = pd.cut(data['age'], 11, precision=0)

    sns.set_theme()
    # fig 1
    plotBooleanCounts(data, categorical)

    # fig 2
    plotNumericalCounts(data, numerical)

    # fig 3
    plotBoxPlots(data, numerical, 'faixa_etaria')

    # fig 4
    plotBoxPlots(data, numerical, 'DEATH_EVENT')

    # fig 5
    correlationMatrix = data.corr()
    sns.heatmap(correlationMatrix, annot=True, vmin=-1, vmax=1, cmap=sns.diverging_palette(220, 20, as_cmap=True))

    plt.show()