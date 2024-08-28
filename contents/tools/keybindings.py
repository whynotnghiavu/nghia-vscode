import os
# import json
# pip install json5
# import json5


def get_keybindings_path():
    if os.name == 'nt':
        return os.path.expanduser('~/AppData/Roaming/Code/User/keybindings.json')
    else:
        return os.path.expanduser('~/.config/Code/User/keybindings.json')


nghia_keybindings_json = "../shortcuts/keybindings.json"
keybindings_path = get_keybindings_path()


if os.path.exists(keybindings_path):
    os.remove(keybindings_path)


try:
    os.symlink(os.path.abspath(nghia_keybindings_json), keybindings_path)
    print(f"Symbolic link created at: {keybindings_path}")
except OSError as e:
    print(f"Failed to create symbolic link: {e}")
