import sys
import re

def change_the_directory(current_path, new_path):
    # Avoid the duplicate /'s in the new path
    mod_new_path = re.sub(r'/{2,}', '/', new_path)

    # 1. If current path is "/"
    if current_path == "/":
        # Handling the scenario if new path contains starting "/"
        return current_path + mod_new_path.lstrip("/")
    
    # 2. folder name wihout starting /
    if re.match("[a-zA-Z0-9_]", mod_new_path):
        return current_path + "/" + mod_new_path
    
    # 3. Handling mod_new_path is only '/'
    if mod_new_path.startswith('/'):
        return mod_new_path

    # Split the paths into components
    current_components = current_path.split('/')
    new_components = mod_new_path.split('/')
    
    # 4. if we have only "." in a string
    if "/" not in mod_new_path and '.' in mod_new_path:
        list_double_dots = re.findall(r'.{2}', mod_new_path)
        print(list_double_dots)
        if len(list_double_dots) <= len(list(filter(None, current_components))):
            for ele in list_double_dots:
                if ele == "..":
                    current_components.pop()
                else:
                    return f"{mod_new_path}: No such file or directory"
            return "/".join(current_components)
        else:
            return f"{mod_new_path}: No such file or directory"

    # Traverse the new path components
    for component in new_components:
        if component == '.':
            continue
        elif component == '..':
            if len(current_components) > 1:  # Ensure not at root
                current_components.pop()
        else:
            current_components.append(component)
    return '/'.join(["/"] if len(current_components) == 1 and current_components[0] == "" else current_components)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <current_directory> <new_directory>")
        sys.exit(1)
    
    current_directory = sys.argv[1]
    new_directory = sys.argv[2]

    result = change_the_directory(current_directory, new_directory)
    print(result)