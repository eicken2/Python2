import sqlite3 as sq

conn = sq.connect('ch17/books.db')
c = conn.cursor()
c.execute("SELECT * FROM titles")
table = [[]]
other = c.fetchall()
for i in range(4):
    table[0].append(c.description[i][0])
        
for j in range(10):
    newbook = []
    for k in range(4):
        newbook.append(other[j][k])
    table.append(newbook)

for m in range(11):
    table[m][0] = table[m][0].ljust(12, " ")
    table[m][1] = table[m][1].ljust(35, " ")
    table[m][2] = str(table[m][2]).ljust(8, " ")
    table[m][3] = table[m][3].ljust(5, " ")

#print(table)
for book in table:
    print(book)