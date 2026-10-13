import socket
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host="db-service", port=6379)

@app.route("/")
def index():
    hits = r.incr("hits")
    return f"Bonjour ! Cette page a été vue {hits} fois. Je suis le conteneur {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)