from flask import Flask, url_for

app = Flask(__name__)

@app.route('/me')
def api_me():
    return {
        "username": 'yqzhang',
        "theme": 'good',
        "image": url_for("user_image", filename='image'),
    }

@app.route('/userImage')
def user_image():
    return 'a image'

if __name__ == '__main__':
    app.run()
