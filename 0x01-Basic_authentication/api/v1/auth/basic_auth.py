#!/usr/bin/env python3
"""Basicauth file
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basicauth class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """base authorization header
        """
        if not authorization_header:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
