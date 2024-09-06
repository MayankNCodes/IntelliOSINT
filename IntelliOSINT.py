import IntelliLib
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
###################################################################################
askPasswordBeforeLogin = False #YOU WANT TO SET PASSWORD FOR LOGIN (True/False)   #
loginPassword = "123" #SET YOUR PASSWORD HERE                                     #
###################################################################################

spacer = "       "
s = "------------------------------------------------------------------------------------------------------------"
banner = """
  ______    ______    ______   ______   ______   __               ______    ______   ______  __    __  ________ 
 /      \  /      \  /      \ /      | /      \ /  |             /      \  /      \ /      |/  \  /  |/        |
/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$/ /$$$$$$  |$$ |            /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/ 
$$ \__$$/ $$ |  $$ |$$ |  $$/   $$ |  $$ |__$$ |$$ |            $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ |   
$$      \ $$ |  $$ |$$ |        $$ |  $$    $$ |$$ |            $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |   
 $$$$$$  |$$ |  $$ |$$ |   __   $$ |  $$$$$$$$ |$$ |            $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |   
/  \__$$ |$$ \__$$ |$$ \__/  | _$$ |_ $$ |  $$ |$$ |_____       $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |   
$$    $$/ $$    $$/ $$    $$/ / $$   |$$ |  $$ |$$       |      $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |   
 $$$$$$/   $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/ $$$$$$$$/        $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/    
"""
version = "Beta"
credits = f"CODED BY MayankNCodes                                                              Version- {version}"

def Banner():
    print(banner+"\n"+credits)
    

try:
    if askPasswordBeforeLogin==True:
            userInput= input("Key: ")
            try:
                if userInput==loginPassword:
                    setToken = "GO"
                else:
                    setToken = "EXIT"
            except Exception as e:
                print("Error - [1520]")
    if askPasswordBeforeLogin==False:
        setToken = "GO"
except Exception as e:
    print("Error - [1224]")

if setToken=="GO":
    Banner()
    print("\n")
    setToken = "RUN"

if setToken=="EXIT":
    print()

while setToken=="RUN":
    now = datetime.now()
    print(s)
    Found    = []
    notFound = []
    #file
    victimUsername = input("Username:: ")
    
    #Facebook
    if IntelliLib.Facebook(victimUsername)=="+":
        print("[+] FACEBOOK -- FOUND")
        Found.append("[+] FACEBOOK -- FOUND")
    if IntelliLib.Facebook(victimUsername)=="-":
        print("[-] FACEBOOK -- NONE")
        notFound.append("[-] FACEBOOK -- NONE")
    
    #Instagram
    if IntelliLib.Instagram(victimUsername)=="+":
        print("[+] INSTAGRAM -- FOUND")
        Found.append("[+] INSTAGRAM -- FOUND")
    if IntelliLib.Instagram(victimUsername)=="-":
        print("[-] INSTAGRAM -- NONE")
        notFound.append("[-] INSTAGRAM -- NONE")
        
    #Tumblr
    if IntelliLib.Tumblr(victimUsername)=="+":
        print("[+] TUMBLR -- FOUND")
        Found.append("[+] TUMBLR -- FOUND")
    if IntelliLib.Tumblr(victimUsername)=="-":
        print("[-] TUMBLR -- NONE")
        notFound.append("[-] TUMBLR -- NONE")
        
    #Threads
    if IntelliLib.Threads(victimUsername)=="+":
        print("[+] THREADS -- FOUND")
        Found.append("[+] THREADS -- FOUND")
    if IntelliLib.Threads(victimUsername)=="-":
        print("[-] THREADS -- NONE")
        notFound.append("[-] THREADS -- NONE")
        
    #Quora
    if IntelliLib.Quora(victimUsername)=="+":
        print("[+] QUORA -- FOUND")
        Found.append("[+] QUORA -- FOUND")
    if IntelliLib.Quora(victimUsername)=="-":
        print("[-] QUORA -- NONE")
        notFound.append("[-] QUORA -- NONE")
    
    #Pinterest
    if IntelliLib.Pinterest(victimUsername)=="+":
        print("[+] PINTEREST -- FOUND")
        Found.append("[+] PINTEREST -- FOUND")
    if IntelliLib.Pinterest(victimUsername)=="-":
        print("[-] PINTEREST -- NONE")
        notFound.append("[-] PINTEREST -- NONE")
    timestamp = now.strftime("%H%M%S")
    stamp = now.strftime("%d/%m/%Y - %H:%M:%S")
    name = victimUsername+" - "+str(timestamp)+".txt"
    lenFound = len(Found)
    lennotFound = len(notFound)
    with open(name,"w") as results:
        results.write(f"[REPORT PRODUCED]: {stamp}"+"\n")
        results.write(f"[USERNAME]: {victimUsername}"+"\n")
        results.write(f"{s}"+"\n")
        results.write(f"[FOUND SOCIALS] - {lenFound}"+"\n")
        for i in Found:
            results.write(f"{spacer}{i}"+"\r\n")
        results.write(f"\n\n{s}\n[NOT FOUND SOCIALS] - {lennotFound}"+"\n")
        for j in notFound:
            results.write(f"{spacer}{j}"+"\r\n")
        results.write(f"{s}\n{credits}")
        
