from imports.forapi import *

@dictionnaires.route('/<string:id>')
class DictionnaireApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.response(200, schema=DictionnaireFinalResponse)
    @decorator(object=Dictionnaire)
    def get(self, object):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        print("je vais rendre ca gros, " ,object.serialize(DictionnaireResponse))
        return object.serialize(DictionnaireResponse)
    
