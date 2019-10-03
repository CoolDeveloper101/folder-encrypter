import os
from cryptography.fernet import Fernet

PATH = 'C:\\Users\\HP\\Desktop\\test_folder'

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

files = getFiles(PATH)
if not os.path.exists(os.path.join(PATH, 'key.pem')):
    with open(os.path.join(PATH, 'key.pem'), 'wb') as k:
        Key = key()
        k.write(Key)
else:
    with open(os.path.join(PATH, 'key.pem'), 'rb') as k:
        Key = k.read()

def _encrypt_folder(files):
    for file in files:
        if not file == os.path.join(PATH, 'key.pem'):
            with open(file, 'r') as f:
                contents = f.read()
            with open(file, 'wb') as f:
                f.write(encrypt(Key, contents))

# encrypt_folder(files)

def _decrypt_folder(files):
    for file in files:
        if not file == os.path.join(PATH, 'key.pem'):
            with open(file, 'rb') as f:
                contents = f.read()
            with open(file, 'w') as f:
                f.write(decrypt(Key, contents))

decrypt_folder(files)
##encrypt_folder(files)


def encrypt_folder(path):
    path = os.path.abspath(path)
    files = getFiles(path)
    _encrypt_folder(files)

def decrypt_folder(path):
    path = os.path.abspath(path)
    files = getFiles(path)
    _encrypt_folder(files)
