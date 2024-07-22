from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
