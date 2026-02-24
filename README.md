# Expense Tracker Application

A simple Python command-line expense management system that allows users to track daily expenses, categorize them, and view monthly summaries. Data is stored using file handling for persistent storage.

## Features

- Add new expenses
- Categorize expenses (Food, Travel, etc.)
- View all recorded expenses
- View total expenses
- Generate monthly summary
- Persistent storage using text file

## Technologies Used

- Python
- File Handling
- Basic Data Processing
- Modular Functions

## Data Format

Expenses are stored in this format:

date,category,amount,description

Example:
2026-02-24,Food,250,Lunch

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run:

python main.py

## Project Structure

expense-tracker-python/
│
├── main.py
├── expenses.txt
└── README.md
