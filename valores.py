# quero saber quantos valores da coluna statepr_final estao com closed e com open do csv
# e quero saber quantas linhas tem closed e a coluna mergedat nao é nula


import pandas as pd
import csv

# df1 tem que ser so de users com gender igual he/him

df1 = pd.read_csv('data/LIWC-22 - 4 dimensoes.csv') 
df = df1[df1['gender'] == 'she/her']

closed_count = df['state_pr_final'].value_counts().get('closed', 0)
open_count = df['state_pr_final'].value_counts().get('open', 0) 
print(f'Total de state_pr_final not null: {df["state_pr_final"].notnull().sum()}') 
print(f'Closed: {closed_count}, Open: {open_count}')

# Contar linhas com 'closed' e 'merged_at' não nula
closed_merged_count = df[(df['state_pr_final'] == 'closed') & (df['merged_at'].notnull())].shape[0]
print(f'Linhas com closed e merged_at feito: {closed_merged_count}')

# Contar linhas com 'closed' e 'merged_at' nula
closed_merged_count = df[(df['state_pr_final'] == 'closed') & (df['merged_at'].isnull())].shape[0]
print(f'Linhas com closed e merged_at nao feito: {closed_merged_count}')

# Contar linhas com 'open' e 'merged_at' nula
open_merged_count = df[(df['state_pr_final'] == 'open') & (df['merged_at'].isnull())].shape[0]
print(f'Linhas com open e merged_at não feito: {open_merged_count}')


# Contar linhas com 'open' e 'merged_at' não nula
open_merged_count = df[(df['state_pr_final'] == 'open') & (df['merged_at'].notnull())].shape[0]
print(f'Linhas com open e merged_at feito: {open_merged_count}')

# calcula porcentagem de merged nao nulas e nulas para os mulheres (df) 
merged_not_null = df['merged_at'].notnull().sum()
merged_null = df['merged_at'].isnull().sum()
total = merged_not_null + merged_null
if total > 0:
    print(f'Porcentagem de merged_at não nula: {merged_not_null / total * 100:.2f}%')
    print(f'Porcentagem de merged_at nula: {merged_null / total * 100:.2f}%')