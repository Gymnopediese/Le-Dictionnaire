from imports.models import *


@termes.route('/')
class TermesAPI(MethodView):
    @termes.doc(description="Get all termes")
    @termes.response(200)
    @jwt_required()
    def get(self):
        termes = Terme.query.all()
        if termes:
            return jsonify([terme.serialize() for terme in termes])
        raise Exception(404, "User not found")
    
    @termes.doc(description="Create a user by ID")
    @termes.arguments(CreateTerme)
    @termes.response(200, schema=CreateTerme)
    @jwt_required()
    def post(self, args):
        user = get_jwt_identity()
        
        print(args)
        terme = Terme(
            name=args["name"],
            genre=args["genre"].value,
            type=args["type"].value,
        )
        db.session.add(terme)
        db.session.commit()
        author = Author(
            terme=terme,
            user_id=user["id"],
        )
        db.session.add(author)
        db.session.commit()

        for i, contenu in enumerate(args["contenus"]):
            cont = Contenu(
                contenu=contenu["contenu"],
                type=contenu["type"],
                terme=terme,
                order=i,
            )
            db.session.add(cont)
        db.session.commit()
        return jsonify(terme.serialize())


@termes.route('/<int:id>')
class TermeAPI(MethodView):
    @termes.doc(description="Get a terme by ID")
    @termes.response(200, schema=UserResponse)
    @jwt_required()
    def get(self, id):
        terme = Terme.query.get(id)
        return jsonify(terme.serialize())
    
    @termes.doc(description="Update a user by ID")
    @termes.arguments(UpdateUser)
    @termes.response(200, schema=UserResponse)
    @jwt_required()
    def put(self, args, id):
        terme = Terme.query.get(id)
        terme.update(**args)
        db.session.commit()
        return jsonify(terme.serialize())
    
    @termes.doc(description="Delete a user by ID")
    @termes.response(204)
    @jwt_required()
    def delete(self, id):
        terme = Terme.query.get(id)
        user = get_jwt_identity()
        
        if not Author.query.filter_by(terme_id=terme.id, user_id=user["id"]).first():
            raise Exception(401, "you are not allowed to delete this ressource")
        
        db.session.delete(terme)
        db.session.commit()
        return jsonify({})
    
    