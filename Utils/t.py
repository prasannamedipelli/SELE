import pandas as pd

data = {
    "name": ["vishal","vikas","rahul"],
    "role": ["QA","Tester","security tester"],
    "Experience" :[23,30,12]
}

df=pd.DataFrame(data)
print(df)

df1= pd.read_csv("emp.csv")
print(df1)

df2= pd.read_excel("sample.xlsx")
print(df2)

print(df["Experience"].mean())