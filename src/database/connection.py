import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

from src.my_logger import logger

load_dotenv()
logger.set_log_file(__name__)

# TODO
def connect():
    db_config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
        "port": os.getenv("DB_PORT")
    }

    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="mateimate",
            database="fasho_app",
            port="5432"
        )
        cur = conn.cursor()
        logger.info("Connected to PostgreSQL database")
        return conn, cur

    except OperationalError as e:
        logger.error(str(e))
        return None, None

# TODO
def disconnect(conn, cur):
    cur.close()
    conn.close()
    logger.info(f"Disconnected from PostgreSQL database")