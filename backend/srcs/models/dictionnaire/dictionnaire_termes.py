from imports.services import *

class DictionnaireTerme(Model):

    dictionnaire = db.relationship('Dictionnaire', backref=db.backref('termes', cascade='all, delete-orphan'))
    dictionnaire_id = db.Column(db.Integer, db.ForeignKey('dictionnaire.id'), nullable=False)
    
    terme = db.relationship('Terme', backref=db.backref('dictionnaires', cascade='all, delete-orphan'))
    terme_id = db.Column(db.Integer, db.ForeignKey('terme.id'), nullable=False)
    
        
    @staticmethod
    def put_terme_metadata(args, terme):
        if not "dictionnaires" in args:
            return
        dictionnaires_new = args["dictionnaires"]["data"]
        dictionnaires_old = terme.dictionnaires
        ids_new = {d['data'] for d in dictionnaires_new}
        ids_old = {d.dictionnaire.id for d in dictionnaires_old}

        dictionnaires_new = [i for i in dictionnaires_new if i["data"] not in ids_old]
        dictionnaires_old = [d for d in dictionnaires_old if d.dictionnaire.id not in ids_new]
        print(dictionnaires_new, dictionnaires_old)
        for dictionnaire in dictionnaires_new:
            d = DictionnaireTerme.get(dictionnaire_id=dictionnaire["data"], terme_id=terme.id)
            if d:
                print("bitch boy in tbe playcea")
                continue
            d = DictionnaireTerme(dictionnaire_id=dictionnaire["data"], terme_id=terme.id)
            db.session.add(d)
            db.session.commit()
        
        for d in dictionnaires_old:
            
            d = DictionnaireTerme.get(dictionnaire_id=d.dictionnaire.id, terme_id=terme.id)
            if not d:
                continue
            db.session.delete(d)
            db.session.commit()
        args.pop("dictionnaires")