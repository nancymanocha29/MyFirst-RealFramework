import pyodbc
from sqlalchemy import create_engine, inspect

expected_schema = {
    "CustomerID": "INT",
    "Name": "VARCHAR(50)",
    "Age": "INT",
    "JoinDate": "DATE"
}

# Connect to SQL Server
engine = create_engine(
    "mssql+pyodbc://@DESKTOP-3EL4QLV\\SQLEXPRESS/TestDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# Inspect target table schema
inspector = inspect(engine)
columns = inspector.get_columns("dept")

print(inspector.get_table_names())

# Convert to dict {column_name: datatype}
actual_schema = {col["name"]: str(col["type"]).upper() for col in columns}
print(actual_schema)


