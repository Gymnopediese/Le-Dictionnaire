from services.app import app
from services.jwt import *
from flask_smorest import Api, Blueprint
from flask import request


class APIConfig:
    API_TITLE = "API for the backend"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_UI_URL = "https://cdn.jsdelivr.net/npm/redoc/bundles/"
    #     # Swagger security definition for JWT
    # # Add Security Definitions
    # OPENAPI_SECURITY_SCHEMES = {
    #     "BearerAuth": {
    #         "type": "http",
    #         "scheme": "bearer",
    #         "bearerFormat": "JWT"
    #     }
    # }
    
    # # Apply security globally
    # OPENAPI_SECURITY = [{"BearerAuth": []}]



app.config.from_object(APIConfig)

api_object = Api(app)



api_object.spec.components.security_scheme(
    "BearerAuth",
    {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    },
)

# @app.before_request
# def rewrite_me_routes():
#     """Intercept requests and rewrite '/me/...' to '/<current_user_id>/...'"""
    # if request.path.startswith("/me/"):
    #     current_user_id = get_jwt_identity()["id"]
    #     new_path = request.path.replace("/me/", f"/users/{current_user_id}/", 1)
    #     request.environ["PATH_INFO"] = new_path  # Modify the request path

    
    


termes = Blueprint("termes", "termes", url_prefix="/termes", description="Request my data",)
users = Blueprint("users", "users", url_prefix="/users", description="Users for the backend",)
auth = Blueprint("auth", "auth", url_prefix="/auth", description="Authentification for the backend",)
dictionnaires =  Blueprint("dictionnaires", "dictionnaires", url_prefix="/dictionnaires", description="Dictionnaire for the backend",)
me = Blueprint("me", "me", url_prefix="/me", description="Request my data",)
test = Blueprint("test", "test", url_prefix="/test", description="Test my data",)