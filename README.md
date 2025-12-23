# Healthkart Growth Accounting Analysis

A comprehensive growth accounting analysis project that evaluates user growth patterns, retention metrics, and provides data-driven business insights for Healthkart over a 56-week period.

## 📋 Project Overview

This project implements the **Growth Accounting Framework** to analyze weekly active user (WAU) patterns, identifying key growth drivers including new user acquisition, retention, churn, and user resurrection. The analysis provides actionable insights for sustainable growth strategies.

## 🎯 Key Objectives

- Calculate weekly growth accounting metrics (New, Retained, Churned, Resurrected users)
- Visualize growth trends and patterns over 56 weeks
- Generate business insights and data-backed recommendations
- Assess growth sustainability using Quick Ratio and Retention Rate metrics

## 📁 Project Structure

```
Healthkart/
│
├── Active Users Data - Internship Round 1 Assignment Healthkart.xlsx  # Input data file
│
├── Python Scripts/
│   ├── understand_structure.py      # Data structure exploration script
│   ├── analyze_dataset.py           # Dataset analysis and insights
│   ├── growth_accounting.py         # Main growth accounting calculation script
│   └── create_main_chart.py         # Visualization generation script
│
├── Output Files/
│   ├── growth_accounting_results.csv              # Complete weekly metrics (CSV)
│   ├── Weekly_Growth_Accounting_Chart.png         # Main growth accounting visualization
│   └── growth_accounting_charts.png               # Comprehensive dashboard (4 charts)
│
└── Documentation/
    ├── README.md                    # This file
    ├── ASSIGNMENT_DELIVERABLES.md   # Assignment deliverables summary
    └── business_insights.md         # Detailed business analysis and recommendations
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - `pandas` - Data manipulation and analysis
  - `numpy` - Numerical computations
  - `matplotlib` - Data visualization
  - `seaborn` - Statistical data visualization
  - `openpyxl` - Excel file reading support

### Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

Or create a `requirements.txt` and install:

```bash
pip install -r requirements.txt
```

### Running the Analysis

#### Step 1: Understand the Data Structure
```bash
python understand_structure.py
```
This script explores the dataset structure and provides initial insights.

#### Step 2: Run Growth Accounting Analysis
```bash
python growth_accounting.py
```
This is the main script that:
- Reads the Excel data file
- Calculates weekly growth accounting metrics
- Generates summary statistics
- Creates the comprehensive dashboard (`growth_accounting_charts.png`)
- Saves results to `growth_accounting_results.csv`

#### Step 3: Create Main Visualization
```bash
python create_main_chart.py
```
Generates the main growth accounting chart (`Weekly_Growth_Accounting_Chart.png`).

## 📊 Key Metrics Calculated

### Growth Accounting Components
- **WAU (Weekly Active Users)**: Total unique users active in each week
- **New Users**: First-time active users in the current week
- **Retained Users**: Users active in both previous and current week
- **Churned Users**: Users active in previous week but not in current week
- **Resurrected Users**: Users who returned after being inactive

### Derived Metrics
- **Quick Ratio**: `(New + Resurrected) / Churned` - Measures growth sustainability
  - > 1.0: Growth is sustainable
  - < 1.0: Declining user base
- **Retention Rate**: `Retained / Previous Week WAU` - Measures product-market fit

### Growth Accounting Formula
```
WAU(t) = new(t) + retained(t) + resurrected(t)
WAU(t) – WAU(t-1) = new(t) + resurrected(t) – churned(t)
```

## 📈 Summary Statistics

Based on 56 weeks of data:

| Metric | Average Value |
|--------|---------------|
| Weekly Active Users (WAU) | 3,078 users |
| New Users per week | 568 users |
| Retained Users per week | 2,187 users |
| Churned Users per week | 825 users |
| Resurrected Users per week | 323 users |
| Quick Ratio | 1.06 |
| Retention Rate | 72.3% |

## 🔍 Key Findings

### Growth Trajectory
- **110% overall growth** (1,759 to 3,696 WAU) over 56 weeks
- Peak WAU: 4,014 users (Week 41)
- Growth marked by volatility with significant fluctuations

### Growth Drivers

**Positive Drivers:**
- Strong retention rate (72.3%) indicating solid product-market fit
- Effective re-engagement (323 resurrected users/week average)
- Sustained growth periods (Weeks 34-41)

**Challenges:**
- High churn rate (825 users/week, ~27% of average WAU)
- Fragile Quick Ratio (1.06 average, with 22 weeks below 1.0)
- Acquisition-churn imbalance requiring constant high acquisition

### Business Recommendations

1. **Primary Focus: Retention & Churn Reduction**
   - Conduct cohort analysis to identify churn patterns
   - Optimize onboarding to improve retention beyond 72.3%
   - Scale win-back campaigns leveraging successful resurrection

2. **Secondary Focus: Stabilize Acquisition**
   - Identify successful channels from high-performing weeks
   - Build sustainable acquisition funnels
   - Focus on quality over quantity in user acquisition

For detailed analysis, see [`business_insights.md`](business_insights.md).

## 📄 Output Files

### `growth_accounting_results.csv`
Complete weekly metrics for all 56 weeks including:
- Week number and label
- WAU, New, Retained, Churned, Resurrected counts
- Quick Ratio and Retention Rate
- Net Growth

### `Weekly_Growth_Accounting_Chart.png`
Main visualization showing stacked bars for:
- New Users (green)
- Resurrected Users (blue)
- Retained Users (purple)
- Churned Users (red, shown below zero line)

### `growth_accounting_charts.png`
Comprehensive dashboard with 4 charts:
1. Weekly Growth Accounting Chart
2. WAU Trend over time
3. Quick Ratio Trend with break-even line
4. Retention Rate Trend

## 🛠️ Scripts Description

### `understand_structure.py`
Explores the dataset structure, validates data format, and provides initial insights about user activity patterns.

### `analyze_dataset.py`
Performs dataset analysis including:
- Dataset structure overview
- Weekly Active Users calculation
- Summary statistics

### `growth_accounting.py`
Main analysis script that:
- Implements the growth accounting framework
- Calculates all weekly metrics
- Generates visualizations
- Exports results to CSV

### `create_main_chart.py`
Creates the primary growth accounting visualization with enhanced formatting and styling.

## 📚 Methodology

This analysis follows the **Growth Accounting Framework** methodology, which breaks down user growth into its fundamental components:

1. **New Users**: First-time active users
2. **Retained Users**: Users who continue to be active
3. **Churned Users**: Users who stopped being active
4. **Resurrected Users**: Users who returned after inactivity

The framework helps identify:
- Whether growth is sustainable (Quick Ratio)
- Product-market fit strength (Retention Rate)
- Growth drivers and constraints
- Areas requiring immediate attention

## 🤝 Contributing

This is an assignment project. For questions or improvements, please refer to the assignment guidelines.

## 📝 License

This project is part of an internship assignment for Healthkart.

## 📧 Contact

For questions about this analysis, please refer to the assignment deliverables document.

---

**Last Updated**: Based on 56 weeks of user activity data  
**Analysis Period**: Weeks 1-56  
**Framework**: Growth Accounting Methodology
