import pytest
import pandas as pd
import pyodbc
import pytest

# Check id customeriDis not null
df = pd.read_csv("Customer.csv")
@pytest.mark.skipif(not df.empty or df is not None, reason="File exist but I want to test skipif")
def test_check_CustomerIDNull():
    df = pd.read_csv("Customer.csv")
    check_null= df["CustomerID"].isnull().sum()
    print(check_null)
    assert check_null==0 , "Custome_id has null values, please check the data"

@pytest.mark.smoke
def test_duplicate():
    df = pd.read_csv("Customer.csv")
    duplicate_count = df.duplicated().sum()

    # assert duplicate_count == 0, "There are duplicate record"
@pytest.mark.parametrize("username, password",[("nancy","manocha"),("ankush","gupta")])
def test_check_parameter(username, password):
    print(username)
    print(password)

# def test_target_table_check():
#     conn = pyodbc.connect(
#         "Driver={SQL Server};"
#         "Server=DESKTOP-3EL4QLV\SQLEXPRESS;"
#         "Database=TestDB;"
#         "Trusted_Connection=yes;"
#
#     )
#
#     cursor = conn.cursor()
#     query = "select count(*) from cc_company"
#     count=pd.read_sql(query,conn)
#     print(count)
#
#     assert count>0, "No data in table"
#


