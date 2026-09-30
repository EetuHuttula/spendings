import sqlite3
#get from db

conn = sqlite3.connect("db.db")
cur = conn.cursor()

def search_spendings():
    rows = cur.execute("SELECT month, amount, description from spendings").fetchall()

    print("-" * 40)
    print(f"{'Kuukausi':<12} {'Määrä':>10}  {'Kuvaus'}")
    print("-" * 40)

    for month, amount, description in rows:
        print(f"{month:<12} {amount:>9.2f} €  {description}")

def search_spendings_based_on_month():
    month = input("Enter month: ")
    rows = cur.execute("""
        SELECT month, SUM(amount)
        FROM spendings
        WHERE month = ?
    """, (month,))
    month, amount = rows.fetchone()

    print("-"*20)
    print("Koko kuukauden menot")
    print("-"*20)
    print(f"{month} {amount:>9.2f} €")

def  insert_spendings():

    month = input("Enter month: ")
    amount = int(input("Amount spent:"))
    desc = input("decsription: ")

    cur.execute("""
        INSERT INTO spendings (month, description, amount) values (?, ?, ?)
    """, (month, desc, amount))
    conn.commit()

def delete_spendings():
    rows = cur.execute("SELECT id, month, amount, description from spendings").fetchall()
    
    print("-" * 40)
    print(f"{'id'} {'Kuukausi':<12} {'Määrä':>10}  {'Kuvaus'}")
    print("-" * 40)

    for id, month, amount, description in rows:
        print(f"{id} {month:<12} {amount:>9.2f} €  {description}")

    print("Mikä rivi poistetaan?")
    del_input = int(input("Kirjoita rivin numero: "))

    cur.execute("""DELETE FROM spendings where id = ?""", (del_input,))
    conn.commit()

def edit_spendings():
    rows = cur.execute(
        "SELECT id, month, amount, description FROM spendings"
    ).fetchall()

    print("-" * 55)
    print(f"{'ID':<4} {'Kuukausi':<12} {'Määrä':>10}  {'Kuvaus'}")
    print("-" * 55)

    for id, month, amount, description in rows:
        print(f"{id:<4} {month:<12} {amount:>9.2f} €  {description}")

    print("-" * 20)

    try:
        edit_input = int(input("Kirjoita muokattavan rivin numero: "))
    except ValueError:
        print("Anna kelvollinen rivinumero.")
        return

    row = cur.execute(
        """
        SELECT month, amount, description
        FROM spendings
        WHERE id = ?
        """,
        (edit_input,)
    ).fetchone()

    old_month, old_amount, old_description = row


    edit_month = input(f"Kuukausi [{old_month}]: ")
    edit_amount = input(f"Määrä [{old_amount:.2f}]: ")
    edit_description = input(f"Kuvaus [{old_description}]: ")

    edit_month = edit_month or old_month
    edit_amount = float(edit_amount) if edit_amount else old_amount
    edit_description = edit_description or old_description

    cur.execute(
        """
        UPDATE spendings
        SET month = ?, amount = ?, description = ?
        WHERE id = ?
        """,
        (edit_month, edit_amount, edit_description, edit_input)
    )

    conn.commit()
