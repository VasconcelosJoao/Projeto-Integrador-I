import pandas as pd

# Carregue o arquivo CSV em um DataFrame
nome_arquivo = 'saida.csv'
df = pd.read_csv(nome_arquivo)

# Certifique-se de que a coluna 'temperature' seja do tipo numérico (float)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Encontre o índice (linha) com a maior temperatura
indice_max_temp = df['temperature'].idxmax()

# Obtenha a data e o valor da temperatura correspondentes à maior temperatura
data_maior_temp = df.loc[indice_max_temp, 'timestamp']
valor_maior_temp = df.loc[indice_max_temp, 'temperature']

print(f"A data da maior temperatura é: {data_maior_temp}")
print(f"O valor da maior temperatura é: {valor_maior_temp}")