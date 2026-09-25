import sqlite3
#get from db

conn = sqlite3.connect("db.db")
cur = conn.cursor()

def search_spendings():

    user_id = input("Enter user ID: ")
    month = input("Enter month: ")

    cur.execute("""
        SELECT users.name, spendings.description, SUM(spendings.amount)
        FROM spendings
        INNER JOIN users ON spendings.user_id = users.id
        WHERE spendings.month = ?
        AND spendings.user_id = ? """
    , (month, user_id))
    data = cur.fetchall()
    print(data)

def  insert_spendings():

    user_id = input("Enter user ID: ")
    month = input("Enter month: ")
    amount = int(input("Amount spent:"))
    desc = input("decsription: ")

    cur.execute("""
        INSERT INTO spendings (month, user_id, description, amount) values (?, ?, ?, ?)
    """, (month, user_id, desc, amount))
    conn.commit()