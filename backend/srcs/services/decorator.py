from functools import wraps
from services.jwt import *
from flask import request


def decorator(user=False, user_db=None, object=None, object2=None, check_jwt=True, autorename = False, get_allow_result=False, check_allowed=True):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            args = list(args)
            final_kwargs = {}
            if not check_jwt:
                return
            try:
                verify_jwt_in_request()
                user_data = (get_jwt_identity())
            except Exception as e:
                print(e)
                raise Exception(405, "Unotorized token boy.")


            if user and not user_db:
                final_kwargs["user"] = user_data
                
            if user_db:       
                user_object = user_db.query.get(user_data["id"])
                if not user_object:
                    raise Exception(404, "User not found.")
                final_kwargs["user"] = user_object
            # Enlevel les enum de merde
            for arg in args:
                if type(arg) != dict:
                    continue
                for i in arg.keys():
                    if "enum" in str(type(arg[i])):
                        arg[i] = arg[i].value

            if ("id" in kwargs and object):
                if kwargs["id"] == "me" and object.__name__.lower() == "user":
                    kwargs["id"] = user_data["id"]
                try:
                    terme = object.query.get(int(kwargs["id"]))
                except:
                    terme = object.query.filter_by(secret=kwargs["id"]).first()
                    
                if terme == None:
                    raise Exception(404, "Cannot found ressource.")
                
                if not autorename:
                    final_kwargs["object"] = terme
                elif object.__name__.lower() in final_kwargs:
                    final_kwargs[object.__name__.lower()+"_object"] = terme
                else:
                    final_kwargs[object.__name__.lower()] = terme
                
                if check_allowed:
                    if request.method == "GET":
                        allow_result = terme.get_allowed(user_data['id'])
                    elif request.method == "POST":
                        allow_result = terme.post_allowed(user_data['id'])
                    elif request.method == "PUT":
                        allow_result = terme.put_allowed(user_data['id'])
                    elif request.method == "DELETE":
                        allow_result = terme.delete_allowed(user_data['id'])
                    else:
                        raise Exception(405, "not allowed")
            elif "id" in kwargs:
                try:
                    final_kwargs["id"] = int(kwargs["id"])
                except:
                    raise Exception(422, "unprocessable id")
            if ("id2" in kwargs and object2):
                if kwargs["id2"] == "me" and object2.__name__.lower() == "user":
                    kwargs["id2"] = user_data["id"]
                try:
                    terme = object2.query.get(int(kwargs["id2"]))
                except:
                    terme = object2.query.filter_by(secret=kwargs["id2"]).first()
                    
                if terme == None:
                    raise Exception(404, "Cannot found ressource.")
                
                if not autorename:
                    final_kwargs["object2"] = terme
                elif object2.__name__.lower() in final_kwargs:
                    final_kwargs[object2.__name__.lower()+"_object"] = terme
                else:
                    final_kwargs[object2.__name__.lower()] = terme
                
                if check_allowed:
                    if request.method == "GET":
                        terme.get_allowed(user_data['id'])
                    elif request.method == "POST":
                        terme.post_allowed(user_data['id'])
                    elif request.method == "PUT":
                        terme.put_allowed(user_data['id'])
                    elif request.method == "DELETE":
                        terme.delete_allowed(user_data['id'])
                    else:
                        raise Exception(405, "not allowed")
                
                
            
            if len(args) > 1:
                final_kwargs["args"] = args[1]
            if get_allow_result:
                final_kwargs[get_allow_result] = allow_result
            return fn(args[0], **final_kwargs)
            # except Exception as e:
            #     raise Exception(500, f"{fn} request for incorrect arguments", e)
        return decorator
    return wrapper
