import pandas as pd

input_file_1 = 'data/dataset-all-agents.xlsx'
input_file_2 = 'data/ATUALIZADO_user_pronouns.xlsx'
output_file = 'data/user_gender_all_agents.xlsx'

df1 = pd.read_excel(input_file_1)
df2 = pd.read_excel(input_file_2)

df2_all = df2[df2['gender'].isin(['he/him', 'she/her'])]

merged_df = pd.merge(df1, df2_all, on="user", how="inner")

final_columns = [
    "pr_id", "user", "gender", "agent", "source_type", "seq_comments", "title", "body",
    "created_at", "body_pr", "merged_at", "state_pr_final",
    "pr_created_at", "pr_closed_at"
]

existing_columns = [col for col in final_columns if col in merged_df.columns]
missing_columns = set(final_columns) - set(existing_columns)

if missing_columns:
    print(f"Colunas não encontradas e serão ignoradas: {missing_columns}")

merged_df = merged_df[existing_columns]

merged_df.to_excel(output_file, index=False)

print(f"Arquivo '{output_file}' criado com sucesso ({len(merged_df)} linhas).")

total_mensagens = len(merged_df)

usuarios_unicos = merged_df['user'].nunique()

usuarios_por_genero = merged_df.drop_duplicates(subset=['user'])['gender'].value_counts()

print(f"Total de mensagens (linhas): {total_mensagens}")
print(f"Total de usuários únicos: {usuarios_unicos}")
print("Usuários por gênero:")
for genero, count in usuarios_por_genero.items():
    print(f"   {genero}: {count}")