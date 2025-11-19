from imports.forapi import *

from imports.models import *
@termes.route('/<string:id>')
class TermeAPI(MethodView):
    @termes.doc(description="Get a terme by ID")
    @termes.response(200, schema=TermeResponse)
    @decorator(object=Terme)
    def get(self, object):
        return jsonify(object.serialize(TermeResponse))
    
    @termes.doc(description="Update a temre by ID or Secret")
    @termes.arguments(TermeCreate)
    @termes.response(200, schema=UserResponse)
    @decorator(object=Terme, user=True)
    def put(self, args, object, user):
        print(args)
        args["content"] = Terme.join_paragraphs(args["paragraphs"])
        object.put_allowed(user["id"])
        object.put(args)
        Version.new(object)
        return jsonify({})
    
    @termes.doc(description="Delete a user by ID")
    @termes.response(204)
    @jwt_required()
    def delete(self, id):
        try:
            Terme.query.get(int(id))
        except:
            terme = Terme.query.filter_by(secret=id).first()
        user = get_jwt_identity()
        
        if not Author.query.filter_by(terme_id=terme.id, user_id=user["id"]).first():
            raise Exception(401, "you are not allowed to delete this ressource")
        
        db.session.delete(terme)
        db.session.commit()
        return jsonify({})
    
    