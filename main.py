from fastapi import FastAPI
import pymysql

app = FastAPI()
database = pymysql.connect(host='ls-6f6b1bdf222c6272937f29acbec7a2ff849ee97e.cvwytoppvggs>
cursor = database.cursor(pymysql.cursors.DictCursor) 

@app.get("/createid")
async def createid(FN:str = "", LN:str = "", DoB:str = "", pd:str = ""):
cursor.execute("insert into PATIENT_INFO (First_Name, Last_Name, Date_of_Birth, P>
database.commit()

