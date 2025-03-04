from app.database import get_db_connection
from app.schemas import ClientCreate, Client


def create(client: ClientCreate) -> dict[Client]:
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO client (first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)", (client.first_name, client.last_name, client.email, client.phone, client.address))
                conn.commit()
                cursor.execute("SELECT * FROM client WHERE id = LAST_INSERT_ID()")
                created_client = cursor.fetchone()
                return created_client
    except Exception as e:
        print(f"Erreur lors de l'insertion : {e}")
        raise e

def findOne(id: int) -> dict[Client]:
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM client WHERE id = %s", (id,))
                client = cursor.fetchone()
            return client
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")
        raise e

def findAll() -> list[dict[Client]]:
    try: 
        with get_db_connection as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM client")
                clients = cursor.fetchall()
            return clients
    except Exception as e:
        raise e

def updateOne(id: int, client: ClientCreate) -> dict[Client]:
    
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE client SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s WHERE id = %s", (client.first_name, client.last_name, client.email, client.phone, client.address, id))
                conn.commit()
                cursor.execute("SELECT * FROM client WHERE id = %s", (id,))
                updated_client = cursor.fetchone()
                return updated_client
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")
        return False

def deleteOne(id: int) -> int:
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM client WHERE id = %s", (id,))
                conn.commit()
                return id
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        raise e
        