#Keypair generation in Python

from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
pubkey = private_key.publickey()

private_key = private_key.exportKey().decode("utf-8")
pubkey = pubkey.exportKey().decode("utf-8")



#Signature generation
pip install ecdsa

from ecdsa import SigningKey
private_key = SigningKey.generate() 
signature = private_key.sign(b"Blockchain is Fun!")
