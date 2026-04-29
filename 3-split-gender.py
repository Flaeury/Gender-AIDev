import pandas as pd

# Nomes dos CSVs de saída
he_file = ''
she_file = ''

with open('ARQUIVO', newline='', encoding='utf-8') as f:
    leitor = pd.read_excel(f)
    cabecalho = leitor.columns

    idx_genero = cabecalho.index('gender')

    with open(he_file, 'w', newline='', encoding='utf-8') as f_he, \
            open(she_file, 'w', newline='', encoding='utf-8') as f_she:

        escritor_he = pd.ExcelWriter(f_he, engine='xlsxwriter')
        escritor_she = pd.ExcelWriter(f_she, engine='xlsxwriter')

        escritor_he.writerow(cabecalho)
        escritor_she.writerow(cabecalho)

        for linha in leitor:
            if linha[idx_genero] == 'he/him':
                escritor_he.writerow(linha)
            elif linha[idx_genero] == 'she/her':
                escritor_she.writerow(linha)

print("Dados divididos em dois CSVs.")
