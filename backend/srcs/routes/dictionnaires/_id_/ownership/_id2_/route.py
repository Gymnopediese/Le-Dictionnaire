from imports.forapi import *

@dictionnaires.route('/<string:id>/ownerships/<string:id2>')
class DictionnaireOwnershipApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.arguments(OwnershipPut)
    @dictionnaires.response(200)
    @decorator(object=Dictionnaire, object2=User, autorename=True, check_allowed=False, user=True)
    def put(self, dictionnaire, args, user, user_object):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        my_rights = Ownership.get_rights(user_id=user["id"], dictionnaire_id=dictionnaire.id, number=True)
        target_rights = Ownership.get_rights(user_id=user_object.id, dictionnaire_id=dictionnaire.id, number=True)
        new_rights = rights_level.get(args.get("rights"))
        
        # I have less rifght than hum
        if my_rights < target_rights:
            raise Exception(405, "not allowed")
        
        # I have not enought right to do this
        if my_rights < new_rights and new_rights > rights_level["read"]:
            raise Exception(405, "not allowed")
        
        # useless request
        if target_rights == new_rights:
            return jsonify({})
    
        # if im changing myslef or someone with my rights
        if my_rights == target_rights:
            # i want to change rights of someone with the same as me
            if user["id"] != user_object.id:
                if my_rights != rights_level["all"]:
                    raise Exception(405, "not allowed")
                # me all -> all, give ownership to someone
                # give owneship (same rights, not the same user, I am the owner)
                Ownership.set_rights(user_object.id, dictionnaire.id, args.get("rights"))
                Ownership.set_rights(user["id"], dictionnaire.id, "write")
                return jsonify({})
            
            # cannot remove ownership
            # Same rights, I am the owne
            if my_rights == rights_level["all"]:
                raise Exception(405, "cannot abandon dictionnary, user DELETE /Dicitonnaires/<id> to delete it")
            
            # cannot block yourself
            # same rights, I want to block
            if my_rights == rights_level["blocked"]:
                raise Exception(405, "cannot block yourself from dictionnaire")
            # write -> read, view - quit writing
            # read -> view - unfollow
            # view -> read - follow
            Ownership.set_rights(user_object.id, dictionnaire.id, args.get("rights"))
            return jsonify({})       
        
        if my_rights < new_rights and my_rights < rights_level["write"]:
            raise Exception(405, "not allowed")
        
        # me all, write -> (none, view -> read), not allowed
        # cannot force someonew to follow a dict
        if new_rights == rights_level["read"] and target_rights < rights_level["write"]:
            raise Exception(405, "cannot force someone to follow dict")
    
        
        # me all -> write, add write aceess
        # me all, write -> (write -> read), force unfollow
        # me all, write -> view, force unfollow
        # me all, write -> none, block
        Ownership.set_rights(user_object.id, dictionnaire.id, args.get("rights"))
        return jsonify({})