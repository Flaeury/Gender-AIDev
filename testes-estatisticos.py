import pandas as pd
from scipy import stats

excel_path_1 = 'she_her.xlsx'
excel_path_2 = 'he_him.xlsx'


# ==========================================
# LOAD AND PROCESS
# ==========================================
def process_dataset(excel_path):

    # load dataset
    df = pd.read_excel(excel_path)

    # remove duplicates
    df = df.drop_duplicates()

    # ==========================================
    # NUMBER OF CHARACTERS
    # ==========================================
    df['num_characters'] = (
        df['body']
        .fillna('')
        .astype(str)
        .str.len()
    )

    character_values = df['num_characters']

    # ==========================================
    # NUMBER OF INTERACTIONS PER USER IN EACH PR
    # ==========================================
    interactions_per_user = (
        df.groupby('pr_id')['body']
        .count()
    )

    return character_values, interactions_per_user


# ==========================================
# PROCESS BOTH DATASETS
# ==========================================
chars_she, interactions_she = process_dataset(excel_path_1)

chars_he, interactions_he = process_dataset(excel_path_2)


# ==========================================
# CHARACTER STATISTICS
# ==========================================
print("\n=========================================")
print("NUMBER OF CHARACTERS")
print("=========================================\n")

print("SHE/HER")
print(f"Mean: {chars_she.mean():.2f}")
print(f"Standard deviation: {chars_she.std():.2f}")

print("\nHE/HIM")
print(f"Mean: {chars_he.mean():.2f}")
print(f"Standard deviation: {chars_he.std():.2f}")

# Welch t-test
t_stat_chars, p_value_chars = stats.ttest_ind(
    chars_she,
    chars_he,
    equal_var=False
)

print("\nT-TEST")
print(f"T-statistic: {t_stat_chars:.4f}")
print(f"P-value: {p_value_chars:.5}")


# ==========================================
# INTERACTION STATISTICS
# ==========================================
print("\n=========================================")
print("INTERACTIONS PER USER IN EACH PR")
print("=========================================\n")

print("SHE/HER")
print(f"Mean: {interactions_she.mean():.2f}")
print(f"Standard deviation: {interactions_she.std():.2f}")

print("\nHE/HIM")
print(f"Mean: {interactions_he.mean():.2f}")
print(f"Standard deviation: {interactions_he.std():.2f}")

# Welch t-test
t_stat_interactions, p_value_interactions = stats.ttest_ind(
    interactions_she,
    interactions_he,
    equal_var=False
)

print("\nT-TEST")
print(f"T-statistic: {t_stat_interactions:.4f}")
print(f"P-value: {p_value_interactions:.5}")