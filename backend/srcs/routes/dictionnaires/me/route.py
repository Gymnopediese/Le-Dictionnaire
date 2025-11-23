from imports.forapi import *

@dictionnaires.route('/me')
class DictionnaireMeApi(MethodView):
    
    @dictionnaires.doc(description="Get a particular dictionnary")
    @dictionnaires.response(200, schema=DictionnaireFinalResponse)
    @decorator()
    def get(self):
        """
        Get all content need for a particular dictionnary.
        ---
        responses:
            200:
                description: User
        """
        return redirect("/api/me/termes", code=302)
    
