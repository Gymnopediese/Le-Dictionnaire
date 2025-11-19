from flask.views import MethodView
import enum
from marshmallow import Schema, fields
from hashlib import sha256
from copy import copy