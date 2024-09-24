import logging
from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
logging.disable(logging.WARNING)


def _hash_password(password: str) -> bytes:
    """Hashes password
    Args:
       password(str)
    Returns:
       bytes
    """
    e_pwd = password.encode()
    return bcrypt.hashpw(e_pwd, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new use
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
