# 📦 Supply Chain & Delivery Performance Analysis (SQL)

## 📌 Project Overview
This project aims to identify and solve critical bottlenecks in the supply chain and delivery process for a global e-commerce dataset (DataCo Smart Supply Chain). The analysis focuses on understanding the root causes of delayed deliveries, identifying the most affected regions, and quantifying the financial impact (Revenue at Risk) of these delays.

## 🎯 Business Questions Answered
1. Which geographical regions suffer the most from late deliveries?
2. Which shipping modes are the primary drivers of these delays?
3. What is the average delay duration (in days) compared to the scheduled shipping time?
4. Which specific products are most frequently delayed?
5. **The Financial Impact:** Which regions cause the highest "Revenue at Risk" due to late deliveries?

## 🛠️ Tools Used
* **Database:** Microsoft SQL Server (SSMS)
* **Language:** SQL (Data Cleaning, Aggregation, and Analysis)
* **Dataset:** DataCo Smart Supply Chain (Kaggle) - Over 180,000 records.

## 📊 Key Findings & Insights

### 1. The Regional Bottleneck
While **Central America** has the highest volume of late orders (15,518 orders), **Western Europe** presents the largest financial risk. Late deliveries in Western Europe tie up over **$3.29 Million** in revenue, making it the top priority for supply chain optimization.

### 2. The Shipping Mode Crisis
The primary cause of delays is not regional infrastructure, but rather specific shipping modes.
* **Standard Class** accounts for the highest *number* of delayed orders globally.
* However, **Second Class** shipping has the worst *delay duration*, arriving an average of **2.5 days later** than the scheduled delivery date.

### 3. Most Affected Products
The analysis revealed that fitness equipment and sporting goods are the most frequently delayed items. The **"Perfect Fitness Perfect Rip Deck"** (Cleats category) is the single most delayed product, with over 13,400 late orders.

## 💡 Strategic Recommendations
1. **Prioritize Western Europe Contracts:** Immediately review and renegotiate Service Level Agreements (SLAs) with logistics partners handling Standard and Second Class shipments in Western Europe to mitigate the $3.29M revenue risk.
2. **Re-evaluate "Second Class" Logistics:** Conduct a deep dive into the routing and carrier performance for Second Class shipping, as the consistent 2.5-day delay severely impacts customer satisfaction.
3. **Inventory Relocation:** Consider positioning high-demand, frequently delayed items (like the "Perfect Fitness Perfect Rip Deck") in fulfillment centers closer to the high-risk regions (Central America and Western Europe).

## 📂 Project Files
* `Supply_Chain_Analysis.sql`: Contains all the SQL queries used for data exploration and insight generation.