import pandas as pd

df = pd.read_excel(
    "Australian_Life_Tables.xlsx",
    sheet_name="Males"
)

print(df.head())

