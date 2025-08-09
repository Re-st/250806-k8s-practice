from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json.get('text', '')
    time.sleep(3) # 번역 작업 시뮬레이션
    translated = f"'{text}' >> 자녀로부터 온 편지입니다. 안녕하세요."
    return jsonify({'translated_text': translated})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

