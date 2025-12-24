from imports.services import *

class Author(Model):
    terme = db.relationship('Terme', backref=db.backref('authors', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('termes', cascade='all, delete-orphan'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    rights = db.Column(db.String)
    
    
          
    @staticmethod
    def put_terme_metadata(args, terme):

        if not "authors" in args:
            return
        authors_new = args["authors"]["data"]
        authors_old = terme.authors
        ids_new = {d['data'] for d in authors_new}
        ids_old = {d.user.id for d in authors_old}
        authors_new = [i for i in authors_new if i["data"] not in ids_old]
        authors_old = [d for d in authors_old if d.user.id not in ids_new]
        print(authors_new, authors_old)
        for user in authors_new:
            d = Author.get(user_id=user["data"], terme_id=terme.id)
            if d:
                continue
            d = Author(user_id=user["data"], terme_id=terme.id, rights="write")
            db.session.add(d)
            db.session.commit()
        
        for d in authors_old:
            
            d = Author.get(user_id=d.user.id, terme_id=terme.id)
            if not d or d.rights == "all":
                continue
            db.session.delete(d)
            db.session.commit()
        args.pop("authors")