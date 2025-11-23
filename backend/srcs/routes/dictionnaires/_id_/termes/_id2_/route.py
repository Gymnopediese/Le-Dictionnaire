from imports.forapi import *

@dictionnaires.route('/<string:id>/termes/<string:id2>')
class DictionnaireTermesApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.response(200, schema=DictionnaireFinalResponse)
    @decorator(object=Dictionnaire, object2=Terme, autorename=True)
    def put(self, dictionnaire, terme):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        new_terme = DictionnaireTerme.query.filter_by(dictionnaire_id=dictionnaire.id, terme_id= terme.id).first()
        print("boty ", dictionnaire.name, terme.name, new_terme)
        if new_terme:
            return jsonify({})
        new_terme = DictionnaireTerme(dictionnaire_id=dictionnaire.id, terme_id= terme.id)
        db.session.add(new_terme)
        db.session.commit()
        return jsonify({})
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.response(200, schema=DictionnaireFinalResponse)
    @decorator(object=Dictionnaire, object2=Terme, autorename=True)
    def delete(self, dictionnaire, terme):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        new_terme = DictionnaireTerme.query.filter_by(dictionnaire_id=dictionnaire.id, terme_id= terme.id).first()
        db.session.delete(new_terme)
        db.session.commit()
        return object.serialize({})
    
