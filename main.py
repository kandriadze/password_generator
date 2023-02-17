import hashlib
import itertools
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

    def password_as_env_variable(self):
        os.environ["PASSWORD"] = self.password

    def decrypt(self):
        charset = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=[]{}|;:,.<>/?"
        for self.password_length in range(1, self.password_length + 1):
            for password_candidate in itertools.product(charset, repeat=self.password_length):
                hashed_password = "".join(password_candidate)
                while hashlib.sha256(self.password.encode()).hexdigest() == hashed_password:
                    return "password decrypted"

                else:
                    return "none"

    def is_password_weak(self):
        # hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        start_time = time.monotonic()
        while True:
            result = self.decrypt()
            if result:
                passed_time = time.monotonic() - start_time
                if passed_time <= 60:
                    return "weak"
                else:
                    return "strong"
                # if self.password_length >= 20:
                #     return "strong"

    # def replace_weak_password(self):
    #     strength = self.is_password_weak()
    #     while strength == "Password is weak":
    #         self.generate_password()
    #         strength = self.is_password_weak()
    #     self.is_password_weak()


if __name__ == '__main__':
    a = PasswordGenerator("/home/kote/PycharmProjects/password_task/test.json")
    a.generate_password()
    print(a.__repr__())
    print(a.__str__())
    # repr(a)
    # str(a)
    print(a.decrypt())

