import mysql.connector

# Assuming the password to be 1234
db = mysql.connector.connect(host='localhost', user='root', password='1234')
cur = db.cursor()
cur.execute('create database if not exists company_info;')
cur.execute('use company_info;')
cur.execute('drop table if exists Employee;')
cur.execute('create table Employee(Emp_ID int primary key, Emp_Name varchar(32), Emp_Salary int, Emp_Dept varchar(9));')
data = ['12, "Aman", 23000,"HR"',
		'31, "Micheal", 12000, "Marketing"',
		'35, "Ramesh", 42000, "Marketing"',
		'36, "Me", 97000, "IT"']
for i in data:
	cur.execute(f"insert into Employee values({i});")
Emp_ID = input("Enter Employee ID to delete: ")
cur.execute(f"delete from Employee where Emp_ID={Emp_ID};")
cur.execute('select * from Employee;')
print(' Emp_ID | Emp_Name | Emp_Salary | Emp_Dept')
print('-'*44)
for i in cur:
	print(f'   {i[0]}      {i[1]:^7}     {i[2]}      {i[3]:^9}')
db.commit()