from fastapi import APIRouter, HTTPException
from app.crud import create, deleteOne, findOne, updateOne
from app.schemas import Client, ClientCreate

client_router = APIRouter()

@client_router.post("/client", response_model=Client)
async def create_client(client: ClientCreate):
    return await create(client)

@client_router.get("/client/{id}", response_model=list[Client])
async def client(id: int):
    client = await findOne(id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@client_router.put("/client/{id}", response_model=Client)
async def update_client(id: int, client: ClientCreate):
    return await updateOne(id, client)

@client_router.delete("/client/{id}", response_model=Client)
async def delete_client(id: int):
    return await deleteOne(id)