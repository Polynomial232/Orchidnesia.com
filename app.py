from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'INI HALAMAN LOGIN'

if __name__ == '__main__':
    app.run()