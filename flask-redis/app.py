import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "Welcome to Said's CoderCo webpage!, This webpage has been viewed "+counter+" time(s)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)