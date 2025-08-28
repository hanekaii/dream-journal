import sqlite3

try:
    conn = sqlite3.connect(":memory:")  # in-memory test DB
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            tags TEXT
        )
    ''')
    cursor.execute("INSERT INTO dreams (date, description, tags) VALUES ('2025-08-27', 'Test dream', 'test')")
    cursor.execute("SELECT * FROM dreams")
    rows = cursor.fetchall()
    assert len(rows) == 1
    print("Test passed!")
except Exception as e:
    print("Test failed:", e)
finally:
    conn.close()