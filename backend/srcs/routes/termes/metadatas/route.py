from imports.forapi import *

from imports.models import *
@termes.route('/metadatas')
class TermeAPI(MethodView):
    @termes.doc(description="Update a temre by ID or Secret")
    @termes.response(200)
    @decorator()
    def get(self):
        return jsonify(allowed_metadata_types)
