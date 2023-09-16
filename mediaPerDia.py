import pandas as pd
import matplotlib.pyplot as plt

def plot_and_save_graph(data, xlabel, ylabel, title, filename):
    plt.figure(figsize=(15, 5))
    plt.plot(data.index, data, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(filename)  # Salva o gráfico como arquivo PNG
    plt.close()  # Fecha a figura para liberar recursos

nome_arquivo = 'saida.csv'
df = pd.read_csv(nome_arquivo)

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

df['dia'] = df['timestamp'].dt.date.dropna()

dados_agrupados = df.groupby('dia')[['temperature', 'humidity']].mean()

# Salve os gráficos como arquivos PNG
plot_and_save_graph(dados_agrupados['temperature'], 'Dia', 'Temperatura Média', 'Temperatura Média por Dia', 'Images/temperatura_media_por_dia.png')

plot_and_save_graph(dados_agrupados['humidity'], 'Dia', 'Humidade Média', 'Humidade Média por Dia', 'Images/humidade_media_por_dia.png')


