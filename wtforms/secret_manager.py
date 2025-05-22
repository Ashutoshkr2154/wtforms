import os
import secrets

class Secret_Manager:
    def __init__(self):
        self.secret_key = os.getenv('SECRET_KEY')
        if not self.secret_key:
            self.secret_key = self.generate_secret_key()
            self.save_secret_key(self.secret_key)

    def generate_secret_key(self):
        return secrets.token_hex(16)

    def save_secret_key(self, secret_key):
        os.environ['SECRET_KEY'] = secret_key

    def get_secret_key(self):
        return self.secret_key