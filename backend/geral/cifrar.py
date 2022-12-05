from hashlib import blake2b

def encrypt(password):
    encrypter = blake2b()
    em_bytes = bytes(password, encoding = "utf-8")
    encrypter.update(em_bytes)
    return encrypter.hexdigest()

def check_password(encrypted_password, password):
    pas = encrypt(password)
    if encrypted_password == pas:
        return True
    return False
