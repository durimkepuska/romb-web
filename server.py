import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="menu"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ushqimet")

myresult = mycursor.fetchall()


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return myresult

