from dotenv import load_dotenv
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

load_dotenv()
salt = bytes(os.getenv("SALT"), "utf-8")
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=5000000)


class Encryption:
    def generate_key(self, password):
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def encrypt_password(self, password, key):
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(password.encode())
        return encrypted_message

    def decrypt_password(self, password, key):
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(password).decode()
        return decrypted_message
