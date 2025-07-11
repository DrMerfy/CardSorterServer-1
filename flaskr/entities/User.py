# --------------------
# Template DO NOT EDIT
# --------------------

from bson import ObjectId
from flask import current_app


class User:
    def __init__(self):
        self.user_id = "686fb69af77d5260cae5ca56"
        self.username = "developer"
        self.password_hash = 0
        self.auth_token = "dev"

    def create_user(self, username, password, email):
        pass

    def verify_user(self, username, password):
        pass

    def get_username(self, user_id):
        return self.username

    @staticmethod
    def validate_request(auth_token):
        return "686fb69af77d5260cae5ca56"

    def _hash_password(self, password):
        pass

    @staticmethod
    def _verify_password(self, password):
        return True

    @staticmethod
    def _encode_auth_token(user_id):
        return "686fb69af77d5260cae5ca56"

    @staticmethod
    def _decode_auth_token(auth_token):
        return "developer"