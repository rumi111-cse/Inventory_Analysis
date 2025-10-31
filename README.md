🚀 Overview

This project demonstrates a complete data-to-decision pipeline designed to analyze vendor performance for a procurement team.
You’ll explore raw purchase, sales, and freight data; perform ETL using Python & SQLite; and visualize insights through an interactive Power BI dashboard.

It’s structured like a real-world company assignment to prove you can translate data into business decisions — the kind of case study that impresses recruiters and hiring managers.


🧠 Key Learning Objectives

Build a SQL-based data model from messy procurement data

Create Python ETL pipelines for ingestion and cleaning

Perform Exploratory Data Analysis (EDA) and business KPIs in Jupyter

Design interactive Power BI dashboards to communicate results

Deliver a professional report with insights and recommendations

⚙️ Project Pipeline

Data Ingestion → Load multiple CSVs into SQLite using ingestiondeb.py

Data Processing → Merge and aggregate vendor data via get_vendor_summary.py

Exploratory Data Analysis → Perform EDA in Jupyter (EDA.ipynb)
Dashboard Creation → Visualize KPIs, trends, and performance metrics in Power BI

📊 Example KPIs

Gross Profit
TotalSalesDollars - TotalPurchaseDollars

Profit Margin (%)
(GrossProfit / TotalSalesDollars) * 100

Stock Turnover
TotalSalesQuantity / TotalPurchaseQuantity

Sales-to-Purchase Ratio
TotalSalesDollars / TotalPurchaseDollars


💡 Insights Delivered

Identify top and under-performing vendors

Measure freight cost impact on overall profit

Detect inventory inefficiencies and sales-to-purchase imbalances

Provide strategic recommendations for vendor optimization

Reporting & Recommendations → Document findings and improvement strategies

optimization

🛠️ How to Run the Project

Clone this repository

git clone https://github.com/<your-username>/Vendor-Performance-Analysis.git
cd Vendor-Performance-Analysis

Install dependencies

pip install pandas sqlalchemy


Place CSV files in the /data folder

Run ingestion

python scripts/ingestiondeb.py


Generate vendor summary

python scripts/get_vendor_summary.py


Open Power BI and connect to inventory.db or load the .pbix dashboard.


🧩 Tools & Technologies

SQL / SQLite – data storage and transformation

Python (pandas, SQLAlchemy) – ETL & EDA

Power BI – dashboard & storytelling

Jupyter Notebook – analysis & documentation

🧾 Results Summary

Improved vendor evaluation visibility

Identified cost-heavy suppliers and freight inefficiencies

Provided actionable KPIs for procurement optimization

Delivered production-ready dashboards and reports
