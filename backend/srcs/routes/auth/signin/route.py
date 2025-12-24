from imports.forapi import *

@auth.route('/signin', methods=['POST'])
@auth.doc(description="Login to an existing account")
@auth.arguments(LoginUser)
@auth.response(201, schema=LoginResponse)
def signin(params):
    """
    Login to an existing account.
    """
    credential = params.get("username")
    password = params.get("password")
    user = User.query.filter_by(username=credential).first()
    if user and user.check_password(password):
        return jsonify({'token': user.generate_token()})
    raise Exception(401, "Invalid username or password")


