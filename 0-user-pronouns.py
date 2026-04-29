import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def login_github(driver):
    driver.get("https://github.com/login")
    input("| Faça login no GitHub e pressione Enter para continuar...")


def login_linkedin(driver):
    driver.get("https://www.linkedin.com/login")
    input("| Faça login no LinkedIn e pressione Enter para continuar...")


def extract_pronouns_or_linkedin(driver, author):
    github_url = f"https://github.com/{author}"
    driver.get(github_url)
    time.sleep(3)

    try:
        pronoun_element = driver.find_element(
            By.XPATH, "//span[contains(@class, 'p-nickname')]//following-sibling::span"
        )
        pronoun = pronoun_element.text.strip()
        if pronoun:
            return pronoun
    except Exception:
        pass

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


def update_xlsx_with_pronouns(input_xlsx, output_xlsx, driver):
    df = pd.read_excel(input_xlsx)

    if "user" not in df.columns:
        raise ValueError("A planilha de entrada precisa ter uma coluna chamada 'user'.")

    if os.path.exists(output_xlsx):
        output_df = pd.read_excel(output_xlsx)
        processed_users = set(output_df["user"].astype(str).str.strip())
    else:
        output_df = pd.DataFrame(columns=["user", "gender"])
        processed_users = set()

    new_rows = []

    for _, row in df.iterrows():
        author = str(row["user"]).strip()

        if not author or author.lower() == "nan":
            continue

        if author in processed_users:
            print(f"Pulando {author} (já processado).")
            continue

        print(f"\nBuscando dados de {author}...")
        new_gender = extract_pronouns_or_linkedin(driver, author)
        print(f"Encontrado: {author} - {new_gender}")

        new_rows.append({
            "user": author,
            "gender": new_gender
        })

        processed_users.add(author)

        temp_df = pd.concat(
            [output_df, pd.DataFrame(new_rows)],
            ignore_index=True
        )

        temp_df.to_excel(output_xlsx, index=False)

    print(f"\nTotal de usuários processados: {len(processed_users)}")


if __name__ == "__main__":
    input_xlsx_path = "data/aidev_dataset.xlsx"
    output_xlsx_path = "user_pronouns.xlsx"

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    login_github(driver)
    login_linkedin(driver)

    update_xlsx_with_pronouns(input_xlsx_path, output_xlsx_path, driver)

    driver.quit()
    print("\nFinalizado.")
