[![CI](https://github.com/EetuHuttula/spendings/actions/workflows/main.yml/badge.svg)](https://github.com/EetuHuttula/spendings/actions/workflows/main.yml) [![codecov](https://codecov.io/gh/EetuHuttula/spendings/graph/badge.svg?token=GL2H63CQZF)](https://codecov.io/gh/EetuHuttula/spendings)

# Spendings MVP

A simple Python CLI application for tracking personal spendings.

## Current MVP scope

- Add a spending entry (month, amount, description)
- List all spendings
- Show monthly total by month
- Edit an existing spending
- Delete a spending
- Persist data in a local SQLite database (`db.db`)

> Note: The current version is CLI-based. A PySide6 GUI can be added later on top of this MVP.

## Tech stack

- Python 3.12
- SQLite
- Poetry (recommended)
- Pytest (tests)

## Getting started

### 1) Clone the repository

```bash
git clone https://github.com/EetuHuttula/spendings.git
cd spendings
```

### 2) Install dependencies

With Poetry:

```bash
poetry install
```

Or with pip:

```bash
pip install -r requirements.txt
```

## Run the application

With Poetry:

```bash
poetry run python src/app.py
```

Without Poetry:

```bash
python src/app.py
```

## Run tests

With Poetry:

```bash
poetry run pytest
```

Without Poetry:

```bash
pytest
```

## Project structure

```text
src/
├── app.py                    # CLI entry point
├── db.py                     # SQLite connection and initialization
├── cli/spendigs_cli.py       # CLI actions and prompts
├── repositories/
│   └── spendings_repository.py
└── tests/
    └── spendings_repository_test.py
```
