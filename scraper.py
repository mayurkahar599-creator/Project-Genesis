import requests
import json
from datetime import datetime
import os

# यह एक पब्लिक B2B API है जो ग्लोबल मेटल रेट्स (जैसे सोना, चांदी) देता है।
# POC के लिए यह परफेक्ट है।
TARGET_URL = "https://api.metals.live/v1/spot"

def fetch_data():
    try:
        print(f"[{datetime.now()}] Target locked. Extracting B2B Commodity data...")
        
        # Headers ऐड कर रहे हैं ताकि हम बॉट ना लगें
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(TARGET_URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            # सोने (Gold) का रेट निकाल रहे हैं
            gold_data = data[0]['gold']
            
            # फाइल में सेव कर रहे हैं
            with open("market_data.csv", "a") as file:
                file.write(f"{datetime.now()}, Gold, {gold_data}\n")
            
            print("Data extracted and secured successfully.")
        else:
            print(f"Target blocked the request. Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"Error in extraction: {e}")

if __name__ == "__main__":
    fetch_data()
