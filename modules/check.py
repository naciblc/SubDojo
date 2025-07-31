import os
import glob
import requests
import dns.resolver
import urllib3
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

date = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")


# DNS çözümleme
def dns_record_check(subdomain):
    resolvers_path = os.path.join(os.getcwd(), "resolvers.txt")
    with open(resolvers_path, "r") as f:
        adress_resolvers = [line.strip() for line in f if line.strip()]
    
    resolver = dns.resolver.Resolver()
    resolver.nameservers = adress_resolvers
    record_types = ["A", "AAAA", "CNAME"]

    for record in record_types:
        try:
            answers = resolver.resolve(subdomain, record)
            if answers:
                return True
        except Exception as e:
            continue

    return False


# HTTP + DNS canlılık kontrolü
def check_subdomains(subdomain):

    if not dns_record_check(subdomain):
        return None

    protocols = ["https://", "http://"]
    for protocol in protocols:
        url = protocol + subdomain
        try:
            
            response = requests.get(url, timeout=30, verify=False)
            if response.status_code < 600:
                
                return url
        except Exception as e:
            continue

    
    return "dns-only://" + subdomain


# Redirect analizi
def request_run(link):
    try:
        resp = requests.get(link, allow_redirects=False, timeout=30, verify=False)
        status = resp.status_code

        if 300 <= status < 400:
            location = resp.headers.get("Location", "")
            redirect_url = urljoin(link, location)
            
            return {
                "original": link,
                "status": status,
                "redirects_to": redirect_url
            }
        elif status < 600:
            
            return {
                "original": link,
                "status": status,
                "redirects_to": None
            }
    except Exception as e:
        
        return {
            "original": link,
            "status": None,
            "redirects_to": None,
            "error": str(e)
        }


# Tüm subdomain'leri kontrol et
def total_subs(domain):
    print(f"[~] Subdomain DNS + Http + Redirect Control")
    out_path = os.path.join("output", "subdomain", domain, "live_subdomains")
    os.makedirs(out_path, exist_ok=True)
    output_file = os.path.join(out_path, f"Live-{domain}-{date}.txt")

    subdomains = set()
    sub_files = glob.glob(os.path.join("output", "subdomain", domain, "*.txt"))
    for file in sub_files:
        with open(file, "r") as f:
            for line in f:
                clean = line.strip()
                if clean:
                    subdomains.add(clean)

    print(f"[~] Total {len(subdomains)} subdomains found.")
    live_subs = set()
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(check_subdomains, sub) for sub in subdomains ]
        for future in as_completed(futures):
            result = future.result()
            if result:
                live_subs.add(result)

    with open(output_file, "w") as f:
        for item in live_subs:
            f.write(f"{item}\n")

    print(f"[✓] {len(live_subs)} live subdomains saved → {output_file}")
    return True


#  Redirect analizi
def run_httpx(domain):
    input_file = os.path.join("output", "subdomain", domain, "live_subdomains", f"Live-{domain}-{date}.txt")
    
    if not os.path.exists(input_file):
        return False

    with open(input_file, "r") as f:
        subdomains = [line.strip() for line in f if line.strip()]

    results = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(request_run, link) for link in subdomains if not link.startswith("dns-only://")]
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)
                
    # dns-only olanları da results listesine ekle
    dns_only_count = 0
    for link in subdomains:
        if link.startswith("dns-only://"):
            dns_only_count += 1
            results.append({
                "original": link,
                "status": None,
                "redirects_to": None,
                "error": "Http/Https"
            })


    with open(input_file, "w") as f:
        for res in results:
            if res["redirects_to"]:
                line = f'{res["original"]} → {res["redirects_to"]} (Status: {res["status"]})\n'
            elif res["status"]:
                line = f'{res["original"]} (Status: {res["status"]})\n'
            else:
                line = f'{res["original"]} (Error: {res["error"]})\n'
            f.write(line)
    print(f"[i] Number of subdomains marked as DNS only: {dns_only_count}")
    return True

