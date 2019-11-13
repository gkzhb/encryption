from flask import Flask, request, render_template, url_for
# import json
app = Flask(__name__)

from des import getDESResult

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/des', methods=['POST'])
def process_DES():
    # data = json.loads(request.get_data(as_text=True))
    data = request.get_json(silent=True)
    status, result = getDESResult(data['text'], data['ciphertext'], data['mode'], data['iv'])
    return {
        "status": status,
        "result": result
    }
