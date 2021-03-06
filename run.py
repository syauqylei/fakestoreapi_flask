import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app
from src.models import db

if os.getenv('FLASK_ENV') is None:
    load_dotenv(find_dotenv())

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == "__main__":
    port = os.getenv('PORT')
    app.run(host='0.0.0.0', port=port)
