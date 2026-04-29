import csv

# Nomes dos CSVs de saída
he_file = 'data/1he_him.csv'
she_file = 'data/1she_her.csv'

with open('data/LIWC-22 - 4 dimensoes c filtro.csv', newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)

    idx_genero = cabecalho.index('gender')

    with open(he_file, 'w', newline='', encoding='utf-8') as f_he, \
            open(she_file, 'w', newline='', encoding='utf-8') as f_she:

        escritor_he = csv.writer(f_he)
        escritor_she = csv.writer(f_she)

        # Escreve o cabeçalho nas dois
        escritor_he.writerow(cabecalho)
        escritor_she.writerow(cabecalho)

        # Filtra as linhas pelo gênero
        for linha in leitor:
            if linha[idx_genero] == 'he/him':
                escritor_he.writerow(linha)
            elif linha[idx_genero] == 'she/her':
                escritor_she.writerow(linha)

print("Dados divididos em dois CSVs.")
