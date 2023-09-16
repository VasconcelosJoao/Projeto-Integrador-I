import pandas as pd

# Carregue o arquivo CSV em um DataFrame
nome_arquivo = 'saida.csv'
df = pd.read_csv(nome_arquivo)

# Verifique se há linhas duplicadas no DataFrame
linhas_duplicadas = df.duplicated().sum()

# Verifique se há valores inválidos (por exemplo, negativos em uma coluna que não pode ser negativa)
valores_invalidos = (df['temperature'] < 0).sum() + (df['humidity'] < 0).sum() 

# Verifique se há inconsistências (por exemplo, datas fora de ordem)
inconsistencias = (df['timestamp'] < df['timestamp'].shift()).sum()  

# Exiba os resultados

print("\nLinhas duplicadas:")
print(linhas_duplicadas)

print("\nValores inválidos:")
print(valores_invalidos)

print("\nInconsistências:")
print(inconsistencias)

