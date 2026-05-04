# 📈 B2B Sales Performance Analysis: Unlocking ERP Data

![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=black)
![SAP](https://img.shields.io/badge/SAP-0FAAFF?style=for-the-badge&logo=sap&logoColor=white)
![ERP Systems](https://img.shields.io/badge/ERP_Analytics-005571?style=for-the-badge)

## 📌 Executive Summary
Raw ERP systems (like SAP and Odoo) generate massive, highly normalized datasets scattered across multiple relational tables (Sales, Products, Customers). This complexity often makes it difficult for management to extract quick, actionable insights. 

The objective of this project is to bridge the gap between complex ERP backend architectures and executive decision-making. I designed an automated, interactive **Power BI dashboard** that consolidates these tables into a single **"Source of Truth"**, enabling data-driven strategies for a B2B bike manufacturer.

---

## 🏗️ Data Architecture & Modeling
To transform the raw SAP sample data into a reporting-ready format, I engineered a robust data model mapping the complex ERP relational tables:
* **Fact & Transaction Tables:** `SalesOrders` and `SalesOrderItems`.
* **Dimension Tables:** `BusinessPartners` (Clients), `Products`, and `ProductTexts`.
* **Relationship Management:** Successfully joined normalized tables to create a unified Star Schema, ensuring accurate aggregations across different currencies and regions.

*(You can view the full ERP data model in the `All_tables.png` file)*

---

## 📊 Key Business Insights
By analyzing the B2B sales data, I uncovered several critical trends:
1. **Financial Overview:** Generated **$3.22M** in total revenue across 334 B2B orders, maintaining a strong Average Order Value (AOV) of **$9.66K**.
2. **Seasonality & Trends:** Sales activity peaks significantly during February and May, but experiences a sharp, critical drop during the late summer (August).
3. **Client & Product Dominance:** * **Top Client:** "Bike World Inc." is the undisputed top client generating **$158K** in revenue.
   * **Top Product:** The "Speedeon Cross" dominates product sales, bringing in **$0.35M**.

*(See: `dashboard_preview.png`)*

---

## 🎯 Strategic Recommendations
As a Business Analyst, my role goes beyond visualizations. Based on the insights, I formulated the following strategic actions for the management team:
* **Counteract Seasonal Drops:** Launch targeted promotional campaigns and discounts specifically in July and August to mitigate the historical summer sales slump.
* **Client Retention:** Establish a "VIP Account Management" program for the top 5 clients (especially *Bike World Inc.*) to secure and expand these high-value B2B relationships.
* **Supply Chain Optimization:** Increase manufacturing and stock levels for the "Speedeon" and "Lazy Cat" product lines ahead of the early peak season (January/February) to prevent potential stockouts.

---

## 🛠️ Tech Stack & Skills Demonstrated
* **Business Intelligence:** Power BI Desktop.
* **Data Source:** ERP Sample Data (SAP / Cloud Data).
* **Data Modeling:** Relational Database Mapping, Star Schema design.
* **Business Analysis:** KPI tracking, Seasonality Analysis, Strategic B2B Recommendations.
* **Presentation:** Delivered a comprehensive executive presentation (`B2B_Sales_Performance_Analysis.pptx`) to communicate findings to stakeholders.

---

## 📂 Project Structure
```text
📦 ERP-Sales-Data-Analytics-Project
 ┣ 📜 Odoo_Sales_Dashboard.pbix               (Main Power BI File)
 ┣ 📜 B2B_Sales_Performance_Analysis.pptx     (Executive Presentation)
 ┣ 🖼️ dashboard_preview.png                   (Dashboard Snapshot)
 ┗ 🖼️ All_tables.png                          (ERP Data Model Schema)