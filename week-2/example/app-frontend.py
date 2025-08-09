from flask import Flask, request, render_template_string
import requests, os

app = Flask(__name__)
OCR_SERVICE_URL = os.environ.get("OCR_SERVICE_URL", "http://localhost:5001")

@app.route('/')
def index():
    return render_template_string("""
        <h1>편지 번역 시스템 (Mock)</h1>
        <form action="/translate" method="post">
            <button type="submit">샘플 편지 번역 요청하기</button>
        </form>
        {% if result %}
            <h2>번역 결과:</h2>
            <p>{{ result }}</p>
        {% endif %}
    """)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # 1. OCR 워커에게 OCR 요청
        ocr_response = requests.post(f"{OCR_SERVICE_URL}/ocr")
        ocr_response.raise_for_status()
        result_text = ocr_response.json().get("translated_text", "오류 발생")
        return render_template_string("""
            <h1>편지 번역 시스템 (Mock)</h1>
            <form action="/translate" method="post">
                <button type="submit">샘플 편지 번역 요청하기</button>
            </form>
            <h2>번역 결과:</h2>
            <p style="color:blue;">{{ result }}</p>
        """, result=result_text)
    except requests.exceptions.RequestException as e:
        return f"서비스 연결 오류: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
