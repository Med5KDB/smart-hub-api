from app.database import get_db_connection
from app.schemas import EmployeeCreate


def create_employee(employee: EmployeeCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO employee (first_name, last_name, email, position) VALUES (%s, %s, %s, %s)", (employee.first_name, employee.last_name, employee.email, employee.position))
            connection.commit()
            print("Insertion réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        return False
    finally:
        connection.close()

def get_employee(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
            result = cursor.fetchone()
            print(f"Récupération réussie ! {result}")
        return result
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        return None
    finally:
        connection.close()

def update_employee(id: int, employee: EmployeeCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE employee SET first_name = %s, last_name = %s, email = %s, position = %s WHERE id = %s", (employee.first_name, employee.last_name, employee.email, employee.position, id))
            connection.commit()
            print("Mise à jour réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        return False
    finally:
        connection.close()

def delete_employee(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
            connection.commit()
            print("Suppression réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return False
    finally:   
        connection.close()