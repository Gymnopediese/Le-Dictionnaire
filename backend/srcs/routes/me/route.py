from imports.forapi import *

@me.route('/')
class MeAPI(MethodView):
    
    @me.doc(description="Get me")
    @me.response(200, schema=MeResponse)
    @decorator(user_db=User)
    def get(self, user):
        """
        Get the info of the user who made the request.
        ---
        responses:
            200:
                description: User
        """
        return jsonify(user.serialize(MeResponse))
    
    # @users.doc(description="Update a user by ID")
    # @users.arguments(UpdateUser)
    # @users.response(200, schema=UserResponse)
    # @jwt_required()
    # def put(self, args, id):
    #     user = User.query.get(id)
    #     user.update(**args)
    #     db.session.commit()
    #     return jsonify(user.serialize())
    
    # @users.doc(description="Delete a user by ID")
    # @users.response(204)
    # @jwt_required()
    # def delete(self, id):
    #     user = User.query.get(id)
    #     db.session.delete(user)
    #     db.session.commit()
    #     return jsonify({})
    
