import sqlite3


def retrieve_bots():
    db = sqlite3.connect("Bots.db")
    cursor = db.cursor()

    sql = "SELECT * FROM bots;"
    cursor.execute(sql)

    record = cursor.fetchall()
    db.close()

    print(record)


def run():
    retrieve_bots()


if __name__ == "__main__":
    run()