from imports.forapi import *


@dictionnaires.route('/')
class DictionnairesAPI(MethodView):

    @dictionnaires.doc(description="Get me")
    @dictionnaires.response(200)
    @decorator(user=True)
    def get(self, user):
        """
        Get the info of the current user.
        ---
        responses:
            200:
                description: User
        """
        dictionnaires = (Dictionnaire.query
            .filter(Dictionnaire.visibility == "public")
            .filter(~Dictionnaire.ownerships.any(
                db.and_(
                    Ownership.user_id == user["id"],
                    Ownership.rights.in_(["all", "write"])
                )))
            .limit(50).all())
        res = [dictionnaire.serialize(DictionnaireResponse) for dictionnaire in dictionnaires]
        print(dictionnaires, res)
        return jsonify(res)
    
    # @dictionnaires.doc(description="Update a user by ID")
    # @dictionnaires.arguments(UpdateUser)
    # @dictionnaires.response(200, schema=UserResponse)
    # @jwt_required()
    # def put(self, args, id):
    #     user = User.query.get(id)
    #     user.update(**args)
    #     db.session.commit()
    #     return jsonify(user.serialize())

    @dictionnaires.doc(description="Create a new dictionnaire")
    @dictionnaires.arguments(DictionnaireCreate)
    @dictionnaires.response(200)
    @decorator()
    def post(self, args):
        user = get_jwt_identity()
        
        dico = Dictionnaire(**args)
        db.session.add(dico)
        db.session.commit()
        
        
        dico = Ownership(
            rights=OwnerShipRights.all.value,
            user_id=user['id'],
            dictionnaire_id=dico.id,
        )
        db.session.add(dico)
        db.session.commit()
        return jsonify({})
    
    
    # @dictionnaires.doc(description="Delete a user by ID")
    # @dictionnaires.response(204)
    # @jwt_required()
    # def delete(self, id):
    #     user = User.query.get(id)
    #     db.session.delete(user)
    #     db.session.commit()
    #     return jsonify({})
    
