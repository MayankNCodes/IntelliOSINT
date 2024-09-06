import requests

passcode = ""

pinterest = "https://www.pinterest.com/"
facebook  = "https://www.facebook.com/"
instagram = "https://www.instagram.com/"
tumblr    = "https://www.tumblr.com/"
threads   = "https://www.threads.net/@"
#twitter   = "https://nitter.net/" # Will introduce functionality soon.
quora     = "https://www.quora.com/profile/"

def Pinterest(param):
    # * Principle: Response Content Length Varies
    # ! Exists:     ALMOST 700K
    # ! Not-Exist:  ~400XXX
    
    request = requests.get(f"{pinterest}{param}")
    #print(len(request.content))
    resp = len(request.content)
    if resp > 600000:
        return "+"
    if resp < 600000:
        return "-"
    
def Facebook(param):
    # * Principle: Response Content Length Varies
    # ! Exists:     ALMOST 280K
    # ! Not-Exist:   ~160XXX
    
    request = requests.get(f"{facebook}{param}")
    #print(len(request.content))
    resp = len(request.content)
    if resp > 270000:
        return "+"
    if resp < 270000:
        return "-"
    
def Instagram(param):
    # * Principle: Response Content Length Varies
    # ! Exists:      MORE THAN 300K    
    # ! Not-Exist:   ~200XXX
    
    request = requests.get(f"{instagram}{param}")
    #print(len(request.content))
    resp = len(request.content)
    if resp > 300000:
        return "+"
    if resp < 300000:
        return "-"
    
def Tumblr(param):
    # * Principle: Response Content Length Varies
    # ! Exists:       MORE THAN 200K 
    # ! Not-Exist:    ~40XXX
    
    request = requests.get(f"{tumblr}{param}")
    #print(len(request.content))
    resp = len(request.content)
    if resp > 300000:
        return "+"
    if resp < 300000:
        return "-"
    
def Threads(param):
    # * Principle: Response Content Length Varies
    # ! Exists:       MORE THAN AND ALMOST 320XXX 
    # ! Not-Exist:    ~190XXX
    
    request = requests.get(f"{threads}{param}") # * Threads Requires @ Before Username. EX- @AnExample
    #print(len(request.content))
    resp = len(request.content)
    if resp > 240000:
        return "+"
    if resp < 240000:
        return "-"

def Quora(param):
    # * Principle: Response Content Length Varies
    # ! Exists:       MORE THAN 100XXX
    # ! Not-Exist:    64XXX
    
    request = requests.get(f"{quora}{param}") # * Threads Requires @ Before Username. EX- @AnExample
    #print(len(request.content))
    resp = len(request.content)
    if resp > 100000:
        return "+"
    if resp < 100000:
        return "-"




