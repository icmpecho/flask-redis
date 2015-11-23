# Flask Redis
This is the source code of a simple Redis as a service deployed to http://redisaas.herokuapp.com

## Usage

    # Storing value
    POST https://redisaas.herokuapp.com/<your_key>

    # Retrieving value back
    GET https://redisaas.herokuapp.com/<your_key>

## Running locally
You need to change `REDIS_URL` in .env to point to your Redis installation

    $ pip install -r requirements.txt
    $ foreman start
