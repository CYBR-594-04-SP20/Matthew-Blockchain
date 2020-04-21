import sqlite3

with sqlite3.connect("blockchain.db") as connection:
    c = connection.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL);
    """)
    c.execute('''
    INSERT INTO user(username, firstname, lastname, password)
    VALUES("test_User", "Matt", "Fong", "password")
    ''')
    connection.commit()
