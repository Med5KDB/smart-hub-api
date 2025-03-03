from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    position: str

class EmployeeCreate(EmployeeBase):
   pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str

class ClientCreate(ClientBase):
   pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True 
        
        