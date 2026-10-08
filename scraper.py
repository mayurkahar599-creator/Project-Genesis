import os
import yfinance as yf
from datetime import datetime
from supabase import create_client, Client

def execute_extraction():
    try:
        print(f"[{datetime.now()}] Initiating Secure Data Extraction...")
        
        # 1. Fetch live accurate data using yfinance
        ticker = yf.Ticker("GC=F")
        current_price = ticker.history(period="1d")['Close'].iloc[-1]
        price = round(float(current_price), 2)
        print(f"Extracted GC=F Price: ${price}")

        # 2. Supabase Injection (The Enterprise Vault)
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        
        if url and key:
            try:
                supabase: Client = create_client(url, key)
                supabase.table('genesis_market_data').insert({"asset": "Gold (GC=F)", "price": price}).execute()
                print("SUCCESS: Data injected into Supabase Enterprise Vault.")
            except Exception as db_err:
                print(f"DATABASE ERROR: {db_err}")
        else:
            print("WARNING: Supabase Keys missing. Engine running in legacy mode.")

        # 3. CSV Fallback (To keep the current GitHub Pages Dashboard running)
        with open("market_data.csv", "a") as f:
            f.write(f"{datetime.now()}, Gold (GC=F), {price}\n")
        print("SUCCESS: Data saved to Legacy CSV.")

    except Exception as e:
        print(f"CRITICAL SYSTEM FAILURE: {e}")

if __name__ == "__main__":
    execute_extraction()
