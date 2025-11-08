from imports.models import *

security = [{"BearerAuth": []}]
security = []

@users.route('/')
class UsersAPI(MethodView):
    @users.doc(description="Get all users", security=security) 
    @users.arguments(UserListQuery, location="query")
    @users.response(200, schema=UserListResponse)
    @jwt_required()
    def get(self, args):
        order_by = args.get("order_by", UserOrderByEnum.username)
        order = args.get("order", OrderEnum.asc)
        limit = args.get("limit")
        start = args.get("start", 0)
        order_by = {
            UserOrderByEnum.username: User.username,
            UserOrderByEnum.email: User.email,
            UserOrderByEnum.age: User.age,
        }[order_by]
        reverse = order == "desc"
        query = User.query.order_by(order_by)
        query = query.offset(start)
        if reverse:
            query = query.reverse()
        if limit is not None:
            query = query.limit(limit)
        users = query.all()
        return jsonify({"users": [user.serialize() for user in users]})

    # @users.doc(description="Create a User")
    # @users.arguments(CreateUser)
    # @users.response(201, schema=LoginResponse)
    # @jwt_required()
    # def post(self, args):
    #     user = User.new(**args)
    #     db.session.add(user)
    #     db.session.commit()
    #     return jsonify({"token": user.generate_token()})

