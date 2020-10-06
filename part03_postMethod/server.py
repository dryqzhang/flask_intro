from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='the long river'))
    return 'welcome'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
