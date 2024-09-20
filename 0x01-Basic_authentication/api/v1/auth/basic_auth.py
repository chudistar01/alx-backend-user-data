#!/usr/bin/env python3
"""Basicauth file
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """base authorization header
        """
        if not base64_authorization_header:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_strings = decoded_bytes.decode('utf-8')
            return decoded_strings
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """user credentials header
        """
        if not decoded_base64_authorization_header:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        try:
            value = decoded_base64_authorization_header.split(':', 1)
            first_value = value[0].strip()
            second_value = value[1].strip()
            return first_value, second_value
        except Exception:
            return None, None
