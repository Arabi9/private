from cryptography.hazmat.primitives.kdf.kyber import Kyber1024
from chacha20poly1305 import ChaCha20Poly1305
import numpy as np

class QuantumEncryption:
    def __init__(self):
        self.kyber = Kyber1024.generate_key()
        self.chacha = ChaCha20Poly1305(np.random.bytes(32))
    
    def hybrid_encrypt(self, data):
        ct, ss = self.kyber.encapsulate()
        encrypted = self.chacha.encrypt(ss, data)
        return ct + encrypted
    
    def quantum_sign(self, data):
        # Gitterbasierte Signatur
        return falcon.sign(data, self.kyber)
