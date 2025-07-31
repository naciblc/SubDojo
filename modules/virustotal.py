import requests
import yaml
import os
from modules.hacker_target import date

def virustotal(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"Virustotal-{domain}-{date}.txt")
    with open("config.yaml","r")as f:
        api_key = yaml.safe_load(f)

    response = requests.get(f"https://www.virustotal.com/vtapi/v2/domain/report?apikey={api_key['virustotal']['api_key']}&domain={domain}")
    op = response.json()
    for subdomain in op['subdomains']:
        with open (of,"a") as f:
            f.write(f"{subdomain}\n")
    print(f"\033[92m[*] VirusTotal: Subdomain scan successful.\033[1m")
