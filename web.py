from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Your User Agent is {}'.format(request.headers.get('User-Agent'))


if __name__ == "__main__":
    app.run()