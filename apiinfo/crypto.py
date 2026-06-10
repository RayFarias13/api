from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# chave de 32 bytes (AES-256)
# EM PRODUÇÃO: guarde em variável de ambiente!
KEY = os.environ.get("KEY_AES").encode()

def encrypt_value(value: str) -> str:
    aesgcm = AESGCM(KEY)
    nonce = os.urandom(12)  # obrigatório no GCM
    ciphertext = aesgcm.encrypt(nonce, value.encode(), None)

    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_value(token: str) -> str:
    raw = base64.b64decode(token)
    nonce = raw[:12]
    ciphertext = raw[12:]

    aesgcm = AESGCM(KEY)
    return aesgcm.decrypt(nonce, ciphertext, None).decode()