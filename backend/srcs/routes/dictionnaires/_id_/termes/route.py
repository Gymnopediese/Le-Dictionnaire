from imports.forapi import *

@dictionnaires.route('/<string:id>/termes')
class DictionnaireApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.arguments(DictionnaireTermesGet, location="query")
    @dictionnaires.response(200, schema=DictionnaireFinalResponse)
    @decorator(autorename=True)
    def get(self, args, id):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        
        sort_by = args.get("sort_by", "name")
        starts_with = args.get("starts_with", "")
        amount = args.get("amount", 50)

        q = ( Terme.query
             .join(DictionnaireTerme, Terme.id == DictionnaireTerme.terme_id)
             .filter(DictionnaireTerme.dictionnaire_id == id) )

        if starts_with:
            q = q.filter(Terme.nom.ilike(f"{starts_with}%"))

        if sort_by in ["id", "name"]:
            q = q.order_by(getattr(Terme, sort_by))
            
        if sort_by in ["ctime", "utime"]:
            q = q.order_by(getattr(Terme, sort_by).desc())#getattr(DictionnaireTerme, sort_by))
        

        if amount:
            q = q.limit(amount)
        print(amount, args)
        res = [t.serialize(DictionnaireTermeResponse) for t in q.all()]
        print(res)
        return jsonify(res)