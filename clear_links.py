import requests, re
print(""" \033[1;34;40m
  █████████  █████       ██████████   █████████   ██████   █████           █████       █████ ██████   █████ █████   ████  █████████ 
  ███░░░░░███░░███       ░░███░░░░░█  ███░░░░░███ ░░██████ ░░███           ░░███       ░░███ ░░██████ ░░███ ░░███   ███░  ███░░░░░███ \033[1;33;40m @nouredine_kn \033[1;34;40m
 ███     ░░░  ░███        ░███  █ ░  ░███    ░███  ░███░███ ░███            ░███        ░███  ░███░███ ░███  ░███  ███   ░███    ░░░   \033[1;33;40mt.me/nkcp_tm \033[1;34;40m
░███          ░███        ░██████    ░███████████  ░███░░███░███            ░███        ░███  ░███░░███░███  ░███████    ░░█████████  \033[1;33;40m DEV---> NOUREDINE KAOINE \033[1;34;40m
░███          ░███        ░███░░█    ░███░░░░░███  ░███ ░░██████            ░███        ░███  ░███ ░░██████  ░███░░███    ░░░░░░░░███   \033[1;33;40m </> PYTHON\033[1;34;40m
░░███     ███ ░███      █ ░███ ░   █ ░███    ░███  ░███  ░░█████            ░███      █ ░███  ░███  ░░█████  ░███ ░░███   ███    ░███
 ░░█████████  ███████████ ██████████ █████   █████ █████  ░░█████ █████████ ███████████ █████ █████  ░░█████ █████ ░░████░░█████████ 
  ░░░░░░░░░  ░░░░░░░░░░░ ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░ ░░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░   ░░░░  ░░░░░░░░░  
\033[1;35;40m
  """)
w = "url.txt"
url = open(w, "r").read().splitlines()
o = open("urls_clinks.txt", "w")
for line in url:
    url2 = line.split("//")[1]
    url3 = "www." + url2.split("/")[0] + "\n"
    print("------->" + url3 + "\033[1;32;40mDONE\n")
    o.write(url3)


