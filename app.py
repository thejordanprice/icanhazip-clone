from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    return request.headers.get("CF-Connecting-IP") or \
           (request.headers.getlist("X-Forwarded-For") or [request.remote_addr])[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
