 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
from datetime import datetime
import os
import re

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://coinmarketcap.com/"
driver.get(url)

time.sleep(8)
rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")[:10]

crypto_data = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    try:
        crypto_data.append({
            "Time": timestamp,
            "Coin": cols[2].text,
            "Price": cols[3].text,
            "24h Change": cols[4].text,
            "Market Cap": cols[6].text
        })
    except:
        pass
driver.quit()
df = pd.DataFrame(crypto_data)
file_name = "crypto_prices.csv"

if os.path.exists(file_name):
    df.to_csv(file_name, mode="a", header=False, index=False)
else:
    df.to_csv(file_name, index=False)

print(f"✅ Successfully saved data for {len(df)} cryptocurrencies")
print("📁 File:", file_name)

def extract_change(value):
    try:
        num = re.findall(r"-?\d+\.?\d*", value.replace(',', ''))
        return float(num[0]) if num else 0
    except:
        return 0

df["24h_numeric"] = df["24h Change"].apply(extract_change)
positive = df[df["24h_numeric"] > 0]

print("\n🚀 Coins with Positive 24h Change:")
if positive.empty:
    print("No positive movers at this time (market is down).")
else:
    print(positive[["Coin", "Price", "24h Change"]])
