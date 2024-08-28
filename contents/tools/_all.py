import os
import subprocess

print(os.getcwd())
os.chdir(os.getcwd())


if os.name == 'nt':
    print("extensions.py")
    subprocess.call(["python", "extensions.py"])

#     print("keybindings.py")
#     subprocess.call(["python", "keybindings.py"])

#     print("settings.py")
#     subprocess.call(["python", "settings.py"])

#     print("snippets.py")
#     subprocess.call(["python", "snippets.py"])

# else:
#     print("extensions.py")
#     subprocess.call(["python3", "extensions.py"])

#     print("keybindings.py")
#     subprocess.call(["python3", "keybindings.py"])

#     print("settings.py")
#     subprocess.call(["python3", "settings.py"])

#     print("snippets.py")
#     subprocess.call(["python3", "snippets.py"])
