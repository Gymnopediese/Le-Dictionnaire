from imports.forapi import *

@users.route('/<string:id>/relationship')
class DictionnaireOwnershipApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.arguments(RelationshipCreate)
    @dictionnaires.response(200)
    @decorator(check_allowed=False, user=True)
    def put(self, args, user, id):
        
        type = args.get("type")

        relationship = Relationship.query.filter_by(user_id=user["id"], target_id=id).first()
        otherway_relationship = Relationship.get_type(target_id=user["id"], user_id=id)
        
        # the boy blocked you sorry
        if otherway_relationship == "blocked":
            raise Exception(405, "no allowed")
        
        #
        if type == "unfollow":
            if not relationship:
                raise Exception(405, "whaaat ?")
            db.session.delete(relationship)
            db.session.commit()
            return jsonify({})
            
        if not relationship:
            relationship = Relationship(
                user_id=user["id"],
                target_id=id,
                type=type
            )
            db.session.add(relationship)
        else:
            relationship.type = type
        db.session.commit()
        return jsonify({})