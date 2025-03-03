from fastapi import APIRouter, HTTPException
from app.crud.employee import create_employee, delete_employee, get_employee, update_employee
from app.schemas import Employee, EmployeeCreate

router = APIRouter()

@router.post("/employee", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    return await create_employee(employee)

@router.get("/employee/{id}", response_model=list[Employee])
async def employee(id: int):
    employee = await get_employee(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/employee/{id}", response_model=Employee)
async def update_employee(id: int, employee: EmployeeCreate):
    return await update_employee(id, employee)

@router.delete("/employee/{id}", response_model=Employee)
async def delete_employee(id: int):
    return await delete_employee(id)