from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    quote = None
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run()
