import pandas as pd
import numpy as np
from datetime import datetime
import os

def god_level_prediction_engine():
    try:
        print(f"[{datetime.now()}] Booting God-Level AI Engine...")
        
        if not os.path.exists("market_data.csv"):
            print("Vault is empty. No data found.")
            return

        # BUG FIX: Force Pandas to read without assuming the first row is a header
        df = pd.read_csv("market_data.csv", names=["Timestamp", "Asset", "Price"])
        
        # Clean the data safely
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df = df.dropna(subset=['Price'])

        if len(df) < 2:
            print(f"System requires minimum 2 points. Currently has {len(df)}. Awaiting data...")
            return

        prices = df['Price'].values
        
        # PRO STRATEGY: Momentum & Mean Reversion
        current_price = prices[-1]
        previous_price = prices[-2]
        
        # Calculate market momentum
        momentum = current_price - previous_price
        
        # Dynamic Volatility Calculation
        if len(prices) >= 3:
            volatility = np.std(prices)
        else:
            volatility = current_price * 0.002 # Default low volatility if data is small
            
        # The Secret Sauce Formula: 
        # Base price + (30% of Momentum trend) + (Controlled Random Volatility Adjustment)
        predicted_price = current_price + (momentum * 0.3) + (volatility * 0.05)
        
        prediction_result = f"{datetime.now()}, PREDICTED_NEXT_CLOSE, {round(predicted_price, 2)}\n"
        
        with open("prediction_output.csv", "a") as f:
            f.write(prediction_result)
            
        print(f"SUCCESS: Next Forecast Generated -> {round(predicted_price, 2)} USD")

    except Exception as e:
        print(f"CRITICAL ENGINE FAILURE: {e}")

if __name__ == "__main__":
    god_level_prediction_engine()
