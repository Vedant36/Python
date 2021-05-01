# 1
def prime_check(n):
    if n in {0,1}: return False
    for i in range(2, int(n**.5)+1):
        if not n%i:
            return False
    return True
# 2
def palindrome_check(string):
    return string==string[::-1]

# 3
def arrangelements(X):
    return [i for i in X if i<0] + [0]*X.count(0) + [i for i in X if i>0]

# 4
def BinarySearch(x, X):
    if X not in x: return False
    i = [0, len(x)//2, len(x)]
    Y = x[i[1]]
    while X!=Y:
        if X>Y:
            i = [i[1], (i[1]+i[2])//2, i[2]]
        else:
            i = [i[0], (i[0]+i[1])//2, i[1]]
        Y = x[i[1]]
    return i[1]

# 5
def factorial(n):
    if n in {0,1}: return 1
    else: return n * factorial(n-1)

# 6
def fibno(n):
    if n in {0,1}: return n
    return fibno(n-1)+fibno(n-2)

# 7
def count_A_lines(file='story.txt'):
    with open(file, 'r') as fp:
        data = fp.read().split('\n')
        return len([1 for i in data if i[:1]=='A'])

# 8
def DISPLAYWORDS(file='story.txt'):
    with open(file, 'r') as fp:
        data = ' '.join(fp.read().split('\n')).split()
        return sum([0<len(i)<4 for i in data])

# 9
def capitalizer(file):
    with open(file,'r') as fp:
        data = fp.read().split('\n')
        words = [[j.title() for j in i.split(' ')] for i in data]
        write = '\n'.join([' '.join(i) for i in words])
    with open(file,'w') as fp:
        fp.write(write)

# 10
def char_info(file):
    with open(file, 'r') as fp:
        data = fp.read()
        vowels = sum([data.count(i) for i in {'a','e','i','o','u'}])
        upper = len([i for i in data if i.isupper()])
        lower = len([i for i in data if i.islower()])
        consonants = upper + lower - vowels
        print(f'Vowels = {vowels}\nConsonants = {consonants}\nUppercase = {upper}\nLowercase = {lower}')

# 11
def remove_a(file, a_file):
    with open(file, 'r') as fp:
        data = fp.read().split('\n')
        a_write = [i for i in range(len(data)) if 'a' in data[i]]
        a_data = [data.pop(a_write[i]-i) for i in range(len(a_write))]
    with open(file) as fp:
        fp.write('\n'.join(data))
    with open(a_file) as fp:
        fp.write('\n'.join(a_data))

# 12
import pickle as pc
data = {'roll no.': 'name', 1352: 'james', 1345: 'ashley', 1357: 'micheal'}
with open('roll.dat', 'wb') as fp:
    fp.write(pc.dumps(data))
roll = int(input('Enter Roll No.: '))
if roll in data:
    print(f'Name Found: {data[roll]}')
else:
    print('This Roll No. does not match any records.')

# 13
import pickle as pc
data = {'roll no.': 'name', 1352: ['james', 87], 1345: ['ashley', 92], 1357: ['micheal', 89]}
with open('roll.dat','wb') as fp:
    fp.write(pc.dumps(data))
roll = float(input('Enter Roll No.: '))
if roll in data:
    marks = int(input(f'Enter updated marks for {data[roll][0]}: '))
    data[roll][1] = marks
    with open('roll.dat','wb') as fp:
        fp.write(pc.dumps(data))
else:
    print('This Roll No. does not match any records.')

# 14
import csv
data = [['1234','apple','water'],
        ['1345', 'orange','sky']]
with open('app.csv') as fp:
    writer = csv.writer()
    writer.writerows(data)

# 15
import csv
with open('app.csv') as fp:
    writer = csv.writer()
    print('Input entries seperated by commas')
    rows = ','.split(input((f'Input entry {i}: ')))
    writer.writerows(rows)
    roll = input('Enter Roll No.: ')
with open('app.csv', 'r') as fp:
    data = list(csv.reader())[1:]
    if roll in {i[0] for i in data}:
        index = ([i[0] for i in data]).index(roll)
        print(f'Name: {data[index][1]}\nMarks: {data[index][2]}')

# 16
import os
name = input('Enter name of the file: ')
location = input('Enter valid directory to place the file in: ')
with open(os.join(location.strip(), name)): pass

# 17
import os
name = input('Enter name of the directory: ')
location = input('Enter valid location: ')
os.mkdir(os.join(location.strip(), name))

# 18
def push(Books, element):
    Books.append(element)
def pop(Books):
    return Books.pop()

# 19
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='items')
cursor = db.cursor()
cursor.execute('delete from category where name="Stockable";')
db.commit()

# 20
import mysql.connector
data = input('Input comma seperated values for Roll_number, Name, Marks: ')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='student')
cursor = db.cursor()
cursor.execute('create table result(Roll_number int, Name varchar(16), Marks int);')
_data = data.split(',')
cursor.execute(f'insert into result({_data})')
db.commit()
