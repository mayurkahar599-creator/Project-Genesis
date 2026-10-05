import pandas as pd
import numpy as np
from datetime import datetime
import os

def run_prediction():
    try:
        print(f"[{datetime.now()}] Booting AI Prediction Engine...")
        if not os.path.exists("market_data.csv"):
            print("No data found to analyze.")
            return

        df = pd.read_csv("market_data.csv")
        # सिर्फ वैलिड नंबर वाला डेटा रखेंगे
        df['Price (USD)'] = pd.to_numeric(df.iloc[:, 2], errors='coerce')
        df = df.dropna(subset=['Price (USD)'])

        if len(df) < 2:
            print("Need more data points to predict accurately. Waiting for tomorrow's extraction.")
            return

        # क्वांटिटेटिव मॉडल: पिछले कुछ दिनों का एवरेज और मार्केट वोलैटिलिटी (Volatility)
        recent_avg = df['Price (USD)'].tail(3).mean()
        volatility = df['Price (USD)'].std()
        
        if pd.isna(volatility):
            volatility = 0
            
        predicted_price = recent_avg + (volatility * 0.05) 

        prediction_result = f"{datetime.now()}, PREDICTED_NEXT_CLOSE, {round(predicted_price, 2)}\n"
        
        with open("prediction_output.csv", "a") as f:
            f.write(prediction_result)
            
        print(f"Analysis Complete. Tomorrow's Forecast: {round(predicted_price, 2)} USD")

    except Exception as e:
        print(f"Engine Error: {e}")

if __name__ == "__main__":
    run_prediction()
