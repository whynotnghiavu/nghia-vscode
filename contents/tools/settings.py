import os
import json
# pip install json5
import json5


def read_json_with_comments():
    with open("../../nghia-vscode.code-workspace", 'r', encoding="utf-8") as file:
        json_with_comments = file.read()
        json_data = json5.loads(json_with_comments)
    return json_data


def get_settings_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/settings.json')
    else:
        return os.path.expanduser('~/.config/Code/User/settings.json')


content = read_json_with_comments()
nghia_settings = "../../.vscode/settings.json"
settings_path = get_settings_path()


with open(nghia_settings, "w", encoding="utf-8") as json_file:
    json.dump(content["settings"], json_file, indent=4)


try:
    if os.path.exists(settings_path):
        os.remove(settings_path)
        print(f"Đã xóa symlink: {settings_path}")
    os.symlink(os.path.abspath(nghia_settings), settings_path)
    print(f"Tạo link: {settings_path}")
except OSError as e:
    print(f"Lỗi: {e}")
