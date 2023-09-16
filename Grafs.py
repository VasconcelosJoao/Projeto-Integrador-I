import pandas as pd
import matplotlib.pyplot as plt

# Gerando dados fictícios para temperatura e Humidade
nome_arquivo = 'saida.csv'
df = pd.read_csv(nome_arquivo)


# Histograma de Temperatura
plt.figure(figsize=(12, 6))
plt.hist(df['temperature'], bins=20, color='green', alpha=0.7)
plt.title('Histograma de Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequência')
plt.savefig('Images/histograma_temperatura.png')  # Salvar em um arquivo .png
plt.close()

# Histograma de Humidade
plt.figure(figsize=(12, 6))
plt.hist(df['humidity'], bins=20, color='green', alpha=0.7)
plt.title('Histograma de Humidade')
plt.xlabel('Humidade')
plt.ylabel('Frequência')
plt.savefig('Images/histograma_humidade.png')  # Salvar em um arquivo .png
plt.close()

# Box Plot de Temperatura
plt.figure(figsize=(8, 6))
plt.boxplot(df['temperature'], vert=False)
plt.title('Box Plot de Temperatura')
plt.xlabel('Temperatura (°C)')
plt.savefig('Images/box_plot_temperatura.png')  # Salvar em um arquivo .png
plt.close()

# Box Plot de Humidade
plt.figure(figsize=(8, 6))
plt.boxplot(df['humidity'], vert=False)
plt.title('Box Plot de Humidade')
plt.xlabel('Humidade')
plt.savefig('Images/box_plot_humidade.png')  # Salvar em um arquivo .png
plt.close()

# Gráfico de Dispersão entre Temperatura e Humidade
plt.figure(figsize=(10, 6))
plt.scatter(df['temperature'], df['humidity'], alpha=0.5, color='red')
plt.title('Gráfico de Dispersão entre Temperatura e Humidade')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Humidade (%)')
plt.savefig('Images/scatter_plot_temperatura_humidade.png')  # Salvar em um arquivo .png
plt.close()
