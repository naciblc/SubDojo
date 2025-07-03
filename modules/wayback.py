import os
import requests
from datetime import datetime
import time

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

def waybackurls(domain):
    data = None
    of = os.path.join("output","subdomain",f"{domain}",f"Wayback-{domain}-{date}.txt")
    for attempt in range(3):
        try:
            response = requests.get(f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&collapse=urlkey")
            response.raise_for_status()
            data = response.json()
            break
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
    if data is None:
        print("[!] Failed to retrieve data from web.archive.org after 3 attempts.")
        return    

    urls = [i[0] for i in data[1:]]
    urls : list[str]
    subdomains = set()
    for u in urls:
        try:
            sub = u.split("/")[2]
            if sub.endswith(domain):
                subdomains.add(sub)
        except IndexError:
            pass
    with open(of,"a") as f:
        for i in subdomains:
            f.writelines(f"{i}\n")

    print(f"\033[92m[*] Waybackurls: Subdomain scan successful.\033[1m")