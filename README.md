# Automated External Attack Surface Discovery Suite

A modular Python-based reconnaissance pipeline designed to automate the initial phases of VAPT (Vulnerability Assessment and Penetration Testing).

Link Medium : https://medium.com/p/58d2382a82b9?postPublishedType=initial

## Features
- **Passive Recon**: Enumerating subdomains via Certificate Transparency (CT) logs.
- **Service Probing**: Validating live targets and identifying HTTP status codes.
- **Visual Recon**: Automated headless browser screenshots of all live services.

## Tech Stack
- Python 3.x
- Playwright (Headless Browser)
- HackerTarget API

## How to Run
1. Install dependencies: `pip install requests colorama playwright`
2. Run Recon: `python sub_hunter.py`
3. Run Prober: `python prober.py`
4. Run Screenshotter: `python screenshotter.py`
