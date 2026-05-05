from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to our website'

@app.route('/web/status', methods=['GET'])
def status():
    url = request.args.get('url')

    session = requests.Session()
    r = session.get(url)

    status_code = r.status_code
    response_time = r.elapsed.total_seconds()

    if status_code == 200:
        state = 'Up'
    else:
        state = 'Down'

    result = {
        'URL': url,
        'status': state,
        'response_time': response_time,
        'status_code': status_code
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
