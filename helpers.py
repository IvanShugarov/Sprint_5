import random
import string

def generate_random_email():
    user_name = "".join(random.choices(string.ascii_lowercase,k=7))
    domain = "".join(random.choices(string.ascii_lowercase,k=3))
    email = f"{user_name}@{user_name}.{domain}"
    return email

def generate_random_string(length=4):
    return "".join(random.choices(string.ascii_lowercase, k=length))