import json
import colorama
from colorama import Fore
import requests
print(f"""

                    {Fore.RED}▄████▄  {Fore.GREEN} ██▀███  {Fore.BLUE} ▄▄▄      {Fore.YELLOW}  ▄████ {Fore.BLUE} ██░ ██ {Fore.GREEN} ▄▄▄      {Fore.RED} ▄████▄  {Fore.YELLOW} ██ ▄█▀
                    {Fore.RED}▒██▀ ▀█ {Fore.GREEN} ▓██ ▒ ██{Fore.BLUE}▒▒████▄   {Fore.YELLOW}  ██▒ ▀█{Fore.BLUE}▒▓██░ ██{Fore.GREEN}▒▒████▄   {Fore.RED} ▒██▀ ▀█ {Fore.YELLOW}  ██▄█▒ 
                    {Fore.RED}▒▓█     {Fore.GREEN} ▓██ ░▄█ {Fore.BLUE}▒▒██  ▀█▄ {Fore.YELLOW} ▒██░▄▄▄{Fore.BLUE}░▒██▀▀██{Fore.GREEN}░▒██  ▀█▄ {Fore.RED} ▒▓█    ▄{Fore.YELLOW} ▓███▄░ 
                    {Fore.RED}▒▓▓▄ ▄▄{Fore.GREEN}▒▒██▀▀█▄ {Fore.BLUE} ░██▄▄▄▄██{Fore.YELLOW} ░▓█  ██{Fore.BLUE}▓░▓█ ░██{Fore.GREEN} ░██▄▄▄▄██{Fore.RED} ▒▓▓▄ ▄██{Fore.YELLOW}▒▓██ █▄ 
                    {Fore.RED}▒ ▓███▀ {Fore.GREEN}░░██▓ ▒██{Fore.BLUE}▒ ▓█   ▓██{Fore.YELLOW}▒░▒▓███▀{Fore.BLUE}▒░▓█▒░██{Fore.GREEN}▓ ▓█   ▓██{Fore.RED}▒▒ ▓███▀ {Fore.YELLOW}░▒██▒ █▄
                    {Fore.RED}░ ░▒ ▒  {Fore.GREEN}░░ ▒▓ ░▒▓{Fore.BLUE}░ ▒▒   ▓▒█{Fore.YELLOW}░ ░▒   ▒{Fore.BLUE}  ▒ ░░▒░▒ {Fore.GREEN}▒▒   ▓▒█{Fore.RED}░░ ░▒ ▒  {Fore.YELLOW}░▒ ▒▒ ▓▒
                    {Fore.RED}░  ▒    {Fore.GREEN} ░▒ ░ ▒░ {Fore.BLUE} ▒   ▒▒ ░ {Fore.YELLOW} ░   ░  {Fore.BLUE}▒ ░▒░ ░  ▒{Fore.GREEN}   ▒▒ ░ {Fore.RED} ░  ▒   ░{Fore.YELLOW} ░▒ ▒░
                    {Fore.RED}░       {Fore.GREEN}   ░░   ░{Fore.BLUE}   ░   ▒  {Fore.YELLOW} ░ ░   ░{Fore.BLUE}  ░  ░░ ░{Fore.GREEN}  ░   ▒  {Fore.RED} ░       {Fore.YELLOW} ░ ░░ ░ 
                   {Fore.RED} ░ ░     {Fore.GREEN}    ░    {Fore.BLUE}       ░  {Fore.YELLOW}░      ░{Fore.BLUE}  ░  ░  ░{Fore.GREEN}      ░  {Fore.RED}░░ ░     {Fore.YELLOW}░  ░   
                    {Fore.RED}░       {Fore.GREEN}
                                                            
                          {Fore.RED}A{Fore.GREEN}u{Fore.BLUE}t{Fore.YELLOW}h{Fore.RED}o{Fore.GREEN}r{Fore.BLUE}: {Fore.YELLOW}K{Fore.RED}a{Fore.GREEN}y{Fore.BLUE}y{Fore.YELLOW}z{Fore.RED}#{Fore.GREEN}4{Fore.BLUE}4{Fore.YELLOW}6{Fore.RED}6
                                                                     
""")
ip = input("deine ip: ")
antwort = requests.get("https://ipinfo.io/{}".format(ip))
data = antwort.json()
print(data["ip"])
print(data["city"])
print(data["country"])
print(data["region"])
print(data["org"])
print("Coded by Kayyz")
