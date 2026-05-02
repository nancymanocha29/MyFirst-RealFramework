import pytest
import pandas as pd

# Check id customeriDis not null
def test_check_CustomerIDNull():
    df = pd.read_csv("Customer.csv")
    check_null= df.isnull().sum()

    assert check_null==0 , "Custome_id has null values, please check the data report"

def test_duplicate():
    df = pd.read_csv("Customer.csv")
    duplicate_count = df.duplicated().sum()

    assert duplicate_count == 0, "There are duplicate record"


