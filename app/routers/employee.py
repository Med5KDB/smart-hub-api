from fastapi import APIRouter, HTTPException
from app.crud.__init__ import createEmployee, deleteEmployee, findEmployee, updateEmployee
from app.schemas import Employee, EmployeeCreate

employee_router = APIRouter()

@employee_router.post("/employee", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    return await createEmployee(employee)

@employee_router.get("/employee/{id}", response_model=list[Employee])
async def employee(id: int):
    employee = await findEmployee(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@employee_router.put("/employee/{id}", response_model=Employee)
async def update_employee(id: int, employee: EmployeeCreate):
    return await updateEmployee(id, employee)

@employee_router.delete("/employee/{id}", response_model=Employee)
async def delete_employee(id: int):
    return await deleteEmployee(id)