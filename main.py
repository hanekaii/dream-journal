from datetime import date
import sqlite3

running = True


def add_dream():
    current_date = date.today()
    print("Date: " + str(current_date))

    dream_date = input("Enter dream date (YYYY-MM-DD) or press Enter to use today: ")
    if dream_date.strip() == "":
        dream_date = str(current_date)


    dream_description = input("Describe your dream: ")


    dream_tags = input("Add dream tags (comma-separated): ")

    conn = qlite3.connect("dreams.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            tags TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO dreams (date, description, tags)
        VALUES (?, ?, ?)
    ''', (dream_date, dream_description, dream_tags))

    conn.commit()
    conn.close()

def view_all_dreams():
    print("test")

def search_dreams():
    print("test2")

while running:
    print('Menu:\n1. Add a Dream\n2. View \n3. Search Dreams \n4. Exit')
    user_input = input()

    if user_input == 1:
        add_dream()
    elif user_input == 2:
        view_all_dreams()
    elif user_input == 3:
        search_dreams()
    elif user_input == 4:
        print("Bye!")
        running = False
    else:
        print("Invalid choice, try again.")
        
