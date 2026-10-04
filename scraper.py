import requests
import json
from datetime import datetime
import os

TARGET_URL = "https://api.metals.live/v1/spot"

def fetch_data():
    try:
        print(f"[{datetime.now()}] Target locked. Deploying stealth extraction...")
        
        # यह सबसे जरूरी हिस्सा है। हम साइट को बेवकूफ बना रहे हैं कि हम Chrome ब्राउज़र हैं, कोई बॉट नहीं।
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        }
        
        # Timeout ऐड किया है ताकि अगर साइट स्लो हो तो हमारा बॉट क्रैश ना हो
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            gold_data = data[0]['gold']
            
            # एक खाली फाइल क्रिएट करने का फोर्सफुल तरीका (अगर पहले से ना हो)
            file_exists = os.path.isfile("market_data.csv")
            
            with open("market_data.csv", "a") as file:
                # अगर फाइल नई है तो पहले हेडिंग डाल दो
                if not file_exists:
                    file.write("Timestamp, Commodity, Price\n")
                
                file.write(f"{datetime.now()}, Gold, {gold_data}\n")
            
            print("Extraction successful. Payload secured.")
        else:
            print(f"Target blocked us again. Status Code: {response.status_code}")
            # अगर ब्लॉक होता है, तो भी हम एक डमी फाइल बनाएंगे ताकि गिटहब क्रैश ना हो
            with open("market_data.csv", "a") as file:
                file.write(f"{datetime.now()}, BLOCKED, {response.status_code}\n")
            print("Dummy file created to prevent GitHub workflow crash.")
            
    except Exception as e:
        print(f"Extraction failed completely: {e}")
        # एरर आने पर भी डमी फाइल बनाओ
        with open("market_data.csv", "a") as file:
            file.write(f"{datetime.now()}, ERROR, {e}\n")

if __name__ == "__main__":
    fetch_data()
