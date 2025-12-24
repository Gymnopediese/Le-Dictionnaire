from imports.forapi import *

from imports.models import *
@termes.route('/<string:id>')
class TermeAPI(MethodView):
    @termes.doc(description="Get a terme by ID")
    @termes.response(200, schema=TermeResponse)
    @decorator(object=Terme, user=True, autorename=True)
    def get(self, terme, user):
        return jsonify(terme.serialize(TermeResponse, user["id"]))
    
    @termes.doc(description="Update a temre by ID or Secret")
    @termes.arguments(TermeCreate)
    @termes.response(200)
    @decorator(object=Terme, user=True, autorename=True)
    def put(self, args, terme, user):
        args["content"] = Terme.join_paragraphs(args["paragraphs"])
        terme.put_allowed(user["id"])
        terme.metadatas_allowed(args["metadatas"], user["id"])
        DictionnaireTerme.put_terme_metadata(args["metadatas"], terme)
        Author.put_terme_metadata(args["metadatas"], terme)
        terme.visibility = args['metadatas']["visibility"]["data"]
        terme.put(args)
        Version.new(terme)
        return jsonify({})
    
    @termes.doc(description="Delete a user by ID")
    @termes.response(204)
    @decorator()
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
    
    