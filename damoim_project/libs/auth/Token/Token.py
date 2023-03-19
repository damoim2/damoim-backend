from django.utils import timezone
import datetime
import os
import base64
import hashlib
import hmac
import json
import time
class Token:
    # define secret keys to sign the tokens
    ACCESS_TOKEN_SECRET_KEY = os.environ.get('SECRET_KEY')
    REFRESH_TOKEN_SECRET_KEY = os.environ.get('SECRET_KEY')

    # define token expiry times in seconds
    ACCESS_TOKEN_EXPIRY_TIME = 3600  # 1 hour
    REFRESH_TOKEN_EXPIRY_TIME = 86400  # 1 day

    # create a new access token and refresh token for the specified user ID
    def create_token_pair(self, user_id):
        access_token = self.create_access_token(user_id)
        refresh_token = self.create_refresh_token(user_id)
        return access_token, refresh_token

    # create a new access token with expiry time of 1 hour from now
    def create_access_token(self, user_id):
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {
            "user_id": user_id,
            "exp": int(time.time()) + self.ACCESS_TOKEN_EXPIRY_TIME
        }
        header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        signature = hmac.new(self.ACCESS_TOKEN_SECRET_KEY.encode(), f"{header_b64}.{payload_b64}".encode(), hashlib.sha256).digest()
        signature_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")
        token = f"{header_b64}.{payload_b64}.{signature_b64}"
        return token

    # create a new refresh token with expiry time of 1 day from now
    def create_refresh_token(self, user_id):
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {
            "user_id": user_id,
            "exp": int(time.time()) + self.REFRESH_TOKEN_EXPIRY_TIME
        }
        header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        signature = hmac.new(self.REFRESH_TOKEN_SECRET_KEY.encode(), f"{header_b64}.{payload_b64}".encode(), hashlib.sha256).digest()
        signature_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")
        token = f"{header_b64}.{payload_b64}.{signature_b64}"
        return token

    # decode and verify an access token
    def decode_and_verify_access_token(self, token):
        try:
            header_b64, payload_b64, signature_b64 = token.split(".")
            header = json.loads(base64.urlsafe_b64decode(header_b64 + "==").decode())
            payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "==").decode())
            signature = base64.urlsafe_b64decode(signature_b64 + "==")
            if header["alg"] != "HS256":
                # invalid algorithm
                return None
            if int(time.time()) > payload["exp"]:
                # expired token
                return None
            expected_signature = hmac.new(self.ACCESS_TOKEN_SECRET_KEY.encode(), f"{header_b64}.{payload_b64}".encode(), hashlib.sha256).digest()
            if not hmac.compare_digest(expected_signature, signature):
                # invalid signature
                return None
            return payload
        except (ValueError, json.JSONDecodeError, TypeError, AttributeError):
            # invalid token
            return None

    # decode and verify a refresh token
    def decode_and_verify_refresh_token(self, token):
        try:
            header_b64, payload_b64, signature_b64 = token.split(".")
            header = json.loads(base64.urlsafe_b64decode(header_b64 + "==").decode())
            payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "==").decode())
            signature = base64.urlsafe_b64decode(signature_b64 + "==")
            if header["alg"] != "HS256":
                # invalid algorithm
                return None
            if int(time.time()) > payload["exp"]:
                # expired token
                return None
            expected_signature = hmac.new(self.REFRESH_TOKEN_SECRET_KEY.encode(), f"{header_b64}.{payload_b64}".encode(), hashlib.sha256).digest()
            if not hmac.compare_digest(expected_signature, signature):
                # invalid signature
                return None
            return payload
        except (ValueError, json.JSONDecodeError, TypeError, AttributeError):
            # invalid token
            return None

    # refresh an access token with a valid refresh token
    def refresh_access_token(self, refresh_token):
        refresh_payload = self.decode_and_verify_refresh_token(refresh_token)
        if not refresh_payload:
            # invalid or expired refresh token
            return None
        user_id = refresh_payload["user_id"]
        access_token = self.create_access_token(user_id)
        return access_token
