# Projeto: Monitoramento de Temperatura com Arduino

## Resumo do Projeto

O projeto consiste em um sistema de monitoramento de temperatura e umidade de um quarto, utilizando um Arduino Uno conectado a um notebook. O sistema coleta dados de temperatura e umidade em intervalos regulares, armazena as informações em um banco de dados SQLite e gera gráficos para análise dos dados ao longo do tempo. O projeto foi desenvolvido para demonstrar a integração de hardware e software na coleta e análise de dados ambientais.

O código do Arduino é responsável por ler os dados do sensor DHT11 e enviá-los ao notebook, onde são processados e analisados. O principal contribuinte do projeto foi João Lucas, que atuou como Scrum Master e desenvolvedor, garantindo a organização e a qualidade do desenvolvimento.

## Funcionalidades

- Coleta de dados de temperatura e umidade a cada 10 segundos.
- Armazenamento dos dados em um banco de dados SQLite.
- Exportação dos dados para um arquivo CSV.
- Análise e tratamento de dados, incluindo a correção de valores faltantes e outliers.
- Geração de gráficos de temperatura e umidade média por dia.

## Requisitos

- **Hardware**: Arduino Uno, sensor DHT11.
- **Software**: 
  - IDE Arduino para programação do Arduino.
  - Python com bibliotecas `pandas`, `matplotlib`, e `sqlite3` para análise de dados.


## Análise de Dados

Os dados coletados são analisados e visualizados utilizando a biblioteca `matplotlib`, permitindo a geração de gráficos que mostram a temperatura e umidade média por dia.

## Contribuições

O projeto foi desenvolvido por João Lucas, que desempenhou um papel crucial como Scrum Master e desenvolvedor, liderando a equipe e garantindo a implementação eficaz das funcionalidades.

---
