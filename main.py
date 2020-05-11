

from fastapi import FastAPI
import sqlite3


app = FastAPI()

@app.get('/')
def root():
	return {"message": "Hello World during the coronavirus pandemic!"}


@app.on_event("startup")
async def startup():
	app.db_connection = sqlite3.connectin('chinook.db')

@app.on_event("shutdown")
async def shutdown():
	app.db_connection.close()

@app.get('/tracks')
async def tracks(page: int=0, per_page: int=10):
	app.db_connection.row_factory = sqlite3.Row
	data = app.db_connection.execute(f"SELECT * FROM tracks ORDER BY trackid LIMIT {page} OFFSET {page*per_page}").fetchall()
	return data

