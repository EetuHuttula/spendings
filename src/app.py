import sqlite3
from db import create_connection, initialize_database
from repositories.spendings_repository import SpendingsRepository
from cli.spendigs_cli import show_spendings, add_spending, search_by_month, edit_spending, delete_spending


def main():
    conn = create_connection()

    initialize_database(conn)

    repository = SpendingsRepository(conn)

    while True:
        print()
        print("===== SPENDINGS =====")
        print("1. Näytä menot")
        print("2. Lisää meno")
        print("3. Näytä kuukauden menot")
        print("4. Muokkaa menoa")
        print("5. Poista meno")
        print("6. Lopeta")

        choice = input("Valitse: ")

        if choice == "1":
            show_spendings(repository)

        elif choice == "2":
            add_spending(repository)

        elif choice == "3":
            search_by_month(repository)

        elif choice == "4":
            edit_spending(repository)

        elif choice == "5":
            delete_spending(repository)

        elif choice == "6":
            print("Moikka!")
            break

        else:
            print("Virheellinen valinta.")

    conn.close()


if __name__ == "__main__":
    main()