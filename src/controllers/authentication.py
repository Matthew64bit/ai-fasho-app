import uuid
from argon2 import PasswordHasher
from ..models.user import User
from ..database.crud import read, create
from ..utils.text_formatter import format_user_search

ph = PasswordHasher()

def create_account(conn, cur, username, password):
    hash_pass = ph.hash(password).split('p=')[1]
    data = {
        'id': uuid.uuid4(),
        'username': username,
        'password': hash_pass
    }
    create(conn, cur, 'users', data)
    return User(username, hash_pass)

def login(cur, username, password):
    hash_pass = ph.hash(password).split('p=')[1]
    return read(cur, format_user_search(username, hash_pass))

