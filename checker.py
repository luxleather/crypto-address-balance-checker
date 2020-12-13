#!/usr/bin/python

import sqlite3
import re
import requests
import time

#Config
EXPLORER = "https://explorer.teloscoin.org/"

#Initialize database
db = sqlite3.connect('addresses.db')
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(address TEXT, bal INTEGER)')
db.commit()

#Menu
print("What you want to do?")
print("1 - Load file to database")
print("2 - List database")
one = input("Choose option: ")

if one == "1":
    #Open txt file with list of addresses
    with open("addr.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            args = stripped_line
            time.sleep(2)

            try:
                if len(str(args)) == 34:

                    bal = requests.get("{}ext/getbalance/{}".format(EXPLORER, args)).json()

                    db = sqlite3.connect('addresses.db')
                    c = db.cursor()
                    c.execute('INSERT INTO users(address, bal) VALUES(?,?)', (str(args), str(bal)))

                    db.commit()
                    db.close()

            except requests.exceptions.RequestException:
                print('error')


if one == "2":
    db = sqlite3.connect('addresses.db')
    c = db.cursor()
    c.execute('SELECT * FROM users')
    usr = c.fetchall()
    for raw in usr:
        print(raw [0],' = ', raw[1])
    db.close()
