from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/<key>', methods=['GET', 'POST'])
def redis_key(key):
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'


if __name__ == '__main__':
    app.run(debug=True)
