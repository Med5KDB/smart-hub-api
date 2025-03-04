from app.database import get_db_connection
from app.schemas import EmployeeCreate, Employee


def create(employee: EmployeeCreate) -> dict[Employee] :
    
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO employee (first_name, last_name, email, position) VALUES (%s, %s, %s, %s)", (employee.first_name, employee.last_name, employee.email, employee.position))
                conn.commit()
                cursor.execute("SELECT * FROM employee WHERE id = LAST_INSERT_ID()")
                created_employee = cursor.fetchone()
                return created_employee
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        return False

def findOne(id: int) -> dict[Employee]:
    
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
                employee = cursor.fetchone()
            return employee
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        raise e

def findAll() -> list[dict[Employee]]:
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM employee")
                employees = cursor.fetchall()
            return employees
    except Exception as e:
        raise e

def updateOne(id: int, employee: EmployeeCreate) -> dict[Employee]:
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("UPDATE employee SET first_name = %s, last_name = %s, email = %s, position = %s WHERE id = %s", (employee.first_name, employee.last_name, employee.email, employee.position, id))
                conn.commit()
                cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
                updated_employee = cursor.fetchone()
                return updated_employee
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        raise e

def deleteOne(id: int) -> int:
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
                conn.commit()
                return id
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        raise e
