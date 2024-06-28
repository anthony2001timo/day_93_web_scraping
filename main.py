import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
result = requests.get(website)
content = result.text

pattern = r"/etry/[/w-]*"
repeated_machine = re.findall(pattern,str(content))
without_repeated = list(set(repeated_machine))

final_machine = []

for i in without_repeated:
    machine_name = i.replace("/entry/", "")
    final_machine.append(machine_name)
    print(machine_name)

########################

noob_machine = "noob-1"
noob_exist = False

for a in final_machine:
    if a == noob_machine:
        noob_exist = True
        break

cyan_color = Fore.CYAN
yellow_color = Fore.YELLOW

if noob_exist == True:
    print(cyan_color + "There is  not any new machine")
else:
    print(yellow_color + "new machine")