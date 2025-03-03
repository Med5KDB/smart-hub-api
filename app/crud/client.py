from app.database import get_db_connection
from app.schemas import ClientCreate


def create_client(client: ClientCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO client (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)", (client.first_name, client.last_name, client.email, client.phone, client.address))
            connection.commit()
            print("Insertion réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        return False
    finally:
        connection.close()

def get_client(id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM client WHERE id = %s", (id,))
            result = cursor.fetchone()
            print(f"Récupération réussie ! {result}")
        return result
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        return None
    finally:
        connection.close()

def update_client(id: int, client: ClientCreate):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE client SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s WHERE id = %s", (client.first_name, client.last_name, client.email, client.phone, client.address, id))
            connection.commit()
            print("Mise à jour réussie !")
        return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        return False
    finally:
        connection.close()

def delete_client(id: int):
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
    finally:   
        connection.close()
        