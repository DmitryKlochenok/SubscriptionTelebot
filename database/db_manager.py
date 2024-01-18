import sqlite3
from ast import literal_eval
import time

import datetime



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
            SET unsub_time='{old_time+2592000}'
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


def get_unsub_date(user_id):
    try:
        with sqlite3.connect("database/sub_db.sqlite") as con:
            cur = con.cursor()
            query = (f"""
               SELECT unsub_time
               FROM sub_table
               WHERE user_id='{user_id}'""")
            cur.execute(query)
            data = cur.fetchone()[0]

        dt_object = datetime.datetime.fromtimestamp(data)
        formatted_date = dt_object.strftime('%Y-%m-%d')

        return formatted_date
    except:
        return None
