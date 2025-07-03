from colorama import Fore, Style, init
import pyfiglet
import threading
import argparse
import os
from modules.command import run_subfinder, run_amass, run_assetfinder
from modules.crtsh import crt_sh
from modules.wayback import waybackurls
from modules.hacker_target import hacker_target
from modules.check import total_subs, run_httpx



def main():
    banner = pyfiglet.figlet_format("SubDojo")
    print(Fore.MAGENTA + Style.BRIGHT + banner)

    parse = argparse.ArgumentParser(description="SubDojo Recon Tools")
    parse.add_argument("-d", "--domain", required=True, help="Target Domain")
    args = parse.parse_args()
    domain = args.domain

    base_path = os.getcwd()
    output = os.path.join(base_path, f"output/subdomain/{domain}")
    os.makedirs(output, exist_ok=True)

    print(f"[*] Target domain: {domain}")

    threadings = []
    threadings.append(threading.Thread(target=run_subfinder, args=(domain,)))
    threadings.append(threading.Thread(target=run_amass, args=(domain,)))
    threadings.append(threading.Thread(target=run_assetfinder, args=(domain,)))
    threadings.append(threading.Thread(target=waybackurls, args=(domain,)))
    threadings.append(threading.Thread(target=crt_sh, args=(domain,)))
    threadings.append(threading.Thread(target=hacker_target, args=(domain,)))

    for t in threadings:
        t.start()
    for t in threadings:
        t.join()

    live_output = os.path.join(base_path, f"output/subdomain/{domain}/live_subdomains")
    os.makedirs(live_output, exist_ok=True)

    total_subs(domain)
    run_httpx(domain)

if __name__ == "__main__":
    main()
