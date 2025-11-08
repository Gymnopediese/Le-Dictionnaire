from imports.models import *

@me.route('/')
class MeAPI(MethodView):
    @me.doc(description="Get me")
    @me.response(200, schema=UserResponse)
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.get(current_user["id"])
        if user:
            return jsonify(user.serialize())
        raise Exception(404, "User not found")
    
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
    
