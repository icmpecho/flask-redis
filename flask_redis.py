import os
from flask import Flask
from flask import request
import redis

app = Flask(__name__)
r = redis.from_url(os.environ.get("REDIS_URL"))


@app.route('/<key>', methods=['GET', 'POST'])
def redis_key(key):
    if request.method == 'POST':
        r.set(key, request.data)
        return request.data
    else:
        data = r.get(key)
        return data


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
