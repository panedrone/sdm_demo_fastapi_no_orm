# import psycopg2
# import mysql.connector
import sqlite3

from dbal.data_store import create_ds, DataStore

# isolation_level=None to disable opening transactions implicitly.
# https://docs.python.org/3/library/sqlite3.html
conn = sqlite3.connect('./todolist.sqlite', check_same_thread=False)  # , isolation_level=None)

# === panedrone: no "conn.autocommit" in sqlite3, but it behaves like conn.autocommit = False
# conn.autocommit = False

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


# ----------------------------------------------------------------------------------------------------
#
# ============= Below are examples for PostgreSQL, MySQL, and Oracle: =============
#
# ----------------------------------------------------------------------------------------------------
#
# using this  https://github.com/panedrone/sqldalmaker/blob/master/src/resources/data_store_no_orm.py
#
# import psycopg2
#
# from dbal.data_store import create_ds, DataStore
#
# conn = psycopg2.connect(host="127.0.0.1", database="my_tests", user="postgres", password="sa")
#
# # https://pynative.com/python-mysql-transaction-management-using-commit-rollback/
# conn.autocommit = False
#
#
# # Dependency
# def get_ds() -> DataStore:
#     ds = create_ds(conn)
#     try:
#         yield ds
#     except Exception as e:
#         ds.rollback()  # there is no "in_transaction" in psycopg2
#         raise e
#
# ----------------------------------------------------------------------------------------------------
#
# using this  https://github.com/panedrone/sqldalmaker/blob/master/src/resources/data_store_no_orm.py
#
# import mysql.connector
#
# from dbal.data_store import create_ds, DataStore
#
#
# # Dependency
# def get_ds() -> DataStore:
#
#     # === panedrone:
#     #
#     #   no way to make it working other than new connection on each handler, but...
#     #   it seems like there is some pooling exists: from .pooling import connect
#
#     conn = mysql.connector.Connect(user='root', password='sa', host='127.0.0.1', database='todolist')
#
#     conn.autocommit = False
#
#     ds = create_ds(conn)
#
#     try:
#         # === panedrone:
#         #
#         #   in mysql, "conn.autocommit = False" means starting transaction by the very first SQL independently of SQL type
#
#         yield ds
#
#     finally:
#
#         if ds.in_transaction():
#             ds.rollback()
#
# ----------------------------------------------------------------------------------------------------
#
# using this  https://github.com/panedrone/sqldalmaker/blob/master/src/resources/data_store_no_orm_cx_oracle.py
#
# import cx_Oracle
#
# from dbal.data_store import create_ds, DataStore
#
# conn = cx_Oracle.connect('MY_TESTS', 'sa', 'localhost:1521/xe', encoding='UTF-8')
#
# conn.autocommit = False
#
#
# def get_oracle_version():
#     return conn.version
#
#
# # Dependency
# def get_ds() -> DataStore:
#     ds = create_ds(conn)
#     try:
#         yield ds
#     except Exception as e:
#         ds.rollback()
#         raise e

