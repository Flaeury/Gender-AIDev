import pandas as pd
from pathlib import Path

input_file = Path("data/aidev_datatset.xlsx")
output_file = Path("data/dataset-all-agents.xlsx")

output_file.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(input_file, engine="openpyxl")

print(f"Tamanho do DataFrame original: {len(df)}")

df = df.loc[:, ~df.columns.astype(str).str.startswith("Unnamed")]

# filtered_df = df[df["agent"].isin(["Copilot", "Cursor", "Devin"])].copy()

# TRAS TODOS OS AGENTES PARA O MESMO DATAFRAME # 
filtered_df = df[df['agent'].isin(['Copilot', 'Cursor', 'Devin', 'OpenAI_Codex', 'Claude_Code'])].copy()

filtered_df["created_at"] = pd.to_datetime(
    filtered_df["created_at"],
    errors="coerce",
    utc=True
)

filtered_df = filtered_df.sort_values(
    by=["pr_id", "created_at"],
    ascending=[True, True]
)

filtered_df["seq_comments"] = filtered_df.groupby("pr_id").cumcount() + 1

filtered_df["created_at"] = filtered_df["created_at"].dt.tz_localize(None)

ordem_colunas = [
    "pr_id", "user", "agent", "source_type", "seq_comments", "title", "body",
    "created_at", "body_pr", "merged_at", "state_pr_final",
    "pr_created_at", "pr_closed_at"
]

ordem_colunas = [col for col in ordem_colunas if col in filtered_df.columns]

filtered_df = filtered_df[ordem_colunas]

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    filtered_df.to_excel(writer, index=False, sheet_name="dados")

print(f"Arquivo salvo em: {output_file.resolve()}")
print(f"Linhas salvas: {len(filtered_df)}")

print(filtered_df.shape)
print(filtered_df["agent"].value_counts())