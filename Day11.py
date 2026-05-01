# Created DF after performing some transformation on csv file data and loaded it into SQL
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

pd.set_option("display.max_columns", None)
company = pd.read_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/Company.csv")

user = pd.read_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/User.csv")

accounts = pd.read_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/Accounts.csv")

def standardize_columns(df):
    df.columns=(df.columns.str.lower()
                .str.replace(" ", "_")
                .str.replace("-","_")
                # .str.replace(r"[^\w_]", regex=True)
                 )
    return df

company=standardize_columns(company)
user=standardize_columns(user)
accounts=standardize_columns(accounts)

company=pd.merge(company, accounts.loc[accounts["account_type"]=="Checking",
                                                ["companyid","account_number"]],
                                               left_on="companyid",
                                               right_on="companyid",
                                               how="left").fillna("00000")
company["rank"]=company.groupby("companyid")["account_number"].rank(method="dense")
company = company.loc[company["rank"]==1]

Company_migrated= {"CC_Company_id": company["companyid"],
                   "CC_Company_Name":company["cname"].str.strip().str.replace(r"[^\w_]","", regex=True)
                                    .str[:41]
                   ,"CC_Address":company["address1"] +" "+ company["address2"]
                   ,"CC_City":company["city"],
                   "CC_state":company["state"],
                   "CC_zip":company["zip"][0:6],
                   "CC_email":company["email"],
                   "CC_Billing_Account": company["account_number"],
                       # pd.merge(company, accounts.loc[accounts["account_type"]=="Checking",
                       #                          ["companyid","account_number"]],
                       #                         left_on="companyid",
                       #                         right_on="companyid",
                       #                         how="left")["account_number"].fillna("00000"),
                   "CC_Tax_id":company["tax_id"]

                   }
# print(company)
# CC_company=pd.DataFrame(Company_migrated)
pd.DataFrame(Company_migrated).to_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/CC_Company.csv", index=False)

cc_company = pd.read_csv("C:/Users/dell/OneDrive/Desktop/Python_prac/CC_Company.csv")

conn =  pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-3EL4QLV\SQLEXPRESS;"
    "Database=TestDB;"
    "Trusted_Connection=yes;"
)

# cursor = conn.cursor()
# cursor.execute("select * from Emp")
# for row in cursor.fetchall():
#     print(row)

# conn.close()

engine = create_engine(
    "mssql+pyodbc://@DESKTOP-3EL4QLV\\SQLEXPRESS/TestDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# Load DataFrame into SQL Server
cc_company.to_sql("cc_company", con=engine, if_exists="replace", index=False)

# print("Data loaded successfully!")
# print(pyodbc.drivers())
print("Data loaded successfully!")