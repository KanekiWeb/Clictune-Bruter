import os, requests, threading, random, urllib.parse
from colorama import Fore, init

init()

# Credit to Pycenter by billythegoat356
# Github: https://github.com/billythegoat356/pycenter/
# License: https://github.com/billythegoat356/pycenter/blob/main/LICENSE

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class Console:
    def banner(self):
        os.system('cls && title [Clictune Bruter v1] - Made By Kaneki Web#9999' if os.name == "nt" else 'clear')
        
        print(center("""

 ██████╗████████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██║        ██║       ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝
██║        ██║       ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗
╚██████╗   ██║       ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║  ██║
 ╚═════╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                       
""").replace("█", Fore.RED+"█"+Fore.RESET))
        
        print(center("[ discord.gg/kaneki ~ github.com/KanekiWeb ]").replace("[", Fore.RED+"["+Fore.RESET).replace("~", Fore.RED+"~"+Fore.RESET).replace("]", Fore.RED+"]"+Fore.RESET) + "\n\n\n")
        
    def printer(self, code, invalid, valid, lock=threading.Lock()):
        lock.acquire()
        print(f" Code: {Fore.YELLOW}{code}{Fore.RESET}  |  Invalid: {Fore.RED}{invalid}{Fore.RESET}  |  Valid: {Fore.GREEN}{valid}{Fore.RESET}", end="\r")
        lock.release()

class Clictune(threading.Thread):
    def __init__(self) -> None:
        self.valid = 0
        self.invalid = 0
        
    def run(self):
        self.code = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(4))
        headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0","Referer":"https://ghostbin.com/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/x-www-form-urlencoded"}
        req = requests.get("https://www.clictune.com/" + self.code, headers=headers)
        
        if '<div style="text-align:center;">The link has been removed <br/> <a href=https://www.clictune.com/>Go to Home</a></div>' in req.text:
            self.invalid += 1
        
        else:
            redirect = req.text.split('https://www.mylink1.biz/link/redirect/?url=')[1].split('">')[0]
            self.valid += 1
            open('hits.txt', 'a+').write(urllib.parse.unquote(redirect) +"\n")
        
        Console().printer(self.code, self.invalid, self.valid)
            
        

if __name__ == "__main__":
    Console().banner()
    Worker = Clictune()
    while True:
        threading.Thread(target=Worker.run()).start()