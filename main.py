import hashlib
import os
import json
import random
import string
import time


class PasswordGenerator:
    def __init__(self, path):
        with open(path, "r") as file:
            config = json.load(file)
            self.password_length = config["password_length"]
            self.include_numbers = config["include_numbers"]
            self.include_symbols = config["include_symbols"]
            self.password = None

    def generate_password(self):
        password = ""
        characters = string.ascii_letters

        if self.include_numbers:
            characters += string.digits
        if self.include_symbols:
            characters += string.punctuation

        for i in range(self.password_length):
            password += random.choice(characters)

        self.password = password

    def __repr__(self):
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        return hashed_password

    def __str__(self):
        if self.password:
            return "Password generated"
        else:
            return "Password not generated"

    def set_password_as_env_variable(self):
        os.environ["PASSWORD"] = self.password

    def check_password_strength(self):
        start_time = time.time()
        hacked = False
        # ... some code to attempt to hack the password ...
        if hacked:
            return "Password is weak"
        if time.time() - start_time < 60:
            return "Password is weak"
        else:
            return "Password is strong"

    def replace_weak_password(self):
        strength = self.check_password_strength()
        while strength == "Password is weak":
            self.generate_password()
            strength = self.check_password_strength()
        self.set_password_as_env_variable()
