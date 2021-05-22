"""
    Author: Albert Dinh

    This file deals with database using SQLite3.

"""

import sqlite3
import purchases

def make_table(conn, cret):
    """ This will make a table of purchases

    Arguments:
        conn (sqlite3): a connection to database

    Returns:
        None
    """
    with conn:
        cret.execute("""CREATE TABLE purchases (
            name_item text,
            price real,
            status text,
            date text)""")


def insert_item(conn, cret, an_item):
    conn = conn
    if an_item.on_off_value():
        status_var = 'In-store'
    elif not(an_item.on_off_value()):
        status_var = 'Ordered Online'
    name = an_item.get_item_name()
    price = an_item.get_price()
    time = an_item.get_time()
    with conn:
        cret.execute("INSERT INTO purchases VALUES (:name_item, :price, :status, :date)", 
        {'name_item': name, 
        'price': price, 
        'status': status_var, 
        'date': time})


def fetch_all(cret):
    """ Get all the items in the table purchases
    """
    cret.execute("SELECT rowid, * FROM purchases")
    items = cret.fetchall()
    for item in items:
        print(item)


def get_cursor():
    """ Get a connection to the database
    """
    c = sqlite3.connect("purchases.db")
    cret = c.cursor()
    return c, cret