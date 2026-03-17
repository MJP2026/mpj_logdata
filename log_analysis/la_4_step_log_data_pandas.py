# source .venv/bin/activate && pip install pandas

import pandas as pd;

print("X"*70)
print("Hello pandas world! la_4_step_log_data_pandas.py")
print("X"*70)

# Dataframe df
df = pd.read_csv('myLogVar_20_rows.csv', header=None, names=['ReturnCode', 'Duration(ms)', 'Text'])
summary = (df.groupby('ReturnCode').agg({
    'Duration(ms)': 'mean',
    'Text': 'mean',
    'ReturnCode': 'count'
     })
    .rename(columns={'ReturnCode': 'Count'}))
print(summary)

print("X"*70)
summary2 = (df.groupby('Duration(ms)').agg({
    'ReturnCode': 'mean',
    'Text': 'mean',
    'Duration(ms)': 'count'
     })
     .rename(columns={'Duration(ms)': 'Count'}))
print("X"*70)
print(summary2)
print("X"*70)
print("Bye pandas world!")
print("X"*70)