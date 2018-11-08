import mysql.connector

import secrets

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database=""
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pickem_matches")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
