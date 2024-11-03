from config import Settings
import mysql.connector


def create_connection(db_host, db_user, db_password, db_name):
    # Create a connection to the database
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = db.cursor()
    return db, cursor

def get_result(settings: Settings, query: str):
    db, cursor = create_connection(settings.db_host, settings.db_user, settings.db_password, settings.db_name)
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result