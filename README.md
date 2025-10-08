🛍️ E-commerce Sales Performance Dashboard (Data Storytelling Project)
Overview
This project showcases the end-to-end process of turning raw e-commerce transaction data into actionable business intelligence through an interactive, deployed web application.

The goal was to move beyond static analysis and create a dynamic tool that allows stakeholders to explore key performance indicators (KPIs), identify sales trends, and understand core product performance and customer behavior.

🚀 Live Demo
View the Live Dashboard Here:Local URL: http://localhost:8501
  Network URL: http://192.168.0.141:8501

GitHub Repository: https://github.com/kiran27262/E-commerce-Sales-Performance-Dashboard..git

Key Insights (The Data Story)
By performing data cleaning, feature engineering, and visualization, the following critical business insights were revealed:

Revenue Volatility: The Monthly Revenue Trend chart shows significant seasonality, with a strong revenue spike in November and December. This suggests that resource allocation and marketing spend should be heavily front-loaded in Q4 to maximize holiday season returns.

Top Product Concentration: Analysis of units sold demonstrates that the Top 3 products account for over 40% of total sales volume. This highlights a dependence on a few core items, indicating a potential risk if those products are discontinued or face market competition.

Sales Timing: The daily activity breakdown reveals that Tuesday and Wednesday are the peak revenue days, while weekends show lower transaction volumes. This insight can be used to optimize staffing, inventory replenishment, and customer service scheduling.

🛠️ Skills and Technologies Demonstrated
This project validates my proficiency in a full data science and web deployment pipeline:

Python (Pandas): Data cleaning, preprocessing, feature engineering (calculating Revenue, extracting Date/Month components), and aggregation.

Data Analysis & EDA: Identifying critical business KPIs, detecting trends, and formulating hypotheses based on sales data.

Data Visualization (Plotly): Creating professional, interactive charts (line, bar, and pie charts) that allow users to hover for details.

Web Development (Streamlit): Building and styling a clean, functional, and fully responsive user interface (UI) with interactive filters (product multiselect) and performance metrics.

Deployment: Successfully deploying the application to a cloud service (Streamlit Cloud or similar) for 24/7 accessibility.

How to Run Locally
Clone the repository:

git clone [YOUR REPO LINK]
cd ecommerce-dashboard

Install dependencies: (Make sure you are in your Anaconda environment if you used Conda)

pip install -r requirements.txt

Run the application:

streamlit run app.py
