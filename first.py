

import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\Dell\.vscode\Dataset for Data Anatytics.xlsx")
df.fillna("NULL",inplace=True)
#df.drop_duplicates(inplace=True)
#print("dublicate rows:",df.duplicated().sum())
#print("null values:",df.isnull().sum())
df["Date"]=pd.to_datetime(df["Date"])
df["Date"]=df["Date"].dt.strftime("%d %b %y")



df.to_excel("Dataset forr Data Anatytics.xlsx",index=False)
print("file cleaned and saved successfully")



