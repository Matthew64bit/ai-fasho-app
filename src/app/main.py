from src.database import crud
from src.database.connection import *
from src.utils import text_formatter

def main():
    dummy_filters = {
        'colours': ['brown']
    }

    conn, cur = connect()
    query = text_formatter.format_query(dummy_filters)
    data = crud.read(cur, query)
    print(data)
    disconnect(conn, cur)

if __name__ == '__main__':
    main()