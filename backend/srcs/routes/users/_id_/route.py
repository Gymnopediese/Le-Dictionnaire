from imports.forapi import *

security = [{"BearerAuth": []}]
security = []

@users.route('/<string:id>')
class UsersAPI(MethodView):

    @users.doc(description="Get all users", security=security) 
    @users.response(200)
    @decorator(user=True, object=User, autorename=True, check_allowed=False)
    def get(self, user, user_object):
        res = user_object.serialize(UserResponse)
        relationship = Relationship.get_type(user_id=user["id"], target_id=user_object.id)
        otherway_relationship = Relationship.get_type(target_id=user["id"], user_id=user_object.id)
        
        if relationship == "stranger" and otherway_relationship == "stranger":
            res["relationship"] = "stranger"
        # blocked me
        elif otherway_relationship == "blocked":
            raise Exception(405, "Not allowed")  
        # blocked him
        elif relationship == "blocked":
            res["relationship"] = "blocked"
        # friends
        elif relationship == otherway_relationship and relationship == "follow":
            res["relationship"] = "friend" 
        elif relationship == "follow":
            res["relationship"] = "follow"
        elif otherway_relationship == "follow":
            res["relationship"] = "following"
        
        
        
        return jsonify(res)

    # @users.doc(description="Create a User")
    # @users.arguments(CreateUser)
    # @users.response(201, schema=LoginResponse)
    # @jwt_required()
    # def post(self, args):
    #     user = User.new(**args)
    #     db.session.add(user)
    #     db.session.commit()
    #     return jsonify({"token": user.generate_token()})

