import os
import base64
import signal

def search(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if path.endswith(".xml"):
                with open(path, "r", encoding="UTF-8", errors='replace') as file:
                    lines = file.readlines()
                    data = []
                    Hosts = [""]
                    Port = [""]
                    User = [""]
                    Pass = [""]
                    for line in lines:
                        if any(tag in line for tag in ["Host", "Port", "User", "Pass"]):
                            line = line.replace('\t', '').replace(' ', '')
                            line = line.replace("<Host>", "").replace('</Host>', ' Host')
                            line = line.replace("<Port>", "").replace('</Port>', ' Port')
                            line = line.replace("<User>", "").replace('</User>', ' User')
                            line = line.replace('<Passencoding="', " ").replace('<Pass>', '').replace("</Pass>", " Pass")
                            line = line.rstrip().replace('">', '').replace('plaintextPassword', '').replace(' crypt"pubkey="', '')
                            data.append(line)

                    for item in data:
                        if item.find("Host") >= 1:
                            Hosts.append(item.replace(" Host", ""))
                        elif item.find("Port") >= 1:
                            Port.append(item.replace(" Port", ""))
                        elif item.find("User") >= 1:
                            User.append(item.replace(" User", ""))
                        elif item.find("Pass") >= 1:
                            Pass.append(item.replace(" Pass", ""))
                            if key == 1:
                                print(f"\033[94m{Hosts[-1].rstrip()}:{Port[-1].rstrip()}:{User[-1].rstrip()}:{Pass[-1].replace(' base64','')}")
                            elif key == 2:
                                if 'base64' in item:
                                    decoded_pass = base64.b64decode(Pass[-1].replace(' base64', ''), altchars=None).decode('UTF-8', errors='replace')
                                    print(f"\033[94m{Hosts[-1]}:{Port[-1]}:{User[-1]}:{decoded_pass}")
                                else:
                                    print(f"\033[94m{Hosts[-1]}:{Port[-1]}:{User[-1]}:{Pass[-1]}")

def menu():
    banner = """
###################################                                  
#        -- XML Parser --         #  
#  [Code By :: Sicario ᕦ(ò_óˇ)ᕤ] #  
##################################    


\033[91m1. Collect HOST:USER:PASS
2. Collect HOST:USER:PASS and decode passwords from base64
\033[0m    """

    print(banner)

    def signal_handler(signal, frame):
        print('\n\033[1mExiting...\033[0m')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    inpt = input("Enter your choice: ")
    if inpt == "1":
        key = 1
        directory = input("Enter the directory path: ").replace('"', '')
        search(directory, key)
    elif inpt == "2":
        key = 2
        directory = input("Enter the directory path: ").replace('"', '')
        search(directory, key)

menu()
