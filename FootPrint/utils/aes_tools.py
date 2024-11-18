# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib


def baby_hash_string(input_string):
    # 创建一个 md5 哈希对象
    md5_hash = hashlib.md5()

    # 更新哈希对象，注意需要将字符串编码为字节
    md5_hash.update(input_string.encode('utf-8'))

    # 获取十六进制的哈希值
    return md5_hash.hexdigest()

BABY_AES_KEY = b'f\xb2Q\x8d\xc5\xf08\x91\xe0Jq\xac\xf2\x86\xfb\x94'

def baby_encrypt_aes(key, data):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the data to be a multiple of the block size (16 bytes for AES)
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    # Combine IV and encrypted data and convert to Base64
    encrypted_data_base64 = base64.b64encode(iv + encrypted_data).decode('utf-8')
    return encrypted_data_base64

def baby_decrypt_aes(key, encrypted_data_base64):
    # Decode the Base64 encoded data
    encrypted_data_bytes = base64.b64decode(encrypted_data_base64)
    # Extract the IV and the encrypted data
    iv = encrypted_data_bytes[:16]
    encrypted_data = encrypted_data_bytes[16:]
    # Create a new AES cipher object for decryption
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the data
    decrypted_data = cipher_dec.decrypt(encrypted_data)
    # Unpad the decrypted data
    unpadded_data = unpad(decrypted_data, AES.block_size).decode('utf-8')
    return unpadded_data



if __name__ == "__main__":
    # Example usage
    # key = get_random_bytes(16)  # 16 bytes for AES-128
    # key = get_random_bytes(16)  # 16 bytes for AES-128
    key = BABY_AES_KEY

    print(key)
    data = "Secret message"

    # Encrypt the data
    encrypted_data_base64 = baby_encrypt_aes(key, data)
    print(f"Encrypted data (Base64): {encrypted_data_base64}")

    # Decrypt the data
    decrypted_data = baby_decrypt_aes(key, encrypted_data_base64)
    print(f"Decrypted data: {decrypted_data}")