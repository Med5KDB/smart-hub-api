from app.database import get_db_connection
from app.schemas import ClientCreate


def create(client: ClientCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO client (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)", (client.first_name, client.last_name, client.email, client.phone, client.address))
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        raise e

def findOne(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM client WHERE id = %s", (id,))
            result = cursor.fetchone()
            print(f"Récupération réussie ! {result}")
        return result
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        raise e

def findAll(): 
    try: 
        with get_db_connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM client")
                clients = cursor.fetchall()
            return clients
    except Exception as e:
        raise e

def updateOne(id: int, client: ClientCreate):
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE client SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s WHERE id = %s", (client.first_name, client.last_name, client.email, client.phone, client.address, id))
                conn.commit()
                print("Mise à jour réussie !")
            return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        return False

def deleteOne(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM client WHERE id = %s", (id,))
            connection.commit()
            print("Suppression réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return False
        