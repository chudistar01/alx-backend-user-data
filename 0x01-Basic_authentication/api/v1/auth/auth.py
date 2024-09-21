#!/usr/bin/env python3
"""Authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """auth function
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path.rstrip('/')

        for excluded in excluded_paths:
            normalized_excluded = excluded.rstrip('/')
            if normalized_path == normalized_excluded:
                return True

        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Users request
        """

        return None
