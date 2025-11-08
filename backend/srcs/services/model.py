from services.db import db
import inspect

class Model(db.Model):
    __abstract__ = True  # n'est pas une table

    id = db.Column(db.Integer, primary_key=True)
    ctime = db.Column(db.DateTime, server_default=db.func.now())
    utime = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @staticmethod
    def exists(**kwargs):
        return bool(Model.query.filter_by(**kwargs).first())

    def serialize(self, depth=100):
        res = {}
        for i in inspect.getmembers(self):
            if i[0].startswith('_'):
                continue
            if inspect.ismethod(i[1]): 
               continue
            if inspect.isclass(i[1]) and depth > 0:
                res[i[0]] = i[1].serialize(depth - 1)
            elif inspect.isclass(i[1]):
                res[i[0]] = i[1].id
            else:
                res[i[0]] = i[1]
        return res
