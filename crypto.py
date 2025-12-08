# =====================================================
# Cryptocurrency Price Tracker with HTML Output
# (NO Jinja2 required)
# =====================================================

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

# ---------- 1. Chrome setup ----------
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ---------- 2. Open website ----------
url = "https://coinmarketcap.com/"
driver.get(url)
time.sleep(8)

# ---------- 3. Scrape Top 10 ----------
rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")[:10]

data = []
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    try:
        data.append({
            "Time": timestamp,
            "Coin": cols[2].text,
            "Price": cols[3].text,
            "24h Change": cols[4].text,
            "Market Cap": cols[6].text
        })
    except:
        pass

driver.quit()

df = pd.DataFrame(data)

# ---------- 4. Save CSV ----------
csv_file = "crypto_prices.csv"
if os.path.exists(csv_file):
    df.to_csv(csv_file, mode="a", header=False, index=False)
else:
    df.to_csv(csv_file, index=False)

print("✅ CSV file updated")

# ---------- 5. HTML generation ----------
html_rows = ""

def extract_number(value):
    try:
        return float(re.findall(r"-?\d+\.?\d*", value.replace(',', ''))[0])
    except:
        return 0

for _, row in df.iterrows():
    change = extract_number(row["24h Change"])
    color = "green" if change > 0 else "red" if change < 0 else "black"

    html_rows += f"""
    <tr>
        <td>{row['Time']}</td>
        <td>{row['Coin']}</td>
        <td>{row['Price']}</td>
        <td style="color:{color}; font-weight:bold;">{row['24h Change']}</td>
        <td>{row['Market Cap']}</td>
    </tr>
    """

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Price Tracker</title>
    <style>
        body {{
            font-family: Arial;
            background-color: #f4f6f9;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
        }}
        table {{
            width: 90%;
            margin: auto;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #222;
            color: white;
        }}
    </style>
</head>
<body>

<h1>💰 Cryptocurrency Price Tracker</h1>
<p style="text-align:center;">Last Updated: {timestamp}</p>

<table>
    <tr>
        <th>Time</th>
        <th>Coin</th>
        <th>Price</th>
        <th>24h Change</th>
        <th>Market Cap</th>
    </tr>
    {html_rows}
</table>

</body>
</html>
"""

with open("crypto_dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML page created: crypto_dashboard.html")
