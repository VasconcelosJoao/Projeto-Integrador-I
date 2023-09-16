# Importando a biblioteca pandas
import pandas as pd

# Carregando os dados
df = pd.read_csv('saida.csv')

# Visualizando as primeiras linhas do DataFrame
print(df.head())

# Verificando se há valores faltantes
print(df.isnull().sum())

# Preenchendo valores faltantes com a média da coluna
df.fillna(df.mean(), inplace=True)

# Verificando novamente se há valores faltantes
print(df.isnull().sum())
