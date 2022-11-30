import sqlite3

con = sqlite3.connect('tutorial.db')
cur = con.cursor()

# cur.execute('CREATE TABLE movie(title,year,score)')
# res = cur.execute('SELECT name FROM sqlite_master')
# print(res.fetchone())
# res = cur.execute('SELECT name FROM sqlite_master WHERE name = "spam"')
# print(res.fetchone() is None)


# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# # con.commit()
# data = [
#     ('Monty Python Live at the Hollywood Bowl', 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany('INSERT INTO movie VALUES(?, ?, ?)', data)
# con.commit()
# res = cur.execute('SELECT score FROM movie')
# print(res.fetchone())
data =[row for row in cur.execute('SELECT title, year, score FROM movie ORDER BY score')]
for i in range(len(data)):
    data[i] = data[i][0] + ', ' + str(data[i][1]) +', ' + str(data[i][2])

for i in enumerate(data,start=1):
    print(str(i))