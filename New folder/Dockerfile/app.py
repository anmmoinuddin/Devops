from flask import Flask

app = Flask(__name__)

# Read version from environment variable or default to 1
import os
version = os.getenv('APP_VERSION', '1')

@app.route('/')
def home():
    return f"Version {version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)