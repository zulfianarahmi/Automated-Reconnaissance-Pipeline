import requests
from colorama import Fore, Style, init

init(autoreset=True)

def probe_subdomains(input_file):
    print(Fore.CYAN + f"[*] Memulai probing dari file: {input_file}")
    
    with open(input_file, 'r') as f:
        subdomains = f.read().splitlines()

    live_subdomains = []

    for sub in subdomains:
        url = f"http://{sub}"
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            status = response.status_code
            
            if status == 200:
                color = Fore.GREEN
            elif status in [401, 403]:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE
                
            print(f"{color}[{status}] {url}")
            live_subdomains.append(f"[{status}] {url}")
            
        except requests.exceptions.RequestException:
            pass

    with open("live_targets.txt", "w") as f:
        for item in live_subdomains:
            f.write(item + "\n")

    print(Fore.CYAN + "\n[*] Scanning selesai. Hasil target hidup disimpan di: live_targets.txt")

if __name__ == "__main__":
    probe_subdomains("subdomains_xxxxxxx.txt")
