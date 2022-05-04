import sqlite3
from os import path

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
loc = ['loc_A', 'loc_B', 'loc_C', 'loc_D', 'loc_E', 'loc_F']
time = [['09:30', '10:00', '10:30', '11:00', '11:30', '12:00'],
        ['09:30', '10:00', '11:00', '11:30', '12:30', '13:00'],
        ['09:00', '09:30', '10:00', '11:00', '11:30', '12:30'],
        ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00'],
        ['09:30', '10:30', '11:00', '11:30', '12:00', '12:30'],
        ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30']]

if not path.exists('location.db'):
    con = sqlite3.connect('location.db')
    c = con.cursor()
    c.execute("CREATE TABLE history(user text, location text, time text)")
    con.commit()

    i, j = 0, 0
    for name in users:
        count, i = 6, 0
        while(count > 0):
            c.execute("INSERT INTO history VALUES('%s', '%s', '%s')"%(name, loc[i], time[j][i]))
            con.commit()
            count -= 1
            i += 1
        j += 1
else:
    con = sqlite3.connect('location.db')
    c = con.cursor()
    print("|  USER | Time |Location|\n+-----------------------+")
    for ele in c.execute("SELECT user, time, location FROM history"):
        print(f"+ {ele[0]} | {ele[1]} | {ele[2]} +")
        print("+-----------------------+")

con.close()