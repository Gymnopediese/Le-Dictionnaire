from imports.forapi import *

@me.route('/users')
class MeUsersAPI(MethodView):
    
    @me.doc(description="Get relationships")
    @me.response(200)
    @me.arguments(MeUserGet, location="query")
    @decorator(user=User)
    def get(self, args, user):

        relationship_types = args.get("relationship_types")

        uid = user["id"]
        q = Relationship.query

        if "friend" in relationship_types:
            q = Relationship.get_friends(uid)
            print("ah merde mdr")

        if "following_only" in relationship_types:
            q = Relationship.get_followings(uid)

        if "following" in relationship_types:
            q = Relationship.query.filter_by(user_id=uid, type="follow")


        if "follower_only" in relationship_types:
            q = Relationship.get_followers(uid)
            results = q.all()
            return jsonify([relationship.serialize(MeRelationshipReverseResponse) for relationship in results])

        if "follower" in relationship_types:
            q = Relationship.query.filter_by(target_id=uid, type="follow")
            results = q.all()
            return jsonify([relationship.serialize(MeRelationshipReverseResponse) for relationship in results])
            
        if "blocked" in relationship_types:
            q = q.filter(
                (Relationship.user_id == uid) &
                (Relationship.type == "blocked")
            )

        results = q.all()
        return jsonify([relationship.serialize(MeRelationshipResponse) for relationship in results])
