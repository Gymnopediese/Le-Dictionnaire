from imports.forapi import *
from hashlib import sha256

waiting_users = []

@auth.route("/signup", methods=["POST"])
@auth.doc(description="Try to create a new user by sending a confirmation mail.")
@auth.arguments(CreateUser)
@auth.response(201, schema=LoginResponse)
def sign_up(arguments):
    """
    Try to create a new user.
    """
    request.remote_addr
    username = arguments.get("username")
    password = sha256(arguments.get("password").encode()).hexdigest()

    if User.exists(username=username):
        raise Exception(400, "username already taken")

    user = User(
        username=username,
        password=password,
    )
    
    db.session.add(user)
    db.session.commit()
    return jsonify(token=user.generate_token())
