"""import pandas as pd

'''data = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Aman", "Riya", "Vinay", "Neha", "Rahul", "Pooja"],
    "Subject": ["Python", "Python", "Java", "Java", "Python", "Java"],
    "Marks": [78, 85, 67, 90, 72, 88],
    "Attendance_%": [92, 88, 75, 95, 80, 90]
}

df = pd.DataFrame(data)'''
#print(df.groupby("Subject")["Marks"].mean())
#print(df[df["Subject"]=="Python"])
#print(df[df["Marks"]>80])
#print(df[df["Attendance_%"]<80])
#print(df.max())
#print(df["Attendance_%"].mean())
#print(df["Marks"].sort_values(ascending=False))
#print(df.groupby("Subject").agg("count"))
#print(df.loc[df["Marks"].idxmax(),["Subject"]=="Python"])
#df["result"] = df["Marks"].apply(lambda x: "Pass" if x>=75 else "Fail")
#print(df)
d1={
    "name":["vinay","anshul","santosh","sushil"],
    "age":[20,21,32,21],
    "salary":[98000,68000,95000,45000]
}
df1=pd.DataFrame(d1)
import numpy as np 
m=np.where(df1>25 and "salary">60000 )
print(m)
"""

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



