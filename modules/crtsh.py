import os
import json
import requests
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

def crt_sh(domain):
    output_dir = os.path.join("output", "subdomain", domain)
    os.makedirs(output_dir, exist_ok=True)
    of = os.path.join(output_dir, f"Crt.sh-{domain}-{date}.txt")

    url = f"https://crt.sh/?q={domain}&output=json"
    headers = {"User-Agent": "Mozilla/5.0"}

    data = None

    for _ in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    break
                except json.decoder.JSONDecodeError:
                    return None 
        except:
            pass  

    if data is None:
        print("[!] Failed to retrieve data from crt.sh after 3 attempts.")
        return None

    subdomains = set()
    for entry in data:
        if 'name_value' in entry:
            sub = entry['name_value']
            for i in sub.split("\n"):
                if "*" not in i and i.endswith(domain):
                    subdomains.add(i)

    with open(of, "w") as f:
        for sub in sorted(subdomains):
            f.write(sub + "\n")

    print(f"\033[92m[*] Crt.sh: Subdomain scan successful.\033[1m")
    return None