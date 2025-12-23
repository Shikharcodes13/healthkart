# Growth Accounting Assignment - Deliverables

## Part 1: Growth Accounting Calculation & Visualization ✅

### Files Generated:
1. **growth_accounting_results.csv** - Complete weekly metrics for all 56 weeks
2. **Weekly_Growth_Accounting_Chart.png** - Main visualization showing New, Resurrected, Retained, and Churned users
3. **growth_accounting_charts.png** - Comprehensive dashboard with 4 charts:
   - Weekly Growth Accounting Chart
   - WAU Trend
   - Quick Ratio Trend
   - Retention Rate Trend

### Key Metrics Calculated:
- **WAU (Weekly Active Users)** for each week
- **New Users** (first-time active)
- **Retained Users** (active in both previous and current week)
- **Churned Users** (active in previous week, not in current)
- **Resurrected Users** (returned after being inactive)
- **Quick Ratio** = (New + Resurrected) / Churned
- **Retention Rate** = Retained / Previous Week WAU

### Summary Statistics:
- Average WAU: 3,078 users
- Average New Users/week: 568
- Average Retained Users/week: 2,187
- Average Churned Users/week: 825
- Average Resurrected Users/week: 323
- Average Quick Ratio: 1.06
- Average Retention Rate: 72.3%

## Part 2: Business Insight & Analysis ✅

### File Generated:
- **business_insights.md** - Comprehensive analysis (286 words)

### Key Findings:
1. **Growth Trajectory**: 110% overall growth (1,759 to 3,696 WAU) but with high volatility
2. **Key Drivers**: Strong retention (72.3%) but high churn (825/week) creates fragile growth
3. **Recommendation**: Primary focus on retention & churn reduction; secondary focus on stabilizing acquisition

## Methodology Applied

The analysis follows the Growth Accounting framework from the article:
- **WAU(t) = new(t) + retained(t) + resurrected(t)**
- **WAU(t) – WAU(t-1) = new(t) + resurrected(t) – churned(t)**
- **Quick Ratio** to assess growth sustainability
- **Retention Rate** to measure product-market fit

## Files in This Deliverable:
1. `growth_accounting.py` - Main analysis script
2. `create_main_chart.py` - Visualization script
3. `growth_accounting_results.csv` - Complete data
4. `Weekly_Growth_Accounting_Chart.png` - Main chart
5. `growth_accounting_charts.png` - Dashboard
6. `business_insights.md` - Business analysis


