import subprocess
import os
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

def run_command(command):
    try:
        if "assetfinder" in command:
            process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=True)
        else:    
            process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        stdout,stderr =process.communicate()
        if process.returncode != 0:
            tool_name = command[0]
            print(f"Error: {tool_name} {stderr.strip()}")
            return False
        return True
    except FileNotFoundError:
        print(f"{tool_name}, Command not found.")
        return False

def run_subfinder(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"Subfinder-{domain}-{date}.txt")
    command=["subfinder","-d",domain,"-rL","resolvers.txt","-o",of]
    
    if run_command(command):
        print(f"\033[92m[*] Subfinder: Subdomain scan successful.\033[1m")
        return of
    return None

def run_amass(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"Amass-{domain}-{date}.txt")
    command = ["amass","enum","-passive","-d",domain,"-rf","resolvers.txt","-o",of]
    if run_command(command):
        with open(of,"r") as f:
            tarama = f.readlines()
    subdomains = set()
    for i in tarama:
        if "FQDN" in i:
            if "sibervatan.org" in i:
                subdomains.add(i.split()[0])

    with open(of,"w") as f:
        for i in subdomains:
            f.writelines(f"{i}\n")        
                
        print(f"\033[92m[*] Amass: Subdomain scan successful.\033[1m")
        return of
    return None

def run_assetfinder(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"Assetfinder-{domain}-{date}.txt")
    command = f"assetfinder -subs-only {domain} > {of}"
    if run_command(command):
        print(f"\033[92m[*] Assetfinder: Subdomain scan successful.\033[1m")
        return of
    return None