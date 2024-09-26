#!/usr/bin/env python3
"""Simple Flask APP
"""
import logging

from flask import Flask, abort, jsonify, redirect, request

from auth import Auth

logging.disable(logging.WARNING)

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Rturns: JSON Messsages
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """POST /users                                                                                                                                  
    Rturns: JSON Messsages                                                                                                                          
    """
    email = request.form.get("email")
    password = request.form("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5010")
