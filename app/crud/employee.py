from app.database import get_db_connection
from app.schemas import EmployeeCreate


def create(employee: EmployeeCreate):
    
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO employee (first_name, last_name, email, position) VALUES (%s, %s, %s, %s)", (employee.first_name, employee.last_name, employee.email, employee.position))
                conn.commit()
                print("Insertion réussie !")
            return True
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        return False

def findOne(id: int):
    
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
                result = cursor.fetchone()
                print(f"Récupération réussie ! {result}")
            return result
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        return None

def updateOne(id: int, employee: EmployeeCreate):
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("UPDATE employee SET first_name = %s, last_name = %s, email = %s, position = %s WHERE id = %s", (employee.first_name, employee.last_name, employee.email, employee.position, id))
                conn.commit()
                print("Mise à jour réussie !")
            return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        return False

def deleteOne(id: int):
    try:
        with get_db_connection() as conn: 
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
                conn.commit()
                print("Suppression réussie !")
            return True
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return False
