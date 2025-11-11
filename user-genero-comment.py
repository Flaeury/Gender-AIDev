import pandas as pd

# Caminhos dos arquivos
input_file_1 = 'data/separar-agentes.csv'
input_file_2 = 'data/github_pronouns.csv'
output_file = 'data/user_genero_comment.csv'

# Ler os dois arquivos CSV
df1 = pd.read_csv(input_file_1)
df2 = pd.read_csv(input_file_2)

# Filtrar apenas os gêneros desejados
df2_filtered = df2[df2['gender'].isin(['he/him', 'she/her'])]

# Fazer o merge com base na coluna "user"
merged_df = pd.merge(df1, df2_filtered, on="user", how="inner")

# Reorganizar as colunas na ordem desejada
final_columns = [
    'pr_id', 'user', 'gender', 'agent',
    'body', 'created_at_comment', 'type', 'title',
    'body_pr', 'merged_at', 'state_pr_final',
    'created_at', 'closed_at'
]

# Verificar se todas as colunas existem antes de reordenar
existing_columns = [col for col in final_columns if col in merged_df.columns]
missing_columns = set(final_columns) - set(existing_columns)

if missing_columns:
    print(f"Colunas não encontradas e serão ignoradas: {missing_columns}")

merged_df = merged_df[existing_columns]

# Salvar o resultado em um novo CSV
merged_df.to_csv(output_file, index=False)

print(f"Arquivo '{output_file}' criado com sucesso ({len(merged_df)} linhas).")

total_mensagens = len(merged_df)

# Total de usuários únicos
usuarios_unicos = merged_df['user'].nunique()

# Contagem de usuários por gênero
usuarios_por_genero = merged_df.drop_duplicates(subset=['user'])['gender'].value_counts()

# Mostrar resumo
print(f"Total de mensagens (linhas): {total_mensagens}")
print(f"Total de usuários únicos: {usuarios_unicos}")
print("Usuários por gênero:")
for genero, count in usuarios_por_genero.items():
    print(f"   {genero}: {count}")