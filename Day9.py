#Panada lib day -1
import pandas as pd
print(pd.__version__)

df = pd.DataFrame([('Ankush',35),('Nancy',32),('Ahaan',)], columns=["Name of Member","Age"])

# print(df.head(2))
# print(df.shape)
df.rename(columns={"Name of Member": "Family_Member"},inplace=True)
print(df)
print(df.info())
print(df.columns)
print(df.shape)

df.to_csv("C:/Users/dell/OneDrive/Desktop/python_sample_files/test_csv.csv")


