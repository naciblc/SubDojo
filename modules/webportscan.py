import os
import glob
from urllib.parse import urlparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
from tqdm import tqdm
from datetime import datetime
from modules.check import date

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def filededect(domain, ap=False):

    print("[*] Starting web port scanning")
    print("[!] All Ports Mode:", ap)

    main = os.getcwd()
    of = glob.glob(os.path.join(f"{main}/output/subdomain/{domain}/live_subdomains/*"))
    subdomains = set()
    oafsd = os.path.join(f"{main}/output/subdomain/{domain}/live_subdomains/live-{domain}-{date}-nonstandard-ports.txt")
    for file in of:
        with open(file, "r") as f:
            subdomain_file = f.readlines()

    a = 0
    for subdomain in subdomain_file:
        if subdomain.startswith("dns-only"):
            subdomains.add(subdomain.split("//")[1].split("(")[0].strip())
        elif "→" in subdomain:
            subdomains.add(subdomain.split("→")[0].split("//")[1].strip())
            parsed_url = urlparse(subdomain.split("→")[1].split("(")[0].strip())
            hostnam = parsed_url.hostname
            subdomains.add(hostnam)
        elif "→" not in subdomain and "DNS only" not in subdomain:
            subdomains.add(subdomain.split("//")[1].split("(")[0].strip())

    if ap:
        port = 93
    else:
        port = 49

    total = len(subdomains) * port
    with tqdm(
        total=total,
        desc="Port Scanning",
        dynamic_ncols=True,
        leave=False,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} • Elapsed: {elapsed} • Remaining: {remaining} • Speed: {rate_fmt}",
        colour="green"
    ) as pbar:
        # Send parsed domains to port scan
        sonuc = []
        with ThreadPoolExecutor(max_workers=500) as sub:
            futures = [sub.submit(portscan, subdom, ap, pbar) for subdom in subdomains]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    sonuc.append(result)

        with open(oafsd, "a") as f:
            for line in sonuc:
                f.writelines(f"{line}\n")

        print("\033[1;32m[✓] Scanning completed\033[0m")


def portscan(subdomain, ap=False, pbar=None):
    protocols = ["https://", "http://"]

    frequently_used_ports = [
        81,591,3000,2082, 2087, 2095, 2096,3001,3002, 3128, 4243, 5000, 5001, 5601, 7000, 7001, 7002, 7474, 8000, 8001,
        8008, 8009, 8069, 8080, 8081,8083, 8088, 8090, 8091, 8118, 8180, 8280, 8281,
        8443, 8500, 8880, 8888, 8983, 9000, 9080, 9090, 9091, 9200, 9443, 10000,
        10250, 10255, 10443, 15672
    ]

    less_frequently_used_ports = [
        300,  593, 832, 981, 1010, 1311, 2480, 3333,
        4567, 4711, 4712, 4993, 5104, 5108, 5800, 5801, 5805, 6080, 6543, 6789,
        7396, 8014, 8042, 8123, 8172, 8222, 8243, 8333, 8834, 9043, 9060, 9191,
        9393, 9444, 9800, 9981, 12443, 16080, 18091, 18092, 20720, 21098, 28017,
        32768, 32775, 33389, 4443
    ]

    if ap:
        frequently_used_ports += less_frequently_used_ports

    results = []

    for port in frequently_used_ports:
        found = False
        for protocol in protocols:
            url = f"{protocol}{subdomain}:{port}"
            try:
                response = requests.get(url, timeout=10, verify=False)
                if response.status_code < 600:
                    results.append(f"{url} (Status: {response.status_code})")
                    found = True
                    break  # If either HTTPS or HTTP works, skip the other
            except Exception:
                pass
        if pbar:
            pbar.update(1)  # Update after each port attempt
        if found:
            continue  # Skip the second protocol if one already responded

    return results if results else None

