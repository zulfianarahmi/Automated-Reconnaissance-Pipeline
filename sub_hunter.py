import requests
from colorama import Fore, Style, init

init(autoreset=True)

class SubHunter:
    def __init__(self, domain):
        self.domain = domain
        self.api_url = f"https://api.hackertarget.com/hostsearch/?q={self.domain}"
        self.found_subdomains = set()

    def banner(self):
        print(Fore.CYAN + Style.BRIGHT + "=" * 45)
        print(Fore.WHITE + Style.BRIGHT + "   SUBDOMAIN HUNTER - RECON EDITION")
        print(Fore.CYAN + Style.BRIGHT + "=" * 45)
        print(Fore.YELLOW + f"Target Domain : {self.domain}\n")

    def scan(self):
        self.banner()
        print(Fore.WHITE + "[*] Menarik data dari HackerTarget API...")

        try:
            response = requests.get(self.api_url, timeout=15)

            if response.status_code != 200:
                print(Fore.RED + f"[!] API Error: {response.status_code}")
                return

            lines = response.text.splitlines()

            for line in lines:
                if "," in line:
                    subdomain = line.split(",")[0].lower()
                    if self.domain in subdomain:
                        self.found_subdomains.add(subdomain)

            self.display_results()

        except requests.exceptions.Timeout:
            print(Fore.RED + "[!] Timeout: koneksi terlalu lama / server sibuk.")
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "[!] Koneksi gagal. Cek internet atau DNS.")
        except Exception as e:
            print(Fore.RED + f"[!] Error tak terduga: {e}")

    def display_results(self):
        sorted_subs = sorted(self.found_subdomains)

        if not sorted_subs:
            print(Fore.RED + "[-] Tidak ada subdomain ditemukan.")
            return

        print(Fore.GREEN + f"[+] Ditemukan {len(sorted_subs)} subdomain:\n")
        for sub in sorted_subs:
            print(Fore.WHITE + f" - {sub}")

        filename = f"subdomains_{self.domain.replace('.', '_')}.txt"
        with open(filename, "w") as f:
            for sub in sorted_subs:
                f.write(sub + "\n")

        print(Fore.YELLOW + f"\n[*] Hasil disimpan ke file: {filename}")

if __name__ == "__main__":
    target = input("Masukkan Domain (contoh: baliprov.go.id): ").strip()

    if not target:
        print(Fore.RED + "Target tidak boleh kosong!")
    else:
        hunter = SubHunter(target)
        hunter.scan()
