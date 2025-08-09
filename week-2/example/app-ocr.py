from flask import Flask, jsonify
import time, requests, os

app = Flask(__name__)
TRANSLATE_SERVICE_URL = os.environ.get("TRANSLATE_SERVICE_URL", "http://localhost:5002")

@app.route('/ocr', methods=['POST'])
def ocr():
    time.sleep(5) # OCR 작업 시뮬레이션
    original_text = "Hello from your child"

    # 2. Translate 워커에게 번역 요청
    translate_response = requests.post(f"{TRANSLATE_SERVICE_URL}/translate", json={'text': original_text})
    return jsonify(translate_response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

