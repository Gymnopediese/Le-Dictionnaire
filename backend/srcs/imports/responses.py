srcs_routes = False
if not srcs_routes:
	from imports.enums import *
	from routes.dictionnaires.response import *
	from routes.dictionnaires._id_.response import *
	from routes.dictionnaires._id_.ownership._id2_.response import *
	from routes.dictionnaires._id_.termes.response import *
	from routes.me.response import *
	from routes.me.dictionnaires.response import *
	from routes.me.termes.response import *
	from routes.me.user.response import *
	from routes.termes.response import *
	from routes.users._id_.response import *
	srcs_routes = True