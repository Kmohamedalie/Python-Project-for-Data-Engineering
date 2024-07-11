#**************************************************************#
#        Create another table name Departments                 #
#**************************************************************#


# Python Scripting: Database initiation

# import libraries
import sqlite3
import pandas as pd


# conn to the STAFF.db
conn = sqlite3.connect('STAFF.db')


# Python Scripting: Create and Load the table
table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Reading the CSV file
file_path = '/home/project/Departments.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Loading the data to a table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Department Table is ready')


# Python Scripting: Running basic queries on data

# 1. Viewing all the data in the table.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# create the dataframe of the new data.
data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict)


# append the data to the INSTRUCTOR table
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')


# 2. Viewing only DEP_NAME column of data.
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# 3. Viewing the total number of entries in the table.
query = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query, conn)
print(query_statement)
print(query_output)


# close the connection to the database
conn.close()