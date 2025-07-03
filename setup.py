import subprocess
import shutil

def is_installed(tool):
    return shutil.which(tool) is not None

def install_tool(cmd):
    subprocess.run(cmd, shell=True, check=True)

tools = {
    "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
    "subfinder": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "amass": "go install github.com/owasp-amass/amass/v3/...@master"
}

for tool, install_cmd in tools.items():
    if not is_installed(tool):
        print(f"{tool} not found, installing...")
        install_tool(install_cmd)
    else:
        print(f"{tool} is already installed.")

print("\n✅ Installation completed!")
print("\n🔁 Note: Make sure the go/bin directory is added to your PATH (e.g., in your ~/.bashrc or ~/.zshrc):")
print("export PATH=$PATH:$(go env GOPATH)/bin")
