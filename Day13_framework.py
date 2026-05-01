import pandas as pd
import openpyxl
import pyodbc

test_suite=pd.read_excel("C:/Users/dell/OneDrive/Desktop/Python_prac/Test_Suite.xlsx")
pd.set_option("display.max_columns", None)

def source_data_count(source_path):
    source_data = pd.read_csv(source_path)
    source_data_count = source_data.shape[0]
    return source_data_count

def target_data_count(target_table):
    conn = pyodbc.connect(
        "Driver={SQL Server};"
    "Server=DESKTOP-3EL4QLV\SQLEXPRESS;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"

    )

    cursor = conn.cursor()
    cursor.execute("select count(*) from "+ target_table)
    return cursor.fetchone()[0]

# print("check")
count_check_cases = test_suite[test_suite["Test Scenario"]=="count"]

null_check_cases = test_suite[test_suite["Test Scenario"]=="Null"]
# print(count_check_cases)
# print("hello  " + str(count_check_cases.shape[0])+ " "+count_check_cases +" " )
# print(count_check_cases.iloc[0,1])

for i in range(0,count_check_cases.shape[0]):
    print(i)
    source_path=str(count_check_cases.iloc[i,2])
    target_table=str(count_check_cases.iloc[i,1])
    test_case=str(count_check_cases.iloc[i,0])

    source_count=source_data_count(source_path)
    target_count= target_data_count(target_table)

    if source_count==target_count:
        print( test_case+" is passed and count is same in source and Target")
    else:
        print("There is mismatch in source and target count for test case - " + test_case)

    source_path=""
    target_table=""
    test_case=""

def nullcheck(target_table):
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-3EL4QLV\SQLEXPRESS;"
        "Database=TestDB;"
        "Trusted_Connection=yes;"

    )

    cursor = conn.cursor()
    query=f"select * from {target_table}"
    # cursor.execute("select * from " + target_table)
    target1= pd.read_sql(query,conn)
    null_columns = target1.columns[target1.isnull().sum() > 0].tolist()
    print(null_columns)
    return target1.isnull().sum()

for i in range(0,count_check_cases.shape[0]):
    # print(i)
    # source_path=str(count_check_cases.iloc[i,2])
    target_table=str(count_check_cases.iloc[i,1])
    output= nullcheck(target_table)

    print(output)

    if output.sum() > 0:
        print("null values")
        # list_of_col = [[output.iloc[i, 0]] for i in range(0, output.shape[0]) if output.isnull()=True]
        # print(list_of_col)
    else:
        print("no null value")
