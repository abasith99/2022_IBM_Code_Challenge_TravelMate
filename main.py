import sqlite3

con = sqlite3.connect('location.db')
c = con.cursor()
cur_time = input("Enter expected time (HH:MM) : ")

sql = f"SELECT location, COUNT(location) AS max_loc FROM (SELECT * FROM history WHERE time = '{cur_time}') GROUP BY location ORDER BY max_loc DESC LIMIT 1"

for ele in c.execute(sql):
    print(f"Predicted location based on historical data : {ele[0]}")
con.commit()
con.close()