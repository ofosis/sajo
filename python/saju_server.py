from flask import Flask, request, jsonify
import json
import test
from flask_cors import CORS
import LuckCrawler as LC

app = Flask(__name__)
CORS(app)

@app.route('/send-json', methods=['POST'])
def process_post_request():
    try:
        data = request.get_json()
        json_result = LC.TranceLuckData(data)
        json_data = json.dumps(json_result, ensure_ascii=False)
        json_variable = json_data
        return jsonify(json_variable)
    except Exception as e:
        print("에러 발생:", repr(e))
        return str(e), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)