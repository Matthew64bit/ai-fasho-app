import uuid

class User:
    def __init__(self, username: str, password: str):
        self.__id = str(uuid.uuid4())
        self.__username = username
        self.__password = password

    def get_id(self) -> str:
        return self.__id

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password
