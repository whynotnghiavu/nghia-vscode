import os
import glob
import shutil
import json


def get_snippets_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/snippets')
    else:
        return os.path.expanduser('~/.config/Code/User/snippets')


source_folder = "../input/snippets"
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
        with open(file, 'r',encoding="utf-8") as f:
            content = f.read()

        snippet_name = os.path.splitext(os.path.basename(file))[0]
        snippet_body = content.splitlines()

        snippets[snippet_name] = {
            "prefix": snippet_name,
            "body": snippet_body,
            "description": snippet_name
        }

    output_file =  f"../output/snippets/{language}.json"
    output_files.append(output_file)
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(snippets, f, indent=2)

  


# Xóa toàn bộ thư mục
shutil.rmtree(snippets_path)
os.mkdir(snippets_path)   


# thay thế icon 🚀
for path in output_files:
    with open(path, "r", encoding="utf-8") as file:
        contents = file.read()
    contents = contents.replace("\\ud83d\\ude80", "🚀")
    with open(path, "w", encoding="utf-8") as file:
        file.write(contents)

for path in output_files:
    symlink_path = os.path.join(snippets_path, path.replace("../output/snippets/","") )


        
    try:
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
            print(f"Đã xóa symlink: {symlink_path}")
        os.symlink(os.path.abspath(path), symlink_path)
        print(f"Tạo link: {symlink_path}")
    except OSError as e:
        print(f"Lỗi: {e}")
 