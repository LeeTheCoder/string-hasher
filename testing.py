import hashlib
import os

# Introduction
os.system('clear')
print("String Hasher v1.0")

# Predefined functions to hash the data
def sha1Hash():
    hash_object = hashlib.sha1(text_to_hash.encode())
    hex_dig = hash_object.hexdigest()
    print('Your hash is ' + hex_dig)

def md5Hash():
    hash_object = hashlib.md5(text_to_hash.encode())
    hex_dig = hash_object.hexdigest()
    print('Your hash is ' + hex_dig)

# Data (text) to hash
text_to_hash = input("Insert a string to hash: ")

os.system('clear')
print('Possible methods of hashing: MD5, SHA-1')
while True:
    method_of_hashing = input('Use algorithm: ')
    if method_of_hashing.lower() == 'md5':
        md5Hash()
        break
    if method_of_hashing.lower() == 'sha-1':
        sha1Hash()
        break
    print('Invalid choice. Choices are "MD5", "SHA-1". Try again.')
