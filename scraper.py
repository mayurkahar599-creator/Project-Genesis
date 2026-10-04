import requests
import json
from datetime import datetime
import os
import urllib3

# हम सिस्टम को बोल रहे हैं कि SSL सिक्योरिटी की चेतावनियों को इग्नोर करे (Bypass)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TARGET_URL = "https://api.metals.live/v1/spot"

def fetch_data():
    try:
        print(f"[{datetime.now()}] Target locked. Bypassing TLS/SSL Security...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        }
        
        # सबसे बड़ा हथियार: verify=False (यह SSL सिक्योरिटी को चकमा दे देगा)
        response = requests.get(TARGET_URL, headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            gold_data = data[0]['gold']
            
            file_exists = os.path.isfile("market_data.csv")
            
            with open("market_data.csv", "a") as file:
                if not file_exists or os.stat("market_data.csv").st_size == 0:
                    file.write("Timestamp, Commodity, Price\n")
                
                file.write(f"{datetime.now()}, Gold, {gold_data}\n")
            
            print("Security Bypassed. Payload secured.")
        else:
            with open("market_data.csv", "a") as file:
                file.write(f"{datetime.now()}, BLOCKED, {response.status_code}\n")
            
    except Exception as e:
        with open("market_data.csv", "a") as file:
            file.write(f"{datetime.now()}, ERROR, {e}\n")

if __name__ == "__main__":
    fetch_data()
