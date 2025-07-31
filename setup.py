#!/usr/bin/env python3
"""
SubDojo - Advanced Subdomain Enumeration Tool
Setup script for installing dependencies and required tools
"""

import subprocess
import shutil
import sys
import os
from pathlib import Path

def is_installed(tool):
    """Check if a tool is installed and accessible"""
    return shutil.which(tool) is not None

def install_tool(cmd):
    """Install a tool using the provided command"""
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing tool: {e}")
        return False

def install_python_deps():
    """Install Python dependencies from requirements.txt"""
    print("\n📦 Installing Python dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Python dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Python dependencies: {e}")
        return False

def check_go_installation():
    """Check if Go is installed and properly configured"""
    if not is_installed("go"):
        print("❌ Go is not installed!")
        print("Please install Go first:")
        print("Ubuntu/Debian: sudo apt install golang-go")
        print("macOS: brew install go")
        print("Windows: Download from https://golang.org/dl/")
        return False
    
    try:
        result = subprocess.run(["go", "version"], capture_output=True, text=True, check=True)
        print(f"✅ Go version: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("❌ Go installation check failed")
        return False

def setup_resolvers():
    """Create resolvers.txt file with default DNS servers"""
    resolvers_file = Path("resolvers.txt")
    if not resolvers_file.exists():
        print("\n🔧 Creating resolvers.txt with default DNS servers...")
        default_resolvers = [
            "# Public DNS Servers for Subdomain Enumeration",
            "1.1.1.1",
            "8.8.8.8",
            "8.8.4.4",
            "1.0.0.1",
            "208.67.222.222",
            "208.67.220.220"
        ]
        with open(resolvers_file, "w") as f:
            f.write("\n".join(default_resolvers))
        print("✅ resolvers.txt created successfully!")

def main():
    """Main setup function"""
    print("🚀 SubDojo Setup Script")
    print("=" * 50)
    
    # Check Go installation
    if not check_go_installation():
        return False
    
    # Install Python dependencies
    if not install_python_deps():
        return False
    
    # Install Go tools
    print("\n🔧 Installing Go tools...")
    tools = {
        "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
        "subfinder": "go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "amass": "go install github.com/owasp-amass/amass/v3/...@master"
    }
    
    for tool, install_cmd in tools.items():
        if not is_installed(tool):
            print(f"📦 Installing {tool}...")
            if install_tool(install_cmd):
                print(f"✅ {tool} installed successfully!")
            else:
                print(f"❌ Failed to install {tool}")
        else:
            print(f"✅ {tool} is already installed.")
    
    # Setup resolvers.txt
    setup_resolvers()
    
    # Final instructions
    print("\n" + "=" * 50)
    print("✅ SubDojo setup completed!")
    print("\n📝 Next steps:")
    print("1. Make sure the go/bin directory is added to your PATH:")
    print("   export PATH=$PATH:$(go env GOPATH)/bin")
    print("2. Add this line to your ~/.bashrc or ~/.zshrc for permanent setup")
    print("3. Configure API keys in config.yaml (optional)")
    print("4. Run: python3 main.py -d example.com")
    print("\n🔐 Remember: Only use on authorized domains!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
