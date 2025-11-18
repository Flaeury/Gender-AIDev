# gerar de tudo
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

colunas_desejadas = ['Analytic', 'Clout', 'Authentic', 'Tone', 'merged_at']

df = pd.read_csv('data/TOTAL LIWC-22 - 4 dimensoes.csv', usecols=colunas_desejadas)

# filtra somente linhas onde merged_at não é vazio
df = df[df['merged_at'].notnull()]

medias = df[['Analytic', 'Clout', 'Authentic', 'Tone']].mean().transpose()
desvios = df[['Analytic', 'Clout', 'Authentic', 'Tone']].std().transpose()

print("Médias:")
print(medias)

print("\nDesvios Padrão:")
print(desvios)

# ax = medias.plot(kind='bar', yerr=desvios, capsize=4,
#                 color=['skyblue', 'lightcoral'], edgecolor='black')
# ax.set_title('Médias e Desvios Padrão das Colunas (merged_at não nula)')
# ax.set_xlabel('Colunas')
# ax.set_ylabel('Valores')
# ax.grid(axis='y')
# ax.legend(title='Source')
# ax.tick_params(axis='x', rotation=45)
# plt.tight_layout()
# plt.savefig('media_desvio.png', dpi=300)
# plt.show()


# contar quantas linhas sobraram
print(f"\nTotal de linhas com merged_at não nula: {len(df)}")