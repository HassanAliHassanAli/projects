# 🛒 Olist E-commerce Analytics & Business Intelligence Project

![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data_Analysis-005571?style=for-the-badge)

## 📌 Executive Summary
This project represents a comprehensive End-to-End Business Intelligence solution designed to analyze the operations of **Olist**, a Brazilian e-commerce platform. By leveraging SQL for data extraction and **Power BI** for advanced modeling and visualization, this project transforms complex raw data into actionable strategic insights. 

As a Data & Business Analyst, my objective was to uncover trends in sales performance, financial transactions, logistics efficiency, and customer satisfaction to drive data-driven decision-making.

---

## 🏗️ Data Architecture & Modeling
Building a robust foundation was critical for this analysis. I engineered a relational data model (Star Schema) to seamlessly connect multiple raw datasets.

* **Fact Table:** `Fact_Sales_Professional_Final` acting as the central hub for transactional metrics (Price, Freight Value, Delivery Actual Days).
* **Dimension Tables:** `Raw_Customers`, `Raw_Sellers`, `Raw_Order_Items`, `Raw_Payments`, `Raw_Reviews`, and `Raw_Geo`.
* **Target Management:** Integrated `Sales_Logistics_Targets` and `TargetsTable` to track performance against strategic goals.

*(You can view the full data model in the `All_tables.png` file)*

---

## 📊 Key Dashboards & Business Insights

### 1. Sales Performance Overview
This dashboard tracks top-level KPIs and product performance to understand revenue drivers.
* **Key Insights:** Identified the top-performing product categories (`health_beauty`, `watches_gifts`, and `bed_bath_table`). Monitored the overall sales target achievement (30.82%) and analyzed the geographical distribution of sales volume across states.
* *(See: `Sales_Overview.png`)*

### 2. Financial & Payments Analysis
Focused on cash flow, transaction preferences, and revenue generation.
* **Key Insights:** Tracked a total payment value of **16.01M**. Revealed that **Credit Cards** dominate the payment methods (78.34%), and the vast majority of customers prefer single-installment payments over long-term installment plans.
* *(See: `Financial_Dashboard.png`)*

### 3. Customer Satisfaction & Feedback
Analyzing the Voice of the Customer (VoC) to gauge service quality and platform health.
* **Key Insights:** Demonstrated a strong positive sentiment, with **57.78%** of customers leaving 5-star reviews. Integrated a granular view of customer comments mapped to order IDs to help operational teams pinpoint specific pain points in 1-star and 2-star reviews.
* *(See: `Customer_Satisfaction.png`)*

### 4. Sellers Geographic Distribution
Optimizing supply chain logic by understanding where sellers are concentrated.
* **Key Insights:** Visualized the dense concentration of sellers in the **Sao Paulo** region, followed by Ibitinga and Curitiba. This geographical mapping helps in optimizing logistics, warehouse placements, and reducing freight costs.
* *(See: `Sellers_Performance.png`)*

---

## 🛠️ Tech Stack & Skills Demonstrated
* **Tools:** Power BI Desktop, SQL.
* **Data Processing:** ETL workflows, Data Cleaning, Data Transformation.
* **Data Modeling:** Star Schema design, Relationship Management (1-to-many, many-to-many).
* **DAX (Data Analysis Expressions):** Created custom measures for KPIs, target achievements, and aggregations.
* **Business Analysis:** Supply chain optimization, financial tracking, and customer experience analysis.

---

## 📂 Project Structure
```text
📦 E-commerce-Analytics-PowerBI
 ┣ 📜 Olist-E-commerce-Analytics-SQL&PowerBI-Project.pbix  (Main Power BI File)
 ┣ 🖼️ Sales_Overview.png
 ┣ 🖼️ Financial_Dashboard.png
 ┣ 🖼️ Customer_Satisfaction.png
 ┣ 🖼️ Sellers_Performance.png
 ┗ 🖼️ All_tables.png (Data Model Schema)