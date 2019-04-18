import pandas
import sqlite3

conn = sqlite3.connect('nypldb.db')

df = pandas.read_csv('nypl_items.csv', low_memory=False)

df.to_sql('nypl_items', conn)

print(pandas.read_sql_query("SELECT * FROM nypl_items", conn))