import sqlite3 as sq


# creating database
database = sq.connect("db_name")
print("db created")


# performing queries
database.execute("""
CREATE TABLE table_name(
    Name char(100),
    Age int
);
""")
print("table created")


database.execute("INSERT INTO table_name VALUES ('bhavin', 23);")
database.execute("INSERT INTO table_name VALUES ('kevin', 22);")
database.execute("INSERT INTO table_name VALUES ('rushang', 21);")
database.execute("INSERT INTO table_name VALUES ('maitri', 22);")

print("data inserted")

datas = database.execute("SELECT * FROM table_name;")
for i in datas:
    print(i)

database.execute("DROP TABLE table_name")
