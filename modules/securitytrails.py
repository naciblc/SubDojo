import os
import requests
import yaml
from modules.virustotal import date

def securitytrails(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"SecurityTrails-{domain}-{date}.txt")
    with open("config.yaml","r")as f:
        api_key = yaml.safe_load(f)
    headers = {
        "Content-Type":"application/json",
        "Apikey":f"{api_key['securitytrails']['api_key']}"
    }
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    response = requests.get(url,headers=headers)
    op = response.json()
    for subdomain in op['subdomains']:
        with open(of,"a") as f:
            f.write(f"{subdomain}.sibervatan.org\n")
    
    print(f"\033[92m[*] SecurityTrails: Subdomain scan successful.\033[1m")