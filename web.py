from flask import Flask, request, render_template, url_for
# import json
app = Flask(__name__)

from des import getDESResult
from rsa import generateKeys, encryptRSA, decryptRSA

def intToStr(n):
    return bin(n)[2:]

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/des', methods=['POST'])
def process_DES():
    # data = json.loads(request.get_data(as_text=True))
    data = request.get_json(silent=True)
    des_key = int(data['ciphertext'], 2)
    n = int(data['n'], 2)
    pub = int(data['pub'], 2)
    key = int(data['key'], 2)
    rsa_encryption = encryptRSA(des_key, n, pub)
    rsa_decryption = decryptRSA(rsa_encryption, n, key)
    enc_str = intToStr(rsa_encryption)
    dec_str = intToStr(rsa_decryption)
    s = ''
    for i in range(64 - len(dec_str)):
        s += '0'
    dec_str = s + dec_str
    if dec_str != data['ciphertext']:
        print(type(dec_str), dec_str)
        print(type(data['ciphertext']), data['ciphertext'])
    status, result = getDESResult(data['text'], dec_str, data['mode'], data['iv'])
    return {
        "status": status,
        "result": result,
        "rsa_enc": enc_str,
        "rsa_dec": dec_str
    }

@app.route('/rsa', methods=['GET'])
def get_RSA_key():
    (n, pub_key, pri_key) = generateKeys()
    return {
        "n": intToStr(n),
        "pub": intToStr(pub_key),
        "key": intToStr(pri_key)
    }
