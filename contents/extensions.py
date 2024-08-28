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


# "editorconfig.editorconfig",

# "mikestead.dotenv",
# "archsense.architecture-view-nestjs",
# "formulahendry.auto-rename-tag",
# "ritwickdey.liveserver",

# "ms-vscode-remote.remote-wsl",
# "kamikillerto.vscode-colorize",
# "blackboxapp.blackbox",
# "ms-vscode.cpptools-themes",
# "ms-vscode.cpptools-extension-pack",
# "ms-vscode.cpptools",
# "AMiner.codegeex",
# "humao.rest-client",
# "dbaeumer.vscode-eslint",
# "xabikos.reactsnippets",
# "twxs.cmake",
# "ms-kubernetes-tools.vscode-kubernetes-tools",
# "Codeium.codeium",
# "MEngRBatinov.json-snippet-to-md-documentation",
# "ms-vscode-remote.remote-containers",
# "ms-vscode.cmake-tools",
# "redhat.vscode-yaml",
# "austenc.tailwind-docs",
# "alefragnani.bookmarks",
# "almenon.arepl",
# "grapecity.gc-excelviewer",
# "ms-toolsai.jupyter",
# "ms-toolsai.jupyter-keymap",
# "ms-toolsai.jupyter-renderers",
# "ms-toolsai.vscode-jupyter-cell-tags",
# "ms-toolsai.vscode-jupyter-slideshow",
# "ms-vscode-remote.remote-wsl",
# "steoates.autoimport",
# "usernamehw.errorlens",



