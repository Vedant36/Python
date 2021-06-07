#!/usr/bin/env python3
# Imports
import regex
import csv
import time

# Loading book dataset with information of 59695 books collected from amazon.com
with open('../../_Other/datasets/books.csv', 'r') as fp:
    data = list(csv.reader(fp))

# Setting up a hashed table to increase access speed
qwe = dict()
for i in data:
    qwe[i[3]]=i[:3]+i[4:]

# function to search for all books that have some word in it
# multiple words can be input to search for books that contain all those words
def ser(search):
    asd = []
    for i in qwe:
        try:
            search_term = f'\\b({search}){{e<2}}\\b'
            d = regex.search(search_term, f"{i} {qwe[i][3]}", regex.IGNORECASE) # Allowing for 2 letter errors
        except:
            continue
        if d:
            asd.append([i,sum(d.fuzzy_counts)])
    return asd

# Getting input from user
print("                                      \033[1;36mBook Database\033[0m\n")
search = input("\033[0;33mSearch for thousands of Books: \033[0m")
print()

# Timing the search
ini = time.time()
# Sorting obtained list to one where the results on the top have lesser errors
booklist = sorted(ser(search), key=lambda a: (a[1], a[0]))
print(f"\033[0;35mSearched in {time.time()-ini}s\033[0m")
# Printing the First 20 best results Book Information
for i in booklist[:20]:
    val = qwe[i[0]]
    print(f"\033[0;32m{i[0]}\033[0m by \033[0;36m{val[3]}")
print()
