from scipy import stats

# Örnek veriler
sales_strategy_a = [1000, 1200, 1500, 1100, 1300]
sales_strategy_b = [900, 1100, 1400, 1000, 1200]

# İki strateji arasındaki satış farkının p-değeri
t_statistic, p_value = stats.ttest_ind(sales_strategy_a, sales_strategy_b)

print("P-değeri:", p_value)
