import os
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests
import glob
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from datetime import datetime

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

def total_subs(domain):
    of = os.path.join("output","subdomain",f"{domain}","live_subdomains",f"Live-{domain}-{date}.txt")
    subdomains = set()
    subdomain_txtname = glob.glob(os.path.join("output","subdomain",f"{domain}","*.txt"))
    for file in subdomain_txtname:
        with open(file,"r") as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    subdomains.add(clean_line)
    live_on = set()
    with ThreadPoolExecutor(max_workers=30) as thred:
        lives = [thred.submit(check_subdomains,sub)for sub in subdomains]
        for live in as_completed(lives):
            result = live.result()
            if result:
                live_on.add(result)
    with open(of,"w")as f:
        for i in live_on:
            f.write(f"{i}\n")
    return True

def check_subdomains(subdomain):
    protocols = ["https://","http://"]

    for protocol in protocols:
        url = protocol + subdomain
        try:
            response = requests.get(url,timeout=10,verify=False)
            if response.status_code < 600:
                return url
        except:
            continue
    return None

#Redirect check
def request_run(domain,link):
        try:
            response = requests.get(link,allow_redirects=False,timeout=10)
            if 300 < response.status_code < 400:
                location = response.headers.get("Location",'')
                if domain not in location:
                    return link
                else:
                    pass
            elif response.status_code < 600:
                return link
        except Exception as e:
            return None
#Redirect check
def run_httpx(domain):
    path = os.getcwd()
    of = os.path.join("output","subdomain",f"{domain}","live_subdomains",f"Live-{domain}-{date}.txt")
    with open(of,"r")as f:
        subdomains = f.readlines()

    subdomains_list = []
    with ThreadPoolExecutor(max_workers=30) as thred:
        futures = [thred.submit(request_run,domain,link.strip()) for link in subdomains]

        for future in as_completed(futures):
            result = future.result()
            if result:
                subdomains_list.append(result)
    with open(of,"w")as f:
        for i in subdomains_list:
            f.write(f"{i}\n")
    print(f"Live Subdomain List saved at: {path}{of}")
    return True