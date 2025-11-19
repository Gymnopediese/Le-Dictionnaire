srcs_routes = False
if not srcs_routes:
	from routes.users.route import *
	from routes.users._id_.route import *
	from routes.auth.password.route import *
	from routes.auth.signin.route import *
	from routes.auth.signup.route import *
	from routes.me.route import *
	from routes.termes.route import *
	from routes.termes._id_.route import *
	from routes.termes._id_.dictionnaires.route import *
	from routes.dictionnaires.route import *
	from routes.dictionnaires._id_.route import *
	from routes.test.route import *
	srcs_routes = True