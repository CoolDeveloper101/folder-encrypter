import os
from cryptography.fernet import Fernet

def key():
    key = Fernet.generate_key()
    return(key)

def encrypt(key, message):
    encoded = message.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return(encrypted)

def decrypt(key ,encrypted_message):
    f2 = Fernet(key)
    decrypted = f2.decrypt(encrypted_message)

    original_message = decrypted.decode()
    return(original_message)


def getFiles(path):
    path = os.path.abspath(path)
    files = []
    for folder in os.walk(path):
        for file in folder[2]:
             files.append(os.path.join(folder[0],file))

    return tuple(files)

def _encrypt_folder(files):
    for file in files:
        if not file == os.path.join(path, 'key.pem'):
            with open(file, 'r') as f:
                contents = f.read()
            with open(file, 'wb') as f:
                f.write(encrypt(Key, contents))


def _decrypt_folder(files):
    for file in files:
        if not file == os.path.join(path, 'key.pem'):
            with open(file, 'rb') as f:
                contents = f.read()
            with open(file, 'w') as f:
                f.write(decrypt(Key, contents))


def encrypt_folder(path):
    path = os.path.abspath(path)
    if not os.path.exists(os.path.join(path, 'key.pem')):
        with open(os.path.join(path, 'key.pem'), 'wb') as k:
            Key = key()
            k.write(Key)
    else:
        with open(os.path.join(path, 'key.pem'), 'rb') as k:
            Key = k.read()
    files = getFiles(path)
    _encrypt_folder(files)

def decrypt_folder(path):
    path = os.path.abspath(path)
    if not os.path.exists(os.path.join(path, 'key.pem')):
        with open(os.path.join(path, 'key.pem'), 'wb') as k:
            Key = key()
            k.write(Key)
    else:
        with open(os.path.join(path, 'key.pem'), 'rb') as k:
            Key = k.read()
    files = getFiles(path)
    _decrypt_folder(files)
