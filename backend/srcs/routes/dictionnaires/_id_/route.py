from imports.forapi import *

@dictionnaires.route('/<string:id>')
class DictionnaireApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.response(200, schema=DictionnaireResponse)
    @decorator(object=Dictionnaire, user=True, autorename=True, get_allow_result="rights")
    def get(self, dictionnaire, user, rights):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        res = dictionnaire.serialize(DictionnaireResponse)
        res["rights"] = rights
        print("right ?", rights)
        return res
    
