import sqlite3 as sq

conn = sq.connect('ch17/books.db')
c = conn.cursor()
c.execute("SELECT * FROM authors ORDER BY last DESC")
#print(c.fetchall())
c.execute("SELECT * FROM titles ORDER BY title")
#print(c.fetchall())
c.execute("SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_isbn ON author_isbn.isbn = titles.isbn ORDER BY title")
#print(c.fetchall())
c.execute("INSERT INTO authors (first, last) VALUES ('Brandon', 'Sanderson')")
c.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES ('0765350386', 'Mistborn', '3', '2006')")
c.execute("INSERT INTO author_isbn (id, isbn) VALUES ('6', '0765350386')")
c.execute("SELECT * FROM titles")

print(c.fetchall())