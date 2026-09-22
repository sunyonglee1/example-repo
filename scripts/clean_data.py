import pandas as pd

df_raw = pd.read_csv('data/raw_data.csv')

print(df_raw.isna().sum())

df_clean = df_raw.dropna(subset=['Store_ID']).copy()

df_clean['Revenue'] = df_clean['Revenue'].fillna(
    df_clean.groupby('Units_Sold')['Revenue'].transform('median')
)

df_clean['Revenue'] = df_clean['Revenue'].fillna(
    df_clean['Revenue'].median()
)

print(df_clean.isna().sum())

df_clean.to_csv('data/clean_data.csv', index=False)