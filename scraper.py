import yfinance as yf
from datetime import datetime
import os

def fetch_data():
    try:
        print(f"[{datetime.now()}] Hunting for data... Bypassing weekend closures.")
        
        gold = yf.Ticker("GC=F")
        
        # 1d की जगह हमने 5d कर दिया है। अगर आज संडे है, तो ये फ्राइडे का रेट निकाल लाएगा!
        data = gold.history(period="5d")
        
        file_exists = os.path.isfile("market_data.csv")
        
        with open("market_data.csv", "a") as file:
            if not file_exists or os.stat("market_data.csv").st_size == 0:
                file.write("Timestamp, Commodity, Price (USD)\n")
            
            if not data.empty:
                current_price = data['Close'].iloc[-1]
                file.write(f"{datetime.now()}, Gold (GC=F), {round(current_price, 2)}\n")
                print(f"Success! Extracted Price: {round(current_price, 2)} USD")
            else:
                # अगर मार्केट पूरी तरह गायब हो, तो भी फाइल में एंट्री होगी ताकि हमें पता रहे
                file.write(f"{datetime.now()}, Gold (GC=F), MARKET_CLOSED\n")
                print("Market closed, forced empty log entry.")
            
    except Exception as e:
        print(f"Extraction failed: {e}")
        with open("market_data.csv", "a") as file:
            file.write(f"{datetime.now()}, ERROR, {e}\n")

if __name__ == "__main__":
    fetch_data()
