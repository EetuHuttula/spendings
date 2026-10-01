import sqlite3
import pytest
from repositories.spendings_repository import SpendingsRepository


@pytest.fixture
def repository(tmp_path):
    db_path = tmp_path / "test.db"

    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE spendings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month VARCHAR(10),
            description VARCHAR,
            amount INTERGER,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    repository = SpendingsRepository(conn)

    yield repository

    conn.close()


def test_insert_spending(repository):
    spending_id = repository.insert_spending(
        "September",
        25.50,
        "Groceries"
    )

    assert spending_id == 1

    spending = repository.get_spending(spending_id)

    assert spending[:4] == (
        1,
        "September",
        25.50,
        "Groceries",
    )
    assert spending[4] is not None

def test_get_spending(repository):
    spending_id = repository.insert_spending(
        "October",
        100.00,
        "Electronics"
    )

    spending = repository.get_spending(spending_id)

    assert spending[:4] == (
        1,
        "October",
        100.00,
        "Electronics",
    )
    assert spending[4] is not None

def test_delete_spending(repository):
    spending_id = repository.insert_spending(
        "November",
        50.00,
        "Clothing"
    )

    repository.delete_spending(spending_id)

    spending = repository.get_spending(spending_id)

    assert spending is None

def test_edit_spending(repository):
    spending_id = repository.insert_spending(
        "December",
        75.00,
        "Gifts"
    )

    repository.edit_spending(
        spending_id,
        "December",
        80.00,
        "Holiday Gifts"
    )

    spending = repository.get_spending(spending_id)

    assert spending[:4] == (
        1,
        "December",
        80.00,
        "Holiday Gifts",
    )
    assert spending[4] is not None

def test_search_spendings(repository):
    repository.insert_spending(
        "January",
        30.00,
        "Books"
    )
    repository.insert_spending(
        "February",
        45.00,
        "Restaurant"
    )

    spendings = repository.search_spendings()

    assert len(spendings) == 2
    assert spendings[0][:4] == (
        1,
        "January",
        30.00,
        "Books",
    )
    assert spendings[1][:4] == (
        2,
        "February",
        45.00,
        "Restaurant",
    )