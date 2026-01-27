from src.database.data_handler import organize
from src.database.connection import *

def main():
    conn, cur = connect()
    organize(conn, cur)
    disconnect(conn, cur)

if __name__ == "__main__":
    main()