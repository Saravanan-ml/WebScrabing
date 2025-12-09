# WebScrabing
# 📈 Real-Time Cryptocurrency Price Tracker (Web Scraping)

A Python-based web scraping project that extracts **real-time cryptocurrency market data** from **CoinMarketCap** using **Selenium WebDriver**.  
The project automates data collection, stores structured records, and supports visualization-ready outputs.

🔍 Project Overview

The **Cryptocurrency Price Tracker** is designed to eliminate manual monitoring of cryptocurrency prices.  
Since CoinMarketCap uses **JavaScript-rendered content**, the project uses **Selenium** to dynamically load pages and extract accurate real-time data.

The system collects:
 Cryptocurrency name  
 Current price  
 24-hour price change  
 Market capitalization  

The scraped data is saved in CSV format and can be used for dashboards, analysis, and reports.

✨ Key Features

 ✅ Real-time cryptocurrency price scraping  
 ✅ Dynamic page handling using Selenium  
 ✅ Top 10 cryptocurrencies tracking  
 ✅ Headless browser execution  
 ✅ CSV export with timestamped data  
 ✅ Identification of positive market movers  
 ✅ Clean and modular code structure  

## 🔄 Workflow

1. **Launch Headless Browser**  
   - Selenium initializes a Chrome browser in headless mode.

2. **Load Data Source**  
   - CoinMarketCap website is loaded and JavaScript content is rendered.

3. **Extract Market Data**  
   - Top 10 cryptocurrency rows are identified and scraped.

4. **Process Data**  
   - Extracted text data is cleaned and converted into structured format.

5. **Store Data**  
   - Data is appended to a CSV file for historical tracking.

6. **Analyze Market Movement**  
   - 24-hour percentage change is converted to numeric values to identify positive movers.

7. **Display Output**  
   - Results are printed in the console and saved for visualization.

## 🛠️ Technology Stack

 **Programming Language:** Python  
 **Web Scraping:** Selenium WebDriver  
 **Browser Automation:** Google Chrome (Headless)  
 **Data Processing:** Pandas  
 **Driver Management:** webdriver-manager  

## 🔄 Future Enhancements

*Multi-source cryptocurrency data scraping
*Real-time alerts and notifications
*Database integration
*Dashboard and cloud deployment
*Machine learning-based trend prediction
