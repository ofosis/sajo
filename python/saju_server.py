from flask import Flask, request, jsonify
import json
import test
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/send-json', methods=['POST'])
def process_post_request():
    try:
        data = request.get_json()
        print("완료")
        # 여기에서 데이터를 처리하고 응답을 생성합니다.
        json_result = test.test1(data)
        print("완료")
        # JSON 파일로 저장
        json_data = json.dumps(json_result, ensure_ascii=False)
        #json_variable = json_data
        print("완료")
        return jsonify(json_data)
    except Exception as e:
        print("에러 발생:", repr(e))
        return str(e), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)