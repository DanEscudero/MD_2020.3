import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def makeCategorical(data, col):
    data[col] = pd.Categorical(data[col])
    data[col] = data[col].cat.codes

def getLayout(cols):
    lines = 1
    return (lines, math.ceil(len(cols)/lines))

def plotBoxPlots(data, cols, x):
    nrows, ncols = getLayout(cols)
    _, ax = plt.subplots(nrows, ncols)
    for col, subplot in zip(cols, ax.flatten()):
        sns.boxplot(x=x, y=col, data=data, ax=subplot)

def plotCorrelation(data):
    correlationMatrix = data.corr()
    sns.heatmap(correlationMatrix, annot=True, vmin=-1, vmax=1, cmap=sns.diverging_palette(220, 20, as_cmap=True))
    plt.xticks(rotation=30,fontsize=8)

if __name__ == "__main__":
    sns.set_theme()
    data = pd.read_csv('../../DEF_NaoLigamosParaAG_FullData.csv', sep=",")

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    data['carro_foi_comprado'] = data.apply(lambda x: not math.isnan(x['valor_carro_comprado']),axis=1)

    # data['idade_negociante'] = pd.Categorical(data['idade_negociante'])
    # makeCategorical(data, 'carro_foi_comprado')
    # makeCategorical(data, 'periodo_visita')
    # makeCategorical(data, 'sexo_negociante')
    # makeCategorical(data, 'idade_negociante')
    # makeCategorical(data, 'cor_cabelo_negociante')
    # makeCategorical(data, 'gesticula_negociante')
    # makeCategorical(data, 'vestimenta_negociante')
    # makeCategorical(data, 'entrou_nos_carros')
    # makeCategorical(data, 'tipo_primeiro_carro')
    # makeCategorical(data, 'tipo_segundo_carro')
    # makeCategorical(data, 'tipo_carro_comprado')

    # cols = data.columns
    # cols = ['ano_primeiro_carro','ano_segundo_carro','ano_carro_comprado']
    # cols = ['valor_primeiro_carro','valor_segundo_carro','valor_carro_comprado']
    # cols = ['tipo_primeiro_carro', 'tipo_segundo_carro', 'tipo_carro_comprado']

    # plotBoxPlots(data, cols, 'loja')

    # print(data)
    # sns.catplot(x='loja', y='carro_foi_comprado', data=data, hue='loja', kind='bar')

    # cols = ['sexo_negociante', 'cor_cabelo_negociante']
    # condicao = data['carro_foi_comprado'] == 1
    # data[cols][condicao].hist(bins=15, figsize=(15, 6))

    sns.countplot(x='cor_carro_comprado', data=data)

    # sns.lineplot(data=data, x='loja', y='tempo_atendimento')
    # sns.boxplot(data=data, x='loja', y='tempo_atendimento')
    # sns.jointplot(data=data, x='carro_foi_comprado', y='loja', kind='kde')

    # plotCorrelation()
    
    plt.show()