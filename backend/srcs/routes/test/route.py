from imports.forapi import *


@test.route('/')
class TestApi(MethodView):
    @test.doc(description="Test stuff")
    @test.response(200, schema=MeResponse)
    @decorator(user_db=User)
    def get(self, user):
        """
        Get the info of the current user.
        ---
        responses:
            200:
                description: User
        """
        return jsonify(user.serialize(MeResponse))