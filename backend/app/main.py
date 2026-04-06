from fastapi import FastAPI
from routes import tickets, employees

app = FastAPI()

app.include_router(tickets.router)
app.include_router(employees.router)

@app.get("/")
def root():
    return {"message": "AI Ticketing System Running"}
