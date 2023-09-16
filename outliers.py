import pandas as pd
import numpy as np

# Carregando os dados do arquivo CSV
df = pd.read_csv('saida.csv')

# Visualizando as primeiras linhas do DataFrame
print(df.head())

# Verificando se há valores faltantes
print(df.isnull().sum())

# Defina uma função para corrigir outliers na coluna de temperatura usando o IQR
def corrigir_outliers(data, coluna):
    q1 = data[coluna].quantile(0.25)
    q3 = data[coluna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    data[coluna] = np.where((data[coluna] < limite_inferior) | (data[coluna] > limite_superior),
                            data[coluna].median(), data[coluna])

# Especifique as colunas de temperatura e umidade
coluna_temperatura = 'temperature'  # Substitua 'temperatura' pelo nome da sua coluna de temperatura
coluna_humidade = 'humidity'  # Substitua 'umidade' pelo nome da sua coluna de umidade

# Corrija outliers nas colunas de temperatura e umidade
corrigir_outliers(df, coluna_temperatura)
corrigir_outliers(df, coluna_humidade)

# Verificando novamente se há valores faltantes após a correção de outliers
print(df.isnull().sum())

# Salve o DataFrame corrigido no mesmo arquivo CSV
nome_arquivo_corrigido = "saida.csv"
df.to_csv(nome_arquivo_corrigido, index=False)
