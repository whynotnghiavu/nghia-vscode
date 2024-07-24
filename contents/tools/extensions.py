import json
import subprocess


command = "code --list-extensions"

extensions = subprocess.run(
    command,
    shell=True,
    check=True,
    stdout=subprocess.PIPE,
    text=True
).stdout.splitlines()

content = {
    "recommendations": extensions
}


with open("../../.vscode/extensions.json", "w") as json_file:
    json.dump(content, json_file, indent=4)
