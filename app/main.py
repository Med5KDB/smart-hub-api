from fastapi import FastAPI
from app.routers import client_router, employee_router
import uvicorn

app = FastAPI()

app.include_router(client_router)
app.include_router(employee_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartHub API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)