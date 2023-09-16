import sqlite3
import csv

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Executar uma consulta para selecionar os dados desejados da tabela 'measurements'
cursor.execute('SELECT * FROM measurements')

# Obter todas as linhas dos resultados da consulta
rows = cursor.fetchall()

# Nome do arquivo CSV de saída
csv_file = 'saida.csv'

# Escrever os dados no arquivo CSV
with open(csv_file, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    
    # Escrever o cabeçalho (nomes das colunas)
    column_names = [description[0] for description in cursor.description]
    csv_writer.writerow(column_names)
    
    # Escrever as linhas de dados
    csv_writer.writerows(rows)

# Fechar a conexão com o banco de dados
conn.close()

print(f'Dados exportados para {csv_file}')
