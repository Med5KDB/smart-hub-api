from fastapi import APIRouter, HTTPException
from app.crud.__init__ import createEmployee, deleteEmployee, findEmployee, updateEmployee
from app.schemas import Employee, EmployeeCreate

employee_router = APIRouter()

@employee_router.post("/employee", response_model=Employee)
def create_employee(employee: EmployeeCreate):
    return createEmployee(employee)

@employee_router.get("/employee/{id}", response_model=list[Employee])
def employee(id: int):
    employee = findEmployee(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@employee_router.put("/employee/{id}", response_model=Employee)
def update_employee(id: int, employee: EmployeeCreate):
    return updateEmployee(id, employee)

@employee_router.delete("/employee/{id}", response_model=Employee)
def delete_employee(id: int):
    return deleteEmployee(id)