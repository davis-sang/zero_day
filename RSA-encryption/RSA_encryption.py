from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from binascii import hexlify


from RSA_decryption import decrypt


key = RSA.generate(1024)

private_key = key
public_key = key.publickey()

data_to_encrypt = b"May the force be with you."
cipher_rsa = PKCS1_OAEP.new(public_key)

encrypted = cipher_rsa.encrypt(data_to_encrypt)

print("Encrypted: ", hexlify(encrypted))

decrypted_message = decrypt(private_key, encrypted)

# Display the encrypted message
print("Decrypted: ", decrypted_message.decode("utf-8"))
