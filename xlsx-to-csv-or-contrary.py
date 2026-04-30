# vou gear um codigo para converter arquivos xlsx para csv e vice versa. a unica coisa que eu faço é chamar la no final a funcao que eu quero como o nome do arquivo, tipo: xlsx_to_csv('meuarquivo.xlsx') ou csv_to_xlsx('meuarquivo.csv')
import pandas as pd

def xlsx_to_csv(xlsx_file, csv_file):
    df = pd.read_excel(xlsx_file)
    df.to_csv(csv_file, index=False, encoding='utf-8')  
    print(f"Arquivo '{xlsx_file}' convertido para '{csv_file}' com sucesso.")

def csv_to_xlsx(csv_file, xlsx_file):
    df = pd.read_csv(csv_file, encoding='utf-8')
    df.to_excel(xlsx_file, index=False)
    print(f"Arquivo '{csv_file}' convertido para '{xlsx_file}' com sucesso.") 

# Exemplo de uso:
xlsx_to_csv('data/ATUALIZADO_user_pronouns.xlsx', 'data/ATUALIZADO_user_pronouns.csv')
# csv_to_xlsx('data/ATUALIZADO_user_pronouns.csv', 'data/ATUALIZADO_user_pronouns.xlsx')