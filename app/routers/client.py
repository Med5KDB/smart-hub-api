from fastapi import APIRouter, HTTPException
from app.crud import create, deleteOne, findOne, updateOne, findAll
from app.schemas import Client, ClientCreate

client_router = APIRouter()

@client_router.post("/client", response_model=Client)
def create_client(client: ClientCreate):
    return create(client)

@client_router.get("/client/{id}", response_model=Client)
def client(id: int):
    client = findOne(id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@client_router.get("/client", response_model=list[Client])
def clients():
    clients = findAll()
    return clients

@client_router.put("/client/{id}", response_model=Client)
def update_client(id: int, client: ClientCreate):
    return updateOne(id, client)

@client_router.delete("/client/{id}", response_model=Client)
def delete_client(id: int):
    return deleteOne(id)