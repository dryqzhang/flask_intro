from flask import Flask
from  markupsafe import escape

app = Flask(__name__)
@app.route('/user/<username>')
def hello_IC(username):
    return 'Hello, %s' % escape(username)

@app.route('/port/<int:port_id>')
def show_port(port_id):
    return 'Port %d' % port_id

if __name__ == '__main__':
    app.run(host='127.0.0.1' ,debug=True)
