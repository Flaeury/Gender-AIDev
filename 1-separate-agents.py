import pandas as pd

input_file = 'data/aiddev_datatset.xlsx'
output_file = 'data/dataset-agents.xlsx'

df = pd.read_excel(input_file)

tamanho_df = len(df)
print(f'Tamanho do DataFrame original: {tamanho_df}')

df = df.loc[:, ~df.columns.astype(str).str.startswith('Unnamed')]

filtered_df = df[df['agent'].isin(['Copilot', 'Cursor', 'Devin'])].copy()

filtered_df['created_at'] = pd.to_datetime(
    filtered_df['created_at'],
    errors='coerce',
    utc=True
)

filtered_df = filtered_df.sort_values(
    by=['pr_id', 'created_at'],
    ascending=[True, True]
)

filtered_df['seq_comments'] = (
    filtered_df.groupby('pr_id').cumcount() + 1
)

filtered_df['created_at'] = filtered_df['created_at'].dt.tz_convert(None)

ordem_colunas = [
    'pr_id', 'user', 'agent', 'source_type', 'seq_comments', 'title', 'body',
    'created_at', 'body_pr', 'merged_at', 'state_pr_final', 
    'pr_created_at', 'pr_closed_at'
]

ordem_colunas = [col for col in ordem_colunas if col in filtered_df.columns]

filtered_df = filtered_df[ordem_colunas]

filtered_df.to_excel(output_file, index=False)