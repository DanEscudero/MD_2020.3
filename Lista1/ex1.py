import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = pd.read_csv('./data.tsv', sep="\t")
    # data['age'].max() = 60667, indicando um possível erro nos dados;

    # estabelecendo um limite de idade; Dados com idade > 95 serão desconsideradas
    # O valor limite vêm do artigo original https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-020-1023-5/tables/1
    data = data[data['age'] < 100]

    data['age'].mean() # 60.8
    print(data.describe())