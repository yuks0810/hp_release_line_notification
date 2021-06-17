import sqlite3

if __name__ == "__main__":
    dbname = 'hp_release.db'
    conn = sqlite3.connect(f'db/{dbname}')
    cur = conn.cursor()

    conn.commit()
    conn.close()
