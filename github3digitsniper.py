import requests
import time
import random
import string

# --- KUZEY 2.0 SETTINGS ---
GITHUB_TOKEN = "BURAYA_TOKENINI_YAZ" 
CHECK_SPEED = 2.0 

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHub-3-Letter-Sniper"
}

def is_nick_available(nick):
    url = f"https://api.github.com/users/{nick}"
    r = requests.get(url, headers=headers)
    return r.status_code == 404

def claim_nick(nick):
    url = "https://api.github.com/user"
    r = requests.patch(url, headers=headers, json={"login": nick})
    return r.status_code == 200

print("🚀 Sniper started, scanning for 3-letter usernames...")

while True:
    chars = string.ascii_lowercase + string.digits
    target = ''.join(random.choices(chars, k=3))
    
    print(f"🔍 Checking: {target}")
    
    if is_nick_available(target):
        print(f"✨ {target} is AVAILABLE! Attempting to claim...")
        if claim_nick(target):
            print(f"🎯 SUCCESS! Your new username is: {target}")
            break
            
    time.sleep(CHECK_SPEED)