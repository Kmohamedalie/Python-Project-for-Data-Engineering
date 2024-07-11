#*******************************************************************#
#                       Querying SQLite3 database                   #
#*******************************************************************#

# How to connect to the SQLite3?
import sqlite3
sql_connection = sqlite3.connect('database.db')

# How to create a database table using SQLite3 and Pandas?
df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

# write a query
query_statement = "Select * from table_name"

# How to query a database table using SQLite3 and Pandas?
df = pandas.read_sql(query_statement, sql_connection)


# print table
print(df.head(10))