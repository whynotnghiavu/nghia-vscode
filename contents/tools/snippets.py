import os
import glob
import shutil
import json


def get_snippets_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/snippets')
    else:
        return os.path.expanduser('~/.config/Code/User/snippets')


source_folder = "../snippets"
snippets_path = get_snippets_path()


list_language = {
    "python": "py",
    "latex": "tex",
}

output_files = []

for language, extension in list_language.items():
    templates = os.path.join(source_folder, language)
    files = glob.glob(os.path.join(templates, f'**/*.{extension}'), recursive=True)

    snippets = {}

    for file in files:
        with open(file, 'r') as f:
            content = f.read()

        snippet_name = os.path.splitext(os.path.basename(file))[0]
        snippet_body = content.splitlines()

        snippets[snippet_name] = {
            "prefix": snippet_name,
            "body": snippet_body,
            "description": snippet_name
        }

    output_file = os.path.join(source_folder, f"{language}.json")
    output_files.append(output_file)
    with open(output_file, 'w') as f:
        json.dump(snippets, f, indent=2)


# Xóa toàn bộ thư mục
shutil.rmtree(snippets_path)
os.mkdir(snippets_path)  # Tạo lại thư mục trống



# 🚀
for path in output_files:
    with open(path, "r", encoding="utf-8") as file:
        contents = file.read()
    contents = contents.replace("\\u00f0\\u0178\\u0161\\u20ac", "🚀") 
    with open(path, "w", encoding="utf-8") as file:
        file.write(contents)


    





for path in output_files:
    symlink_path = os.path.join(snippets_path, path)

    if os.path.exists(symlink_path):
        print(f"The symbolic link already exists: {path}")
    else:
        try:
            os.symlink(os.path.abspath(path), symlink_path)
            print(f"Symbolic link created at: {symlink_path}")
        except OSError as e:
            print(f"Failed to create symbolic link: {e}")
