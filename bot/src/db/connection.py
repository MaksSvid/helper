from psycopg import connect, OperationalError
from bot.src.settings import settings


def create_connection(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT
):
    try:
        print("try connection ...")
        connection = connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("The connection to the PostgreSQL DB successful!")
    except OperationalError as err:
        print(f"The error '{err}' occurred")
        connection = None
    return connection


conn = create_connection()