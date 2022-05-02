from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def cbc_encrypt(key, plaintext):
    iv = Random.get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(plaintext, AES.block_size))


def cbc_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return unpad(plaintext, AES.block_size)


def ctr_encrypt(key, plaintext):
    pass


def ctr_decrypt(key, ciphertext):
    pass
