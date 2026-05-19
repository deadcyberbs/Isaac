from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/img', methods=['POST'])
def process_frame():
    return jsonify({"status": "success", "message": "Isolated GUI Mode (No Hardware)"})


@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'hi.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)