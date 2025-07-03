import requests
import os
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

def hacker_target(domain):
    of = os.path.join("output","subdomain",f"{domain}",f"HackerTarget-{domain}-{date}.txt")
    response = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")
    a = response.text
    asd = a.split("\n")
    subdomains = set()
    for i in asd:
        if domain in i:
            a = i.split(",")
            subdomains.add(a[0])
    with open(of,"a") as f:
        for sub in subdomains:
            f.write(f"{sub}\n")
    print(f"\033[92m[*] Hackertarget: Subdomain scan successful.\033[1m")