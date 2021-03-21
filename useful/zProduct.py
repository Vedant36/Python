
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="vedant36",
    password="1qaz@WSX",
    database="db0")

cursor = db.cursor()

# cursor.execute("""create table if not exists Bye(
#     Product_ID integer, 
#     pro_name varchar(16),
#     pro_qty integer,
#     pro_price float(2) );""")
# data = "1234, 'apple', 3, 6"#input("Enter data in the format: Product_ID, pro_name, pro_qty, pro_price\n")
# cursor.execute(f"insert into Bye values({data});")
cursor.execute("select * from Bye;")

for i in cursor:
	print(i)

db.commit()