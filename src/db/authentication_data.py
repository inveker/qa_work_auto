from src.db.db_driver import DB


class AuthenticationData:
    @staticmethod
    def get():
        db = DB.read()
        return (db['login'], db['password'])
