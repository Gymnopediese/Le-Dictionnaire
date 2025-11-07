from imports.all import *
from tests.fake_db import fake_db
from sqlalchemy.sql import text
os.environ['PYTHONUNBUFFERED'] = "1"

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
    