from imports.forapi import *

from imports.models import *
@termes.route('/<string:id>/dictionnaires')
class TermeDictionnaireAPI(MethodView):
    @termes.doc(description="Update a temre by ID or Secret")
    @termes.arguments(TermeDictionnaireCreate)
    @termes.response(200, schema=UserResponse)
    @decorator(object=Terme, user=True)
    def put(self, args, object, user):
        terme = object
        for id in args["dictionnaires"]:
            dictionnaire = Dictionnaire.query.get(id)
            if not dictionnaire:
                raise Exception(404, "ressource does not exist")
            dictionnaire.put_allowed(user["id"])
            link = DictionnaireTerme.query.filter_by(dictionnaire_id=dictionnaire.id, terme_id=terme.id).first()
            if link:
                continue
            link = DictionnaireTerme(dictionnaire_id=dictionnaire.id, terme_id=terme.id)
            db.session.add(link)
        db.session.commit()
        return jsonify({})
    
    @termes.doc(description="Delete a user by ID")
    @termes.response(204)
    @termes.arguments(TermeDictionnaireCreate)
    @decorator(object=Terme, user=True)
    def delete(self, args, object, user):
        for id in args["dictionnaires"]:
            dictionnaire = Dictionnaire.query.get(id)
            if not dictionnaire:
                raise Exception(404, "ressource does not exist")
            dictionnaire.delete_allowed(user["id"])
            link = DictionnaireTerme.query.filter_by(dictionnaire_id=dictionnaire.id, terme_id=object.id).first()
            if not link:
                continue
            db.session.delete(link)
        db.session.commit()
        return jsonify({})
    
    