from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    container_id = os.uname()[1]
    return f"hello world Roberto Luis Angulo Vásquez {container_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)