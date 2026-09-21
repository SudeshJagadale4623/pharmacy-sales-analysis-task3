"""
Pharmacy Sales & Drug Analysis
--------------------------------
Internship Task 3 - VirtualWorks Lab

Steps:
1. Load and explore the pharmacy sales dataset
2. Identify top-selling medicines
3. Analyze monthly sales growth
4. Compare branded vs generic medicine sales
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

pd.set_option("display.width", 120)

# ---------------------------------------------------------
# STEP 1: LOAD & EXPLORE
# ---------------------------------------------------------
df = pd.read_csv("pharmacy_sales_data.csv", parse_dates=["Date"])

print("=" * 60)
print("STEP 1: DATA OVERVIEW")
print("=" * 60)
print(f"Shape: {df.shape}")
print(df.head())
print("\nColumn types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

total_sales = df["TotalAmount"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["OrderID"].nunique()
avg_order_value = total_sales / total_orders

print(f"\nTotal Sales: ${total_sales:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

# ---------------------------------------------------------
# STEP 2: TOP-SELLING MEDICINES
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 2: TOP-SELLING MEDICINES")
print("=" * 60)

top_by_revenue = df.groupby("MedicineName")["TotalAmount"].sum().sort_values(ascending=False).head(10)
top_by_quantity = df.groupby("MedicineName")["Quantity"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 medicines by revenue:")
print(top_by_revenue.round(2))
print("\nTop 10 medicines by quantity sold:")
print(top_by_quantity)

# ---------------------------------------------------------
# STEP 3: MONTHLY SALES GROWTH
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 3: MONTHLY SALES TREND")
print("=" * 60)

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["TotalAmount"].sum().sort_index()
monthly_growth = monthly_sales.pct_change().fillna(0) * 100

print("\nMonthly sales:")
print(monthly_sales.round(2))
print("\nMonth-over-month growth (%):")
print(monthly_growth.round(1))

# ---------------------------------------------------------
# STEP 4: BRANDED VS GENERIC COMPARISON
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 4: BRANDED VS GENERIC ANALYSIS")
print("=" * 60)

brand_vs_generic = df.groupby("Type").agg(
    Total_Sales=("TotalAmount", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Orders=("OrderID", "nunique"),
    Avg_Unit_Price=("UnitPrice", "mean"),
).round(2)
brand_vs_generic["Avg_Order_Value"] = (brand_vs_generic["Total_Sales"] / brand_vs_generic["Orders"]).round(2)

print(brand_vs_generic)

# Category breakdown
print("\nSales by category:")
category_sales = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)
print(category_sales.round(2))

# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------
# Monthly sales trend
plt.figure(figsize=(8, 4))
monthly_sales.plot(kind="line", marker="o", color="#2563eb")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales ($)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=120)
plt.close()

# Top 10 medicines by revenue
plt.figure(figsize=(8, 5))
top_by_revenue.sort_values().plot(kind="barh", color="#f59e0b")
plt.title("Top 10 Medicines by Revenue")
plt.xlabel("Revenue ($)")
plt.tight_layout()
plt.savefig("top_medicines_revenue.png", dpi=120)
plt.close()

# Branded vs Generic pie chart
plt.figure(figsize=(5, 5))
brand_vs_generic["Total_Sales"].plot(kind="pie", autopct="%1.1f%%", colors=["#3b82f6", "#10b981"])
plt.title("Branded vs Generic — Share of Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("branded_vs_generic.png", dpi=120)
plt.close()

print("\nCharts saved: monthly_sales_trend.png, top_medicines_revenue.png, branded_vs_generic.png")

# ---------------------------------------------------------
# SAVE TEXT SUMMARY
# ---------------------------------------------------------
with open("analysis_summary.txt", "w") as f:
    f.write("PHARMACY SALES & DRUG ANALYSIS SUMMARY\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total Sales: ${total_sales:,.2f}\n")
    f.write(f"Total Quantity Sold: {total_quantity:,}\n")
    f.write(f"Total Orders: {total_orders:,}\n")
    f.write(f"Average Order Value: ${avg_order_value:,.2f}\n\n")
    f.write("Top 10 Medicines by Revenue:\n")
    f.write(top_by_revenue.round(2).to_string() + "\n\n")
    f.write("Monthly Sales:\n")
    f.write(monthly_sales.round(2).to_string() + "\n\n")
    f.write("Month-over-Month Growth (%):\n")
    f.write(monthly_growth.round(1).to_string() + "\n\n")
    f.write("Branded vs Generic Comparison:\n")
    f.write(brand_vs_generic.to_string() + "\n\n")
    f.write("Sales by Category:\n")
    f.write(category_sales.round(2).to_string() + "\n")

print("\nSummary written to 'analysis_summary.txt'")
