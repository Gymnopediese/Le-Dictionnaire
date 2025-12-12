from imports.forapi import *

@me.route('/dictionnaires')
class MeDictionnairesAPI(MethodView):
    
    @me.doc(description="Get me")
    @me.response(200)
    @me.arguments(MeDictionnairesGet, location="query")
    @decorator(user=User)
    def get(self, args, user):

        rights_less_than = args.get("rights_less_than")
        rights_higher_than = args.get("rights_higher_than")
        rights_in = args.get("rights_in", [])
        
        q = Ownership.query.filter_by(user_id=user["id"])  # ou votre modèle

        if rights_less_than:
            level = rights_level[rights_less_than]
            q = q.filter(Ownership.rights.in_([r for r, l in rights_level.items() if l <= level]))

        if rights_higher_than:
            level = rights_level[rights_higher_than]
            q = q.filter(Ownership.rights.in_([r for r, l in rights_level.items() if l >= level]))
        print(rights_in)
        if rights_in:
            q = q.filter(Ownership.rights.in_(rights_in))

        results = q.all()
        print(results)
        return jsonify([dictionnaire.serialize(MeOwnershipResponse) for dictionnaire in results])
