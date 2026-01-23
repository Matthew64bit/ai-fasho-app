#create read update delete
from src.my_logger import logger
import uuid

logger.set_log_file(__name__)

dummy_data = {
    "id": uuid.uuid4(),
    "brand": "TEST_BRAND",
    "category": "TEST_CATEGORY",
    "gender": "M",
    "style": ["TEST_AESTHETIC", "TEST_OCCASION"],
    "fit": "TEST_FIT",
    "colours": ["TEST_COLOUR1", "TEST_COLOUR2"],
    "season": "F/W",
    "price": 249.99,
    "url": "https://dummyurl.com"
}

def create(conn, cur, data):
    query = """
            INSERT INTO clothes
            (id, brand, category, gender, style, fit, colours, season, price, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cur.execute(query, (
            dummy_data["id"],
            dummy_data["brand"],
            dummy_data["category"],
            dummy_data["gender"],
            dummy_data["style"],
            dummy_data["fit"],
            dummy_data["colours"],
            dummy_data["season"],
            dummy_data["price"],
            dummy_data["url"]
        ))
        conn.commit()
        logger.info("Inserted SUCCESSFULLY dummy_data")

    except Exception as e:
        logger.error(str(e))
