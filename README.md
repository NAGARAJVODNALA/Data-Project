# Data-Project

# Data Engineer Test - Supermarket Transactions Analysis & Maze Navigation

## Project Overview  
This project involves analyzing supermarket transaction data collected over two years to generate valuable business insights. It consists of two main tasks:  
1. Supervised Learning for Business Insights – Using Machine Learning to predict sales, assess promotional impacts, and classify high-performing supermarkets.  
2. Maze Navigation Model – Implementing reinforcement learning to train an agent to navigate a maze efficiently.  

The goal is to clean, normalize, and transform data into Python-compatible formats while leveraging Machine Learning techniques for predictive modeling and decision-making.

---

###

📊 Task 1: Supervised Learning for Business Insights
📌 Data Sources
The project uses four datasets:

Items.csv – Product details (code, type, brand, size)
Sales.csv – Sales transactions (amount, units, time, customer ID, voucher)
Promotion.csv – Promotions applied to items (week, display impact, feature)
Supermarkets.csv – Supermarket locations (supermarket number, post-code)
✅ Data Cleaning & Transformation
✔ Removed duplicates
✔ Standardized column names and formatted data types
✔ Merged datasets on common keys (code, Supermarket_No, province)

✅ Feature Engineering
✔ Created new features to capture sales patterns
✔ Extracted time-related insights (month, weekday)
✔ Mapped promotional impact

✅ Model Training & Evaluation
1️⃣ Sales Forecasting (Regression Model)
Problem Statement: Predict sales based on promotions, store location, and product features.
Algorithm Used: RandomForestRegressor
Features Used:
🏷 Product-related: code, brand, type
🏬 Store-related: Supermarket_No
🕒 Time-related: Month, Weekday
🎟 Promotion-related: Promotion Active
Evaluation Metric:
RMSE (Root Mean Squared Error)
Achieved a strong RMSE score, indicating accurate predictions
2️⃣ Supermarket Performance Classification (Classification Model)
Problem Statement: Classify supermarkets into high-performing (1) and low-performing (0).
Algorithm Used: RandomForestClassifier
Features Used: Month, Weekday, code, Promotion Active, Display Impact
Evaluation Metric:
Accuracy Score
The model achieved high accuracy, confirming the importance of key features
📈 Business Insights
📊 Promotion Impact: Sales were significantly higher when promotions were active
🛒 Weekend Sales Surge: Transactions peaked on weekends
🏬 High-Performing Stores: Certain supermarkets outperformed others due to location & promotions
💰 Customer Segmentation: High spenders contributed disproportionately to sales
🎯 Task 2: Maze Navigation Using Reinforcement Learning
📌 Objective
Design a reinforcement learning model where an agent learns to navigate a 10x10 maze while avoiding obstacles.

✅ Approach
✔ Q-learning Algorithm: Uses a Q-table to store values for each state-action pair.
✔ Rewards System:

✅ +100 for reaching the goal
🚶 -1 for moving to a valid path
❌ -10 for hitting a wall
✔ Exploration vs. Exploitation: Uses an epsilon-greedy policy to balance learning and optimal decision-making.
✔ Performance: Over 30 training iterations, the agent improves navigation efficiency.
📊 Training Results & Performance Analysis
Tracked agent movement for 30 iterations
Observed a decreasing trend in steps, indicating successful learning
Plotted a learning curve (iterations vs. steps to goal)
Real-time visualization demonstrated the agent’s progress
📈 Business Value
📊 Optimized Promotions – Identifies the best time and place for running promotions.
📦 Improved Inventory Management – Forecasts demand trends based on sales data.
🏬 Enhanced Store Operations – Helps classify high-performing supermarkets for better resource allocation.
🤖 AI-powered Decision Making – Demonstrates reinforcement learning applications in navigation and logistics.
📝 Report
A full project report, including detailed documentation, insights, and performance analysis, is available in the reports/ directory.

