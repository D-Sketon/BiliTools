import base64


def encrypt(string):
    a = base64.b64encode(string.encode())
    return base64.b64encode(a).decode()


def decrypt(string):
    b = base64.b64decode(string.encode())
    return base64.b64decode(b).decode()
