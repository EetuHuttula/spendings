def show_spendings(repository):
    rows = repository.search_spendings()

    if not rows:
        print("Ei menoja.")
        return

    print("-" * 60)
    print(f"{'ID':<4} {'Kuukausi':<12} {'Määrä':>10}  {'Kuvaus'}")
    print("-" * 60)

    for spending_id, month, amount, description, time in rows:
        print(
            f"{spending_id:<4} "
            f"{month:<12} "
            f"{amount:>9.2f} €  "
            f"{description}"
        )

    print("-" * 60)


def add_spending(repository):
    month = input("Kuukausi: ")

    try:
        amount = float(input("Määrä: "))
    except ValueError:
        print("Anna kelvollinen summa.")
        return

    description = input("Kuvaus: ")

    repository.insert_spending(
        month,
        amount,
        description
    )

    print("Meno lisätty!")


def search_by_month(repository):
    month = input("Kuukausi: ")

    result = repository.search_spendings_based_on_month(month)

    if result is None:
        print("Kuukaudelta ei löytynyt menoja.")
        return

    month, amount = result

    print("-" * 30)
    print("Koko kuukauden menot")
    print("-" * 30)
    print(f"{month}: {amount:.2f} €")


def delete_spending(repository):
    show_spendings(repository)

    try:
        spending_id = int(
            input("Poistettavan menon ID: ")
        )
    except ValueError:
        print("Anna kelvollinen ID.")
        return

    spending = repository.get_spending(spending_id)

    if spending is None:
        print("Menoa ei löytynyt.")
        return

    repository.delete_spending(spending_id)

    print("Meno poistettu!")


def edit_spending(repository):
    show_spendings(repository)

    try:
        spending_id = int(
            input("Muokattavan menon ID: ")
        )
    except ValueError:
        print("Anna kelvollinen ID.")
        return

    spending = repository.get_spending(spending_id)

    if spending is None:
        print("Menoa ei löytynyt.")
        return

    _, old_month, old_amount, old_description, _ = spending

    month = input(
        f"Kuukausi [{old_month}]: "
    )

    amount = input(
        f"Määrä [{old_amount:.2f}]: "
    )

    description = input(
        f"Kuvaus [{old_description}]: "
    )

    month = month or old_month
    description = description or old_description

    if amount:
        try:
            amount = float(amount)
        except ValueError:
            print("Anna kelvollinen summa.")
            return
    else:
        amount = old_amount

    repository.edit_spending(
        spending_id,
        month,
        amount,
        description
    )

    print("Meno muokattu!")
