srcs_routes = False
if not srcs_routes:
	from routes.auth.password.route import *
	from routes.auth.signin.route import *
	from routes.auth.signup.route import *
	from routes.dictionnaires.route import *
	from routes.dictionnaires._id_.route import *
	from routes.dictionnaires._id_.ownership._id2_.route import *
	from routes.dictionnaires._id_.termes.route import *
	from routes.dictionnaires._id_.termes._id2_.route import *
	from routes.dictionnaires.me.route import *
	from routes.me.route import *
	from routes.me.dictionnaires.route import *
	from routes.me.termes.route import *
	from routes.me.user.route import *
	from routes.termes.route import *
	from routes.termes._id_.route import *
	from routes.termes._id_.dictionnaires.route import *
	from routes.termes.metadatas.route import *
	from routes.test.route import *
	from routes.users.route import *
	from routes.users._id_.route import *
	from routes.users._id_.relationship.route import *
	srcs_routes = True