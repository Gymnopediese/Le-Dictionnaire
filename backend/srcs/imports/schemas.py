srcs_routes = False
if not srcs_routes:
	from imports.enums import *
	from routes.auth.password.schema import *
	from routes.auth.signin.schema import *
	from routes.auth.signup.schema import *
	from routes.dictionnaires.schema import *
	from routes.dictionnaires._id_.termes.schema import *
	from routes.me.dictionnaires.schema import *
	from routes.me.user.schema import *
	from routes.termes.schema import *
	from routes.termes._id_.dictionnaires.schema import *
	from routes.termes.metadatas.schema import *
	from routes.users.schema import *
	from routes.users._id_.relationship.schema import *
	srcs_routes = True