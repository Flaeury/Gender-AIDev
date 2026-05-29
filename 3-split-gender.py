import pandas as pd

# ==========================================
# LOAD DATASET
# ==========================================
df = pd.read_excel(
    'data/user_gender_filtered_agents.xlsx'
)

# ==========================================
# FILTER DATA
# ==========================================
df_he = df[
    df['gender'] == 'he/him'
]

df_she = df[
    df['gender'] == 'she/her'
]

# ==========================================
# SAVE EXCEL FILES
# ==========================================
df_he.to_excel(
    'he_him.xlsx',
    index=False
)

df_she.to_excel(
    'she_her.xlsx',
    index=False
)

print("Excel files created successfully.")