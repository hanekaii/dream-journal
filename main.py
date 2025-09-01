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


    dream_tags = input("Add dream tags (comma-separated, e.g., flying, teeth): ")

    conn = sqlite3.connect("dreams.db")
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
    conn = sqlite3.connect("dreams.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dreams")
    rows = cursor.fetchall()

    if not rows:
            print("No dreams recorded yet.")
    else:
        for row in rows:
            print("-------------------------")
            print(f"DreamID: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Desc: {row[2]}")
            print(f"Tags: {row[3]}")
            print("-------------------------")

    conn.close()



def search_dreams():
    search_tags = input("Enter tags to search for (comma-separated): ")
    search_tags = [tag.strip().lower() for tag in search_tags.split(",") if tag.strip()] #lowercases

    conn = sqlite3.connect("dreams.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM dreams WHERE " + " OR ".join(["tags LIKE ?" for _ in search_tags])
    params = [f"%{tag}%" for tag in search_tags]
    cursor.execute(query, params)
    results = cursor.fetchall()

    if not results:
            print("No dreams recorded yet.")
    else:
        for row in results:
            print("-------------------------")
            print(f"DreamID: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Desc: {row[2]}")
            print(f"Tags: {row[3]}")
            print("-------------------------")


while running:
    print('Menu:\n1. Add a Dream\n2. View \n3. Search Dreams \n4. Exit \n')
    user_input = input()

    if user_input == '1':
        add_dream()
    elif user_input == '2':
        view_all_dreams()
    elif user_input == '3':
        search_dreams()
    elif user_input == '4':
        print("Bye!")
        running = False
    else:
        print("Invalid choice, try again.")
        
