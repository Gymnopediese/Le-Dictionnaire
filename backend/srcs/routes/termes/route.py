from imports.forapi import *

@termes.route('/')
class TermesAPI(MethodView):
    @termes.doc(description="Get all termes")
    @termes.response(200)
    @decorator()
    def get(self):
        termes = Terme.query.all()
        if termes:
            return jsonify([terme.serialize() for terme in termes])
        raise Exception(404, "User not found")
    
    @termes.doc(description="Create a user by ID")
    @termes.arguments(TermeCreate)
    @termes.response(200, schema=TermeResponse)
    @decorator(user=True)
    def post(self, args, user):
        # for id in args["dictionnaires"]:
        #     dictionnaire = Dictionnaire.query.get(id)
        #     if not dictionnaire:
        #         raise Exception(404, "Not a valid dictionnary")
        #     dictionnaire.put_allowed(user["id"])
        #     dictionnaire_link = DictionnaireTerme(dictionnaire_id=id, terme_id=terme.id)
        #     db.session.add(dictionnaire_link)
        # db.session.commit()
        Terme.metadatas_allowed(args["metadatas"], user["id"])
        terme = Terme(
            name=args["name"],
            content=Terme.join_paragraphs(args["paragraphs"]),
            metadatas=args["metadatas"],
            visibility=args['metadatas']["visibility"]["data"],
        )
        db.session.add(terme)
        db.session.commit()
        
        DictionnaireTerme.put_terme_metadata(args["metadatas"], terme)
        Author.put_terme_metadata(args["metadatas"], terme)
        
        

        author = Author(
            terme=terme,
            user_id=user["id"],
            rights="all",
        )
        db.session.add(author)
        db.session.commit()
        Version.new(terme)
        return jsonify(terme.serialize(TermeResponse))


