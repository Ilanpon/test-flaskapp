from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    agent = 'Your User Agent is {}'.format(request.headers.get('User-Agent'))
    return render_template('index.html', agent=agent)


if __name__ == "__main__":
    app.run()