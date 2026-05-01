# Compare csv and sql data
import pandas as pd
import pyodbc
pd.set_option("display.max_columns", None)

source=pd.read_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/company.csv")

conn =  pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-3EL4QLV\SQLEXPRESS;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"
)

cursor=conn.cursor()
cursor.execute("select * from cc_company")

target=pd.DataFrame(cursor.fetchall())
# print(result)

if source.shape[0]==target.shape[0]:
    print("count is same in source and target")
else:
    output=[ "Source count is more than target by "+ str(source.shape[0]-target.shape[0]) if (source.shape[0]-target.shape[0]) > 0
             else "target count is more by"+ str (target.shape[0]-source.shape[0]) ]
    print(output)



