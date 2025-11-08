from pathlib import Path

# make your own path_to_import function
def path_to_import(path):
    path = str(path).replace("srcs/", "").replace("/", ".").replace(".py", "")
    return f"from {path} import *\n"
def generate_import_file(path, output, pattern="*.py", dependencies = []):
    imports = ""
    for _path in dependencies:
        if "from " in _path:
            imports += _path
        else:
            imports += path_to_import(_path)
    for path in Path(path).rglob(pattern):
        path = str(path)
        if path == output or "__" in path:
            continue
        imports += path_to_import(path)
    with open(output, "w") as f:
        f.write(imports)
    return output

def main():
    methodview = "from flask.views import MethodView\n"
    schemas = generate_import_file("srcs/routes", "srcs/imports/schemas.py", "*schema.py")
    services = generate_import_file("srcs/services", "srcs/imports/services.py", "*.py", [schemas, methodview])
    generate_import_file("srcs/routes", "srcs/imports/routes.py", "*route.py", [services])
    generate_import_file("srcs/models", "srcs/imports/models.py", "*.py", [services])
    generate_import_file("srcs/tests", "srcs/imports/tests.py", "*.py", [services])
    generate_import_file("srcs/imports", "srcs/imports/all.py", "*.py")
    print("done !")

if __name__ == "__main__":
    main()