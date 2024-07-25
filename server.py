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
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['null']  # NOT recommended - see details below
          
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
   return myresult

