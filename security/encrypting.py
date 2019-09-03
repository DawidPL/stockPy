from cryptography.fernet import Fernet
import os


def get_token():
    with open(r'C:\Users\Dawid\Documents\stockPy\stockPy\security\api_token.txt', 'rb') as file_object:
        for line in file_object:
            token = line
    return token.decode("utf-8")


# def encrypting():
#     key = Fernet.generate_key()
#     cipher_suite = Fernet(key)
#     ciphered_text = cipher_suite.encrypt(b"Password")
#     print(ciphered_text)
#     unciphered_text = cipher_suite.decrypt(ciphered_text)
#     print(unciphered_text)
#
#     with open('passkey.bin', 'wb') as file_object:
#         file_object.write(ciphered_text)


def decrypting():
    pass
