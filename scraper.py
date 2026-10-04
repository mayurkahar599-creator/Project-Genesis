import yfinance as yf
from datetime import datetime
import os

def fetch_data():
    try:
        print(f"[{datetime.now()}] Shifting target to Yahoo Finance Backend...")
        
        # GC=F दुनिया भर में सोने (Gold Futures) का असली टिकर सिंबल है
        gold = yf.Ticker("GC=F")
        
        # पिछले 1 दिन का डेटा निकाल रहे हैं
        data = gold.history(period="1d")
        
        if not data.empty:
            # लेटेस्ट क्लोजिंग प्राइस निकाल रहे हैं
            current_price = data['Close'].iloc[-1]
            
            file_exists = os.path.isfile("market_data.csv")
            with open("market_data.csv", "a") as file:
                if not file_exists or os.stat("market_data.csv").st_size == 0:
                    file.write("Timestamp, Commodity, Price (USD)\n")
                
                # कीमत को 2 डेसिमल तक राउंड कर रहे हैं
                file.write(f"{datetime.now()}, Gold (GC=F), {round(current_price, 2)}\n")
            
            print(f"Success! Gold Price Extracted: {round(current_price, 2)} USD")
        else:
            print("Data stream empty. Market might be completely closed or symbol changed.")
            
    except Exception as e:
        print(f"Extraction failed: {e}")
        with open("market_data.csv", "a") as file:
            file.write(f"{datetime.now()}, ERROR, {e}\n")

if __name__ == "__main__":
    fetch_data()
