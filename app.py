import sqlite3
from repositories.spendings_repository import search_spendings, insert_spendings

def main():

      menu_actions = {
            's': search_spendings,
            'a': insert_spendings
      }

      while True:
            action = input(
                  "\nLets see what happens\n"
                  "(S)pendings  \n"
                  "(A)dd spendings \n"
                  "(Q)uit \n"
            ).lower().strip()

            if action == 'q':
                  print("stopping")
                  break 
            actions = menu_actions.get(action)
            if actions:
                  actions()
            else:
                  print("invalid choice")

if __name__ == "__main__":
    print("Hello! Welcome")
    try:
        main()
        if main():
            conn = sqlite3.connect("db.db")
            conn.close()
    except KeyboardInterrupt:
        print("\nInterrupted! Saving data and exiting...")
        print("Data saved. Goodbye!")           