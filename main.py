import os

from flask_migrate import Migrate

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

app = create_app(os.getenv('APP_ENV', 'dev'))
app.register_blueprint(blueprint)

app.app_context().push()

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
