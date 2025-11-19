from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization


private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()


private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


message = b"Message to be signed"
signature = private_key.sign(message, hashes.SHA256())


try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
