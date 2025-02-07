# 🛒 Data-Project: Supermarket Transactions Analysis & Maze Navigation  

## 📌 Project Overview
This project involves analyzing **supermarket transaction data** collected over **two years** to generate **valuable business insights**. The goal is to **clean, normalize, and transform** data into **Python-compatible formats** while leveraging **Machine Learning techniques** for predictive modeling. Additionally, a reinforcement learning approach is implemented for **maze navigation**.

---

## 📊 Task 1: Supervised Learning for Business Insights

### **📌 Data Sources**
The project uses **four datasets**:

- 📄 **Items.csv** – Product details (**code, type, brand, size**)
- 📄 **Sales.csv** – Sales transactions (**amount, units, time, customer ID, voucher**)
- 📄 **Promotion.csv** – Promotions applied to items (**week, display impact, feature**)
- 📄 **Supermarkets.csv** – Supermarket locations (**supermarket number, post-code**)

---

### **✅ Data Cleaning & Transformation**
✔ Removed **duplicates**  
✔ Standardized **column names** and formatted **data types**  
✔ Merged datasets on **common keys** (`code`, `supermarket`, `province`)  

---

### **✅ Feature Engineering**
✔ Created new **features** to **capture sales patterns**  
✔ Extracted **time-related insights** (`week`, `units`)  
✔ Mapped **promotional impact**  

---

## **✅ Model Training & Evaluation**

### **1️⃣ Sales Forecasting (Neural Network Model)**
**🔹 Problem Statement:** Predict sales based on **promotions, store location, and product features**.  
**🔹 Algorithm Used:** MLP Regressor (Neural Network)  
**🔹 Features Used:**  
- 🏷 **Product-related:** `code`, `brand`, `type`  
- 🏬 **Store-related:** `supermarket`  
- 🕒 **Time-related:** `week`, `units`  
- 🎟 **Promotion-related:** `promotion active`, `display impact`  
**🔹 Evaluation Metric:** **RMSE (Root Mean Squared Error) and R² Score**  
- **RMSE:** 0.1664 (lower is better)  
- **R² Score:** 0.7555 (explains 75.55% of variance in sales data)  

---

### **📈 Business Insights**
✔ **📊 Promotion Impact:** Sales were significantly **higher when promotions were active**  
✔ **🛒 Weekly Sales Trends:** Sales **fluctuate over weeks**, peaking during certain periods  
✔ **🏬 High-Performing Stores:** Certain supermarkets **outperform others due to location & promotions**  
✔ **💰 Customer Segmentation:** High spenders **contribute disproportionately to sales**  

---

## **📊 Business Recommendations**

### **1. Optimize Promotional Strategies**
- Focus on **Type 2 items** and **top-selling brands** for marketing campaigns.  
- Use **A/B testing** to determine the most effective promotional techniques.  
- Increase targeted promotions on items with higher demand elasticity.  

### **2. Improve Demand Forecasting**
- Leverage sales predictions for **inventory planning** and **supply chain adjustments**.  
- Plan promotional events based on predicted high-demand weeks.  
- Implement real-time tracking to adjust stock levels dynamically.  

### **3. Enhance Model Performance**
- Incorporate **additional features** (e.g., customer demographics, seasonal trends, external factors).  
- Implement **hyperparameter tuning** for the neural network to improve predictive power.  
- Experiment with **alternative machine learning models** such as XGBoost or ensemble methods for improved accuracy.  

---

## 🎯 Task 2: Maze Navigation Using Reinforcement Learning  

### **📌 Objective**  
Design a **reinforcement learning model** where an agent **learns to navigate** a **10x10 maze** while **avoiding obstacles**.  

---

### **✅ Approach**  
✔ **Q-learning Algorithm:** Uses a **Q-table** to store values for each state-action pair.  
✔ **Rewards System:**  
  - ✅ **+100** for reaching the goal  
  - 🚶 **-1** for moving to a valid path  
  - ❌ **-10** for hitting a wall  
✔ **Exploration vs. Exploitation:** Uses an **epsilon-greedy policy** to balance learning and optimal decision-making.  
✔ **Performance:** Over **30 training iterations**, the agent **improves navigation efficiency**.  

---

## **📊 Training Results & Performance Analysis**  
✔ **Tracked agent movement** for **30 iterations**  
✔ **Observed a decreasing trend in steps**, indicating **successful learning**  
✔ **Plotted a learning curve (iterations vs. steps to goal)**  
✔ **Real-time visualization** demonstrated the agent’s progress  

---

## **📈 Business Value**  

- **📊 Optimized Promotions** – Identifies the best **time and place** for running promotions.  
- **📦 Improved Inventory Management** – Forecasts **demand trends** based on sales data.  
- **🏬 Enhanced Store Operations** – Helps classify **high-performing supermarkets** for better resource allocation.  
- **🤖 AI-powered Decision Making** – Demonstrates reinforcement learning applications in **navigation and logistics**.  

---

## 📝 Report  
A **full project report**, including **detailed documentation, insights, and performance analysis**, is available in the files.  

---

