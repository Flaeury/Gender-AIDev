import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def login_github(driver):
    """Abre o GitHub para login manual."""
    driver.get("https://github.com/login")
    input("| Faça login no GitHub e pressione Enter para continuar...")


def login_linkedin(driver):
    """Abre o LinkedIn para login manual."""
    driver.get("https://www.linkedin.com/login")
    input("| Faça login no LinkedIn e pressione Enter para continuar...")


def extract_pronouns_or_linkedin(driver, author):
    """Extrai o pronome do GitHub, e se não encontrar, tenta no LinkedIn."""
    github_url = f"https://github.com/{author}"
    driver.get(github_url)
    time.sleep(3)

    # Tenta encontrar pronome no GitHub
    try:
        pronoun_element = driver.find_element(
            By.XPATH, "//span[contains(@class, 'p-nickname')]//following-sibling::span"
        )
        pronoun = pronoun_element.text.strip()
        if pronoun:
            return pronoun
    except Exception:
        pass

    # Se não encontrou, tenta achar link para LinkedIn
    try:
        linkedin_link = driver.find_element(By.XPATH, "//a[contains(@href, 'linkedin.com/in/')]")
        linkedin_url = linkedin_link.get_attribute("href")

        if linkedin_url:
            driver.get(linkedin_url)
            time.sleep(5)
            try:
                span_element = driver.find_element(By.XPATH, "//span[contains(@class, 'text-body-small')]")
                linkedin_pronoun = span_element.text.strip()
                return linkedin_pronoun if linkedin_pronoun else "Null"
            except Exception:
                return "Null"
    except Exception:
        return "Null"

    return "Null"


def update_csv_with_pronouns(input_csv, output_csv, driver):
    authors_data = []
    processed_users = set()  # guarda quem já foi avaliado

    # Carregar os dados existentes
    with open(input_csv, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            authors_data.append(row)

    # Se já existe arquivo de saída, carrega os usuários já processados
    if os.path.exists(output_csv):
        with open(output_csv, "r", encoding="utf-8") as outfile:
            reader = csv.DictReader(outfile)
            for row in reader:
                processed_users.add(row["user"].strip())

    updated_data = []

    for row in authors_data:
        # CSV COM GENEROS
        # if row["gender"].strip() == "Null":
        #     author = row["user"]
        #     print(f"\nBuscando dados de {author}...")
        #     new_gender = extract_pronouns_or_linkedin(driver, author)
        #     print(f"Encontrado: {author} - {new_gender}")
        #     row["gender"] = new_gender
        author = row["user"].strip()
        if author in processed_users:
            print(f"Pulando {author} (já processado).")
            continue

        print(f"\nBuscando dados de {author}...")
        new_gender = extract_pronouns_or_linkedin(driver, author)
        print(f"Encontrado: {author} - {new_gender}")

        updated_data.append({"user": author, "gender": new_gender})
        processed_users.add(author)

        # CSV COM GENEROS
        # with open(output_csv, "w", encoding="utf-8", newline="") as outfile:
        #     fieldnames = ["user", "gender"]
        #     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerows(updated_data)

        # Salva o progresso continuamente (para não perder nada se o script parar)
        with open(output_csv, "a", encoding="utf-8", newline="") as outfile:
            fieldnames = ["user", "gender"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Se o arquivo estiver vazio, escreve o cabeçalho
            if outfile.tell() == 0:
                writer.writeheader()

            writer.writerow({"user": author, "gender": new_gender})

    print(f"\nTotal de usuários processados: {len(processed_users)}")


if __name__ == "__main__":
    input_csv_path = "comment_review_result_2.csv"
    output_csv_path = "github_pronouns.csv"

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    login_github(driver)
    login_linkedin(driver)

    update_csv_with_pronouns(input_csv_path, output_csv_path, driver)

    driver.quit()
    print("\nFinalizado.")
