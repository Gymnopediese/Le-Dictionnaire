from imports.services import *

class Relationship(Model):
    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('followings', cascade='all, delete-orphan'))
    target = db.relationship('User', foreign_keys=[target_id], backref=db.backref('followers', cascade='all, delete-orphan'))
    
    type = db.Column(db.String)

    @staticmethod
    def get_type(user_id, target_id):
        res = Relationship.get(user_id=user_id, target_id=target_id)
        return res.type if res else "stranger"
  
    @staticmethod      
    def get_friends(user_id):
        r1 = aliased(Relationship)
        r2 = aliased(Relationship)
        return (
            db.session.query(r1)
            .join(
                r2,
                and_(
                    r2.user_id == r1.target_id,
                    r2.target_id == r1.user_id,
                    r2.type == "follow",
                ),
            )
            .filter(
                r1.user_id == user_id,
                r1.type == "follow",
            )
        )
        
    @staticmethod      
    def get_followers(user_id):
        r1 = aliased(Relationship)
        r2 = aliased(Relationship)
        return (
            db.session.query(r1)
            .outerjoin(
                r2,
                and_(
                    r2.user_id == r1.target_id,
                    r2.target_id == r1.user_id,
                    r2.type == "follow",
                ),
            )
            .filter(
                r1.target_id == user_id,
                r1.type == "follow",
                r2.id.is_(None), 
            )
        )
        
    @staticmethod      
    def get_followings(user_id):
        r1 = aliased(Relationship)
        r2 = aliased(Relationship)
        return (
            db.session.query(r1)
            .outerjoin(
                r2,
                and_(
                    r2.user_id == r1.target_id,
                    r2.target_id == r1.user_id,
                    r2.type == "follow",
                ),
            )
            .filter(
                r1.user_id == user_id,
                r1.type == "follow",
                r2.id.is_(None), 
            )
        )