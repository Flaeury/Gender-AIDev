#Pegar todoas as colunas e linhas onde a coluna "agent" seja Copilot, Cursor ou Devin

import csv
import pandas as pd

input_file = 'comment_review_result_2.csv'
output_file = 'separar-agentes.csv'

# Ler o arquivo CSV de entrada
df = pd.read_csv(input_file)

# Filtrar as linhas onde a coluna "agent" seja Copilot, Cursor ou Devin
filtered_df = df[df['agent'].isin(['Copilot', 'Cursor', 'Devin'])]

# Salvar o DataFrame filtrado em um novo arquivo CSV
filtered_df.to_csv(output_file, index=False)