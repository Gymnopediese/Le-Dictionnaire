from imports.all import *
import blueprints
from generator import main as generate_import_files
from flask_migrate import Migrate


os.environ['PYTHONUNBUFFERED'] = "1"
import atexit

migrate = Migrate(app, db)


def on_exit():
    generate_import_files()
atexit.register(on_exit)


if __name__ == '__main__':
    # if os.getenv("TEST") == "True":
    with app.app_context():
        # db.drop_all()
        # db.session.execute(text("DROP SCHEMA public CASCADE;"))
        # db.session.execute(text("CREATE SCHEMA public;"))
        # db.session.commit()
        db.create_all()
        # db.session.add(User(username="poupi", password=User.hash("123")))
        db.session.commit()
        # fake_db()
        pass

    app.run(debug=True, host="0.0.0.0", ssl_context='adhoc')
