import asyncio
import os
from playwright.async_api import async_playwright
from colorama import Fore, init

init(autoreset=True)

async def take_screenshots(input_file):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    print(Fore.CYAN + f"[*] Membaca target dari {input_file}...")
    
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
        targets = [line.split("] ")[1] for line in lines if "] " in line]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        print(Fore.YELLOW + f"[*] Memulai pengambilan gambar untuk {len(targets)} target...")

        for url in targets:
            filename = url.replace("http://", "").replace("https://", "").replace("/", "_") + ".png"
            filepath = os.path.join("screenshots", filename)
            
            print(Fore.WHITE + f"[>] Processing: {url}")
            try:
                await page.goto(url, timeout=30000, wait_until="networkidle")
                await page.screenshot(path=filepath)
                print(Fore.GREEN + f"  [+] Saved: {filepath}")
            except Exception as e:
                print(Fore.RED + f"  [-] Failed {url}: {str(e)}")

        await browser.close()

    print(Fore.CYAN + "\n[*] Selesai! Cek folder 'screenshots' kamu.")

if __name__ == "__main__":
    asyncio.run(take_screenshots("live_targets.txt"))
