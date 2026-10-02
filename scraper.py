import requests
import json
from datetime import datetime

# यह हमारा टारगेट है (अभी के लिए एक फ्री/डमी API, बाद में हम असली शिकार करेंगे)
TARGET_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_data():
    try:
        print(f"[{datetime.now()}] Target locked. Extracting data...")
        response = requests.get(TARGET_URL)
        
        if response.status_code == 200:
            data = response.json()
            # हम सिर्फ काम का डेटा निकालेंगे
            price = data['bpi']['USD']['rate']
            time_updated = data['time']['updated']
            
            # इसे एक टेक्स्ट या CSV फाइल में सेव करेंगे
            with open("market_data.csv", "a") as file:
                file.write(f"{time_updated}, {price} USD\n")
            
            print("Data extracted and secured successfully.")
        else:
            print("Target blocked the request. We need to bypass next time.")
            
    except Exception as e:
        print(f"Error in extraction: {e}")

if __name__ == "__main__":
    fetch_data()
