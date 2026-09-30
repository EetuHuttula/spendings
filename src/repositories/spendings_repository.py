class SpendingsRepository:

    def __init__(self, conn):
        self.conn = conn

    def search_spendings(self):
        return self.conn.execute("""
            SELECT id, month, amount, description, time
            FROM spendings
            ORDER BY id
        """).fetchall()

    def search_spendings_based_on_month(self, month):
        return self.conn.execute("""
            SELECT month, SUM(amount)
            FROM spendings
            WHERE month = ?
            GROUP BY month
        """, (month,)).fetchone()

    def insert_spending(self, month, amount, description):
        cursor = self.conn.execute("""
            INSERT INTO spendings
                (month, description, amount)
            VALUES (?, ?, ?)
        """, (month, description, amount))

        self.conn.commit()

        return cursor.lastrowid

    def get_spending(self, spending_id):
        return self.conn.execute("""
            SELECT id, month, amount, description, time
            FROM spendings
            WHERE id = ?
        """, (spending_id,)).fetchone()

    def delete_spending(self, spending_id):
        self.conn.execute("""
            DELETE FROM spendings
            WHERE id = ?
        """, (spending_id,))

        self.conn.commit()

    def edit_spending(
        self,
        spending_id,
        month,
        amount,
        description
    ):
        self.conn.execute("""
            UPDATE spendings
            SET month = ?,
                amount = ?,
                description = ?
            WHERE id = ?
        """, (
            month,
            amount,
            description,
            spending_id
        ))

        self.conn.commit()