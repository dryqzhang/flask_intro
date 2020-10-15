from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def main(name=None):
    return render_template('hello.html', name=name)

@app.route('/IC')
def IC_index():
    return render_template('qlqdIC.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
