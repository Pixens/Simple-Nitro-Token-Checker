import httpx, os, threading
from colorama import Fore
os.system("")

url = 'https://discord.com/api/v9/users/@me'
tokens = open('tokens.txt', 'r').read().splitlines()

class data:
    nitro = 0; normal = 0

def checkToken(token):
    try:
        resp = httpx.get(url, headers = {'Authorization': token})
        if resp.status_code == 200:
            if resp.json()['premium_type'] == 2:
                print(f"{Fore.GREEN}[+] Nitro: {token} | username = {resp.json()['username']}#{resp.json()['discriminator']}")
                data.nitro += 1
                open('nitro-tokens.txt', 'a').write(token + '\n')
            elif resp.json()['premium_type'] == 0:
                print(f"{Fore.RED}[-] Normal: {token} | username = {resp.json()['username']}#{resp.json()['discriminator']}")
                data.normal += 1
                open('normal-tokens.txt', 'a').write(token + '\n')
        elif resp.status_code == 401:
            print(f"{Fore.RED}[!] Invalid: {token} | username = N/A")
        else:
            print(f"{Fore.RED}[!] Locked: {token} | username = N/A")
    except Exception as e:
        checkToken(token)
        
threads = []
for fulltoken in tokens:
    token = fulltoken.split(':')[-1]
    t = threading.Thread(target = checkToken, args = [token,])
    threads.append(t)
    
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()
    
print()
print(f'Nitro Tokens: {data.nitro}')
print(f'Normal Tokens: {data.normal}')