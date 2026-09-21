# Pharmacy Sales & Drug Analysis
**Internship Task 3 — VirtualWorks Lab**
**Submitted by:** Sudesh Ganesh Jagadale

---

## 1. Objective

Analyze pharmacy sales data to identify top-selling medicines and revenue
patterns, evaluate monthly sales growth, and compare branded versus generic
medicines using sales datasets.

## 2. Dataset

A pharmacy sales dataset (`pharmacy_sales_data.csv`) with **1,245 orders**
spanning **6 months (March–August 2026)** across 12 medicines and 9 therapy
categories. Columns:

| Column | Description |
|---|---|
| OrderID | Unique order identifier |
| Date | Order date |
| MedicineName | Medicine sold (branded or generic name) |
| Type | Branded / Generic |
| Category | Therapy category (e.g. Diabetes, Pain Relief) |
| Quantity | Units sold in the order |
| UnitPrice | Price per unit ($) |
| TotalAmount | Order total ($) |

## 3. Key Metrics

| Metric | Value |
|---|---|
| Total Sales | $33,025.50 |
| Total Quantity Sold | 4,546 units |
| Total Orders | 1,245 |
| Average Order Value | $26.53 |

## 4. Top-Selling Medicines

**By revenue**, insulin products dominate — Lantus ($4,004) and generic
Insulin ($3,270) are the top two, followed by Lipitor ($2,420) and
Prilosec ($2,331). This makes sense since insulin has the highest unit
price in the catalog.

**By quantity**, everyday medicines lead — Ibuprofen (277 units),
Calpol/Paracetamol (247 units), and Amlodipine (242 units) are the
most frequently purchased, reflecting common, low-cost conditions.

*(See `top_medicines_revenue.png` for the chart.)*

## 5. Monthly Sales Trend

| Month | Sales ($) | Growth vs Prior Month |
|---|---|---|
| March 2026 | 5,436.0 | — |
| April 2026 | 4,498.0 | -17.3% |
| May 2026 | 6,334.0 | +40.8% |
| June 2026 | 5,447.5 | -14.0% |
| July 2026 | 4,959.0 | -9.0% |
| August 2026 | 6,351.0 | +28.1% |

Sales show a fluctuating, non-linear pattern with peaks in May and August.
There is no strong sustained upward or downward trend over the period —
sales oscillate month to month, suggesting seasonal or order-volume
variability rather than steady growth.

*(See `monthly_sales_trend.png` for the chart.)*

## 6. Branded vs Generic Comparison

| Type | Total Sales | Quantity | Orders | Avg Unit Price | Avg Order Value |
|---|---|---|---|---|---|
| Branded | $19,734.0 | 2,112 | 548 | $9.30 | $36.01 |
| Generic | $13,291.5 | 2,434 | 697 | $5.50 | $19.07 |

- **Branded medicines generate more total revenue** ($19,734 vs $13,291.5) despite fewer orders (548 vs 697), because their unit price is significantly higher.
- **Generic medicines sell in higher quantity** (2,434 vs 2,112 units) and are ordered more frequently — consistent with cost-conscious buying behavior.
- **Average order value is nearly double for branded** ($36.01 vs $19.07), confirming branded purchases contribute disproportionately to revenue.

*(See `branded_vs_generic.png` for the chart.)*

## 7. Sales by Category

Diabetes medicines lead category sales ($9,309.5), driven by high-value
insulin products, followed by Hypertension ($5,316.0) and Gastric ($3,747.0).

## 8. Tools Used

- **Python** with **pandas** for data analysis and **matplotlib** for charts
- Full reproducible script: `sales_analysis.py`

## 9. Files Submitted

- `pharmacy_sales_data.csv` — sales dataset
- `sales_analysis.py` — full analysis script
- `analysis_summary.txt` — analysis output
- `monthly_sales_trend.png` — monthly sales chart
- `top_medicines_revenue.png` — top 10 medicines by revenue chart
- `branded_vs_generic.png` — branded vs generic sales share chart
- `Project_Report.md` — this report
