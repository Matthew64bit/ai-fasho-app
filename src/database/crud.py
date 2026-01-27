# create read update delete
from src.my_logger import logger

logger.set_log_file(__name__)

def create(conn, cur, data):
    query = """
            INSERT INTO clothes
                (id, brand, category, gender, style, fit, colours, season, price, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
            """
    try:
        cur.execute(query, (
            data['id'],
            data['brand'],
            data['category'],
            data['gender'],
            data['style'],
            data['fit'],
            data['colours'],
            data['season'],
            data['price'],
            data['url']
        ))
        conn.commit()

    except Exception as e:
        logger.error(str(e))

def read(cur, query: str):
    try:
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        logger.error(str(e))
