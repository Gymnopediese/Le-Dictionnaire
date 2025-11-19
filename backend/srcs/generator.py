from pathlib import Path

# make your own path_to_import function
def path_to_import(path):
    path = str(path).replace("srcs/", "").replace("/", ".").replace(".py", "")
    return f"\tfrom {path} import *\n"
def generate_import_file(folder, output, pattern="*.py", dependencies = []):
    imports = f"{folder.replace('/', '_')} = False\n"
    imports += f"if not {folder.replace('/', '_')}:\n"
    for _path in dependencies:
        if "from " in _path:
            imports += "\t" + _path
        else:
            imports += path_to_import(_path)
    for path in Path(folder).rglob(pattern):
        path = str(path)
        if path == output or "__" in path:
            continue
        imports += path_to_import(path)
    imports += f"\t{folder.replace('/', '_')} = True"
    with open(output, "w") as f:
        f.write(imports)
    return output

def main():
    extern = "from imports.extern import *\n"
    services = generate_import_file("srcs/services", "srcs/imports/services.py", "*.py", [extern])
    model = generate_import_file("srcs/models", "srcs/imports/models.py", "*.py")
    enum = generate_import_file("srcs/routes", "srcs/imports/enums.py", "*enum.py")
    responses = generate_import_file("srcs/routes", "srcs/imports/responses.py", "*response.py", [enum])
    schemas = generate_import_file("srcs/routes", "srcs/imports/schemas.py", "*schema.py", [enum])
    
    generate_import_file("srcs/routes", "srcs/imports/forapi.py", "koko", [services, model, schemas, responses])

    generate_import_file("srcs/routes", "srcs/imports/routes.py", "*route.py")
    generate_import_file("srcs/tests", "srcs/imports/tests.py", "*.py")
    
    generate_import_file("srcs/imports", "srcs/imports/all.py", "*.py")
    print("done !")

if __name__ == "__main__":
    main()