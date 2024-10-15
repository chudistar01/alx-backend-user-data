#!/usr/bin/env python3
"""Returns a hashed password
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Returns byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
