# import psycopg2
# import mysql.connector
import sqlite3

from dbal.data_store import create_ds, DataStore

# isolation_level=None to disable opening transactions implicitly.
# https://docs.python.org/3/library/sqlite3.html
conn = sqlite3.connect('./todolist.sqlite', check_same_thread=False)  # , isolation_level=None)


# https://stackoverflow.com/questions/15856976/transactions-with-python-sqlite3
# conn.isolation_level = None


# Dependency
def get_ds() -> DataStore:
    ds = create_ds(conn)
    try:
        yield ds
    finally:
        if ds.in_transaction():
            ds.rollback()
