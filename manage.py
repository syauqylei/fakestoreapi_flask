import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv

from .src.app import create_app, db

if os.getenv('FLASK_ENV') != "production":
    load_dotenv()

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

db.init_db(app)
migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
