import pandas as pd

# Lê o CSV
df = pd.read_csv('data/LIWC-22 - 4 dimensoes c filtro.csv')

# 🔹 Mantém apenas PRs únicos (primeira ocorrência de cada pr_id)
df = df.drop_duplicates(subset='pr_id', keep='first')

# 🔹 (Opcional) Filtra somente usuários com gender == 'he/him'
df = df[df['gender'] == 'he/him']

# -----------------------------------------------------
# Contagem de valores closed e open
closed_count = df['state_pr_final'].value_counts().get('closed', 0)
open_count = df['state_pr_final'].value_counts().get('open', 0)
print(f'Total de state_pr_final not null: {df["state_pr_final"].notnull().sum()}')
print(f'Closed: {closed_count}, Open: {open_count}')

# -----------------------------------------------------
# Linhas com closed e merged_at não nula
closed_merged_done = df[(df['state_pr_final'] == 'closed') & (df['merged_at'].notnull())].shape[0]
print(f'Linhas com closed e merged_at feito: {closed_merged_done}')

# Linhas com closed e merged_at nula
closed_merged_not_done = df[(df['state_pr_final'] == 'closed') & (df['merged_at'].isnull())].shape[0]
print(f'Linhas com closed e merged_at nao feito: {closed_merged_not_done}')

# -----------------------------------------------------
# Linhas com open e merged_at nula
open_merged_not_done = df[(df['state_pr_final'] == 'open') & (df['merged_at'].isnull())].shape[0]
print(f'Linhas com open e merged_at não feito: {open_merged_not_done}')

# Linhas com open e merged_at não nula
open_merged_done = df[(df['state_pr_final'] == 'open') & (df['merged_at'].notnull())].shape[0]
print(f'Linhas com open e merged_at feito: {open_merged_done}')

# -----------------------------------------------------
# Porcentagens de merged_at
merged_not_null = df['merged_at'].notnull().sum()
merged_null = df['merged_at'].isnull().sum()
total = merged_not_null + merged_null
if total > 0:
    print(f'Porcentagem de merged_at não nula: {merged_not_null / total * 100:.2f}%')
    print(f'Porcentagem de merged_at nula: {merged_null / total * 100:.2f}%')

# -----------------------------------------------------
# Contagem total de PRs únicos
print(f"Total de PRs únicos: {df['pr_id'].nunique()}")

