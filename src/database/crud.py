# create read update delete
from src.my_logger import logger
from psycopg2 import sql


def create(conn, cur, table_name: str, data: dict):
    columns = data.keys()
    values = [data[column] for column in columns]

    query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) RETURNING id").format(
        table=sql.Identifier(table_name),
        fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
        values=sql.SQL(', ').join(sql.Placeholder() * len(values))
    )
    try:
        cur.execute(query, values)
        conn.commit()
        logger.set_log_file(__name__)
        logger.info(f'Successfully commited: {data}')

    except Exception as e:
        logger.error(str(e))


def read(cur, query):
    try:
        cur.execute(query)
        if 'users' in query:
            return cur.fetchone()
        elif 'clothes' in query:
            return cur.fetchall()
        else:
            return None
    except Exception as e:
        logger.error(str(e))
