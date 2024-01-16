import sqlite3
from ast import literal_eval
import time



def create_database():
    with sqlite3.connect("sub_db.sqlite") as con:
        cur = con.cursor()

        query = ("""
        CREATE TABLE sub_table(
        user_id integer,
        unsub_time integer
        )""")
        cur.execute(query)


def add_user(user_id, unsub_time):
    with sqlite3.connect("database/sub_db.sqlite") as con:
        cur = con.cursor()
        query = (f"""
           SELECT user_id
           FROM sub_table
           WHERE user_id='{user_id}'""")
        cur.execute(query)
        users = cur.fetchone()
    if users is None:
        with sqlite3.connect("database/sub_db.sqlite") as con:
            cur = con.cursor()
            query = (f"""
            INSERT INTO sub_table (user_id, unsub_time)
            VALUES ({user_id}, {unsub_time})""")
            cur.execute(query)
    else:
        with sqlite3.connect("database/sub_db.sqlite") as con:
            cur = con.cursor()
            query = (f"""
               SELECT unsub_time
               FROM sub_table
               WHERE user_id='{user_id}'""")
            cur.execute(query)
            old_time = cur.fetchone()[0]
        with sqlite3.connect("database/sub_db.sqlite") as con: #2592000 для месяца
            cur = con.cursor()
            query = (f"""
            UPDATE sub_table
            SET unsub_time='{old_time+40}'
            WHERE user_id='{user_id}'""")
            cur.execute(query)


def show_expired():
    with sqlite3.connect("database/sub_db.sqlite") as con:
        cur = con.cursor()
        query = (f"""
           SELECT user_id, unsub_time
           FROM sub_table""")
        cur.execute(query)
        data = cur.fetchall()

    unsub = []
    subbed = []
    for user in data:
        if user[1]<time.time():
            unsub.append(user[0])
        else:
            subbed.append(user[0])
    print("unsub: ", unsub)
    print("subbed: ", subbed)
    return unsub, subbed


def unsub_list(users):
    for user in users:
        with sqlite3.connect("database/sub_db.sqlite") as con:
            cur = con.cursor()
            query = (f"""
               DELETE
               FROM sub_table
               WHERE user_id="{user}" """)
            cur.execute(query)



