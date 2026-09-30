import sqlite3
from repositories.spendings_repository import search_spendings, insert_spendings, search_spendings_based_on_month, delete_spendings, edit_spendings

def main():

      menu_actions = {
            's': search_spendings,
            'm': search_spendings_based_on_month,
            'a': insert_spendings,
            'd': delete_spendings,
            'e': edit_spendings
      }

      while True:
            action = input(
                  "\nLets see what happens\n"
                  "(A)dd spendings \n"
                  "(D)elete spendings\n"
                  "(E)dit spendings row\n"
                  "(S)ee all spendings\n"
                  "(M)onthly spesific spendings\n"
                  "(Q)uit \n"
            ).lower().strip()

            if action == 'q':
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