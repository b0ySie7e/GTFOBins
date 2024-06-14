import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore, Style, init

def search_gtfobins(binary_name, section_filter):
    url = f"https://gtfobins.github.io/gtfobins/{binary_name}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        sections = soup.find_all(['h2', 'h3', 'p', 'pre'])
        if not sections:
            print(f"No detailed sections found for binary '{binary_name}' on GTFOBins.")
            return

        print(f"{Fore.CYAN}Information for binary '{binary_name}' from GTFOBins:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
        
        current_section = None
        section_data = []

        for section in sections:
            if section.name in ['h2', 'h3']:
                current_section = section.get_text().strip()
                section_data.append((current_section, ""))
            elif section.name == 'p':
                if section_data and section_data[-1][1] == "":
                    section_data[-1] = (section_data[-1][0], section.get_text().strip())
            elif section.name == 'pre':
                if section_data:
                    section_data[-1] = (section_data[-1][0], section_data[-1][1] + f"\n{section.get_text().strip()}\n{'-' * len(section.get_text().strip())}")

        for title, content in section_data:
            if section_filter and section_filter.lower() not in title.lower():
                continue
            print(f"\n{Fore.YELLOW}{title}{Style.RESET_ALL}\n{Fore.YELLOW}{'-' * len(title)}{Style.RESET_ALL}")
            print(content)
    else:
        print(f"Binary '{binary_name}' not found on GTFOBins or there was an error retrieving the page.")

if __name__ == "__main__":
    init(autoreset=True)
    
    parser = argparse.ArgumentParser(
        description="Fetch and display GTFOBins information for a given binary.",
        epilog="Example: python3 GTFOBins.py -b awk -s SUID"
    )
    parser.add_argument(
        '-b', '--binary', 
        type=str, 
        required=True, 
        help="Name of the binary to search for on GTFOBins."
    )
    parser.add_argument(
        '-s', '--section',
        type=str,
        help="Specific section to filter the output (e.g., SUID, Sudo)."
    )
    args = parser.parse_args()

    search_gtfobins(args.binary, args.section)
