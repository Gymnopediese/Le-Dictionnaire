srcs_models = False
if not srcs_models:
	from models.dictionnaire.dictionnaire import *
	from models.dictionnaire.dictionnaire_termes import *
	from models.dictionnaire.ownership import *
	from models.terme.author import *
	from models.terme.link import *
	from models.terme.reaction import *
	from models.terme.suggestion import *
	from models.terme.terme import *
	from models.terme.version import *
	from models.user.ip import *
	from models.user.relationship import *
	from models.user.user import *
	srcs_models = True