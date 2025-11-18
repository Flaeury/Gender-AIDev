import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

colunas_desejadas = ['Analytic', 'Clout', 'Authentic', 'Tone', 'merged_at']

df_hehim = pd.read_csv('data/1he_him.csv', usecols=colunas_desejadas)
df_sheher = pd.read_csv('data/1she_her.csv', usecols=colunas_desejadas)

df_hehim['Source'] = 'HeHim'
df_sheher['Source'] = 'SheHer'

df = pd.concat([df_hehim, df_sheher], ignore_index=True)

# filtra somente linhas onde merged_at não é nula
df = df[df['merged_at'].notnull()]

medias = df.groupby('Source')[['Analytic', 'Clout', 'Authentic', 'Tone']].mean().transpose()
desvios = df.groupby('Source')[['Analytic', 'Clout', 'Authentic', 'Tone']].std().transpose()

print("Médias:")
print(medias)

print("\nDesvios Padrão:")
print(desvios)

ax = medias.plot(kind='bar', yerr=desvios, capsize=4,
                color=['skyblue', 'lightcoral'], edgecolor='black')
ax.set_title('Médias e Desvios Padrão das Colunas (merged_at não nula)')
ax.set_xlabel('Colunas')
ax.set_ylabel('Valores')
ax.grid(axis='y')
ax.legend(title='Source')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('media_desvio_hehim.png', dpi=300)
plt.show()

# t-test entre grupos
df_hehim_group = df[df['Source'] == 'HeHim']
df_sheher_group = df[df['Source'] == 'SheHer']

print("\nP-values (t-test):")
for col in ['Analytic', 'Clout', 'Authentic', 'Tone']:
    t_stat, p_value = stats.ttest_ind(
        df_hehim_group[col].dropna(),
        df_sheher_group[col].dropna(),
        equal_var=False
    )
    print(f"  {col}: {p_value:.4f}")

# contar quantas linhas sobraram
print(f"\nTotal de linhas com merged_at não nula: {len(df)}")
print(f" - He/Him: {len(df_hehim_group)}")
print(f" - She/Her: {len(df_sheher_group)}")
