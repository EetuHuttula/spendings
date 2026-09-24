#import sqlite3

#conn = sqlite3.connect("db.db")
#cur = conn.cursor()
#cur.execute('INSERT INTO person (name, age) VALUES (?, ?)',
#            ('Aapeli', 26 ))
#conn.commit()

#cur.execute('SELECT name, description, amount FROM spendings INNER JOIN users ON spendings.user_id = users.id WHERE month = "helmikuu"')
#data = cur.fetchall()
#print(data)
#conn.close


