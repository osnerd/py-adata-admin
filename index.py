import colorama
import requests
import os
import json
import webbrowser

colorama.init(autoreset=True)

deployment = ""
adminkey = ""

def print_ascii():
    ascii_art = """
 █████╗ ██████╗  █████╗ ████████╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
███████║██║  ██║███████║   ██║   ███████║
██╔══██║██║  ██║██╔══██║   ██║   ██╔══██║
██║  ██║██████╔╝██║  ██║   ██║   ██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

          https://adata.one
    """
    os.system("cls")
    print(colorama.Fore.CYAN + ascii_art)

def print_response(response):
    try:
        print(colorama.Fore.LIGHTWHITE_EX + json.dumps(response.json(), indent=4))
    except:
        print(colorama.Fore.RED + "Error parsing response!")

def create_keys(amount, days):
    url = f"https://{deployment}/admin/createkeys"
    payload = {"key": adminkey, "amount": amount, "days": days}
    response = requests.post(url, json=payload)
    print_ascii()
    print_response(response)

def reset_db():
    url = f"https://{deployment}/admin/resetdb"
    payload = {"key": adminkey}
    response = requests.post(url, json=payload)
    print_ascii()
    print_response(response)

def create_user(username, password, key):
    url = f"https://{deployment}/user/create"
    payload = {"username": username, "password": password, "key": key}
    response = requests.post(url, json=payload)
    print_ascii()
    print_response(response)

def login_user(username, password):
    url = f"https://{deployment}/user/login"
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload)
    print_ascii()
    print_response(response)

def check_status(token):
    url = f"https://{deployment}/user/status"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print_ascii()
    print_response(response)

def open_docs():
    docs_url = "https://docs.adata.one"
    webbrowser.open(docs_url)
    print(colorama.Fore.GREEN + f"Opening documentation: {docs_url}")

def login():
    global adminkey
    global deployment
    print_ascii()
    dp = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Deployment Name: ").strip()
    ak = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Admin Key: ").strip()
    deployment = f"{dp}.vercel.app"
    adminkey = ak
    os.system("cls")

def main_menu():
    while True:
        print_ascii()
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}1{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Create Keys")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}2{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Reset Database")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}3{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Create User")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}4{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Login User")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}5{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Check User Status")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}6{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Open Docs")
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}0{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Exit")
        print("\n" + colorama.Fore.LIGHTBLACK_EX + "-" * 40)
        choice = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Select an option: ").strip()

        if choice == "1":
            days = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} How Long (Days): ").strip()
            amount = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Amount: ").strip()
            create_keys(int(amount), int(days))
        elif choice == "2":
            reset_db()
        elif choice == "3":
            username = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Username: ").strip()
            password = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Password: ").strip()
            key = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Key: ").strip()
            create_user(username, password, key)
        elif choice == "4":
            username = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Username: ").strip()
            password = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Password: ").strip()
            login_user(username, password)
        elif choice == "5":
            token = input(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RESET}?{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.RESET} Token: ").strip()
            check_status(token)
        elif choice == "6":
            open_docs()
        elif choice == "0":
            print(colorama.Fore.GREEN + "Exiting... Goodbye!")
            break
        else:
            print(colorama.Fore.RED + "Invalid option! Please try again.")
        input(colorama.Fore.LIGHTBLACK_EX + "\nPress Enter to return to the menu...")

if __name__ == "__main__":
    login()
    main_menu()
