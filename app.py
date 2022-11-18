from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/name=<username>%message=<msg>')
def show_user_profile(username,msg):
    return f"Hello {username}! {msg}!"


if __name__ == '__main__':
    app.run()
