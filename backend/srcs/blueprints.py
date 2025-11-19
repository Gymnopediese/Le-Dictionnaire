from services import smorest
from imports.services import *
from flask_smorest.blueprint import Blueprint
# print(smorest.__dict__)
for key, val in smorest.__dict__.items():
    if type(val) is Blueprint and key != "Blueprint":
        api_object.register_blueprint(val)