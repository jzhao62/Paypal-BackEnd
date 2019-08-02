import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def display_all_accounts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def _login(conn, user, pwd):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user where username = '%s' and password = '%s'" % (user, pwd))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def _register(conn, user):
    cur = conn.cursor()
    cur.execute("SELECT * FROM user where username = '%s' " % (user))
    row = cur.fetchone()

    if(cur != None):
        #insert
    else:
        # report error




def main():
    database = "account"

    # create a database connection
    conn = create_connection(database)
    with conn:
       # _login(conn, 'admin','admin')
       _register(conn, 'admin')


if __name__ == '__main__':
    main()