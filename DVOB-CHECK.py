import urllib.request
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

def print_header():
    custom_fig = Figlet(font='slant', width=120)
    dvob_check_art = custom_fig.renderText("DVOB-CHECK")
    print(Fore.CYAN + Style.BRIGHT + dvob_check_art + Style.RESET_ALL)
    print(Fore.MAGENTA + "Don't forget to follow my Instagram account ahu_orphan")

def check_url_safety(url):
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        if soup.find_all("iframe"):
            print(Fore.RED + "This website contains iframes which may indicate malicious content.")
        else:
            print(Fore.GREEN + "This website does not contain iframes.")

        if soup.find_all("script"):
            print(Fore.RED + "This website contains scripts which may indicate malicious content.")
        else:
            print(Fore.GREEN + "This website does not contain scripts.")

        if soup.find_all("a"):
            print(Fore.RED + "This website contains hyperlinks which may lead to malicious websites.")
        else:
            print(Fore.GREEN + "This website does not contain hyperlinks.")
    except Exception as e:
        print(Fore.RED + "An error occurred while checking the URL:", e)

if __name__ == "__main__":
    print_header()
    url_to_check = input("Enter the URL to check: ")
    check_url_safety(url_to_check)
