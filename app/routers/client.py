from fastapi import APIRouter, HTTPException
from app.crud.client import create_client, delete_client, get_client, update_client
from app.schemas import Client, ClientCreate

router = APIRouter()

@router.post("/client", response_model=Client)
async def create_client(client: ClientCreate):
    return await create_client(client)

@router.get("/client/{id}", response_model=list[Client])
async def client(id: int):
    client = await get_client(id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/client/{id}", response_model=Client)
async def update_client(id: int, client: ClientCreate):
    return await update_client(id, client)

@router.delete("/client/{id}", response_model=Client)
async def delete_client(id: int):
    return await delete_client(id)