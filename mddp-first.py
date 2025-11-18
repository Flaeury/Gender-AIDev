import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 🔹 Colunas que vamos usar
colunas_desejadas = ['pr_id', 'Analytic', 'Clout', 'Authentic', 'Tone', 'merged_at', 'created_at_comment']

# 🔹 Lê o CSV
df = pd.read_csv('data/TOTAL LIWC-22 - 4 dimensoes.csv', usecols=colunas_desejadas)

# 🔹 Converte a data
df['created_at_comment'] = pd.to_datetime(df['created_at_comment'], errors='coerce', utc=True)

# 🔹 Ordena para garantir que o mais antigo vem primeiro
df = df.sort_values(by='created_at_comment', ascending=True)

# 🔹 Mantém apenas o primeiro comentário de cada PR
df = df.drop_duplicates(subset='pr_id', keep='first')

# 🔹 Divide entre quem tem merged_at e quem não tem
df_merged = df[df['merged_at'].notnull()]
df_not_merged = df[df['merged_at'].isnull()]

# ======================================================
# Cálculo das médias e desvios
# ======================================================

colunas_metricas = ['Analytic', 'Clout', 'Authentic', 'Tone']

medias_merged = df_merged[colunas_metricas].mean()
desvios_merged = df_merged[colunas_metricas].std()

medias_not_merged = df_not_merged[colunas_metricas].mean()
desvios_not_merged = df_not_merged[colunas_metricas].std()

# ======================================================
# Exibição dos resultados
# ======================================================
print("📊 Estatísticas — Merged_at NÃO nula (PRs merged)")
print("Médias:\n", medias_merged)
print("\nDesvios padrão:\n", desvios_merged)
print(f"\nTotal de linhas: {len(df_merged)}")

print("\n" + "="*60 + "\n")

print("📊 Estatísticas — Merged_at NULA (PRs não merged)")
print("Médias:\n", medias_not_merged)
print("\nDesvios padrão:\n", desvios_not_merged)
print(f"\nTotal de linhas: {len(df_not_merged)}")

# ======================================================
# (Opcional) Visualizar comparação em gráfico
# ======================================================
# medias_df = pd.DataFrame({
#     'Merged_at não nula': medias_merged,
#     'Merged_at nula': medias_not_merged
# })
# ax = medias_df.plot(kind='bar', yerr=[desvios_merged, desvios_not_merged], capsize=4)
# ax.set_title('Comparação: PRs merged vs não merged')
# ax.set_ylabel('Média das dimensões LIWC')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
