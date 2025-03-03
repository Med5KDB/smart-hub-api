from database import get_db_connection
def test_db_connection():
    try:
        connection = get_db_connection()
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"Connexion réussie ! Version de MySQL : {version['VERSION()']}")
        
        connection.close()
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")

if __name__ == "__main__":
    test_db_connection()