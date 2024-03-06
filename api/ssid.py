import secrets
import string


def generateRandomSsid(length=50):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
