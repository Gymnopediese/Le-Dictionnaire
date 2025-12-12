srcs_routes = False
if not srcs_routes:
	from routes.dictionnaires.enum import *
	from routes.termes.enum import *
	from routes.termes.metadatas.enum import *
	from routes.users._id_.relationship.enum import *
	srcs_routes = True