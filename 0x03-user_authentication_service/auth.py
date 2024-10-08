#!/usr/bin/env python3
"""Module authentication
"""

import logging
from db import DB
from user import User
from uuid import uuid4
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


def _generate_uuid() -> bytes:
    """Generates uuid
    Returns:
         str: string representation
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """validates password and user
        Args:
          email
          password

        Returns:
          bool
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                password_bytes = password.encode('utf-8')
                hashed_password = user.hashed_password
                if bcrypt.checkpw(password_bytes, hashed_password):
                    return True
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """create a session and return session id as string
        Args:
           email (str): user's email

        Returns:
           str: session id
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieve user object
        Args:
           session_id(str): session id
        Returns:
           Union[User, None]: user object
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user
