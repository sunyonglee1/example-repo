import pandas as pd

df = pd.read_csv('data/final_data.csv')

store_summary = df.groupby('Store_ID').agg(
    total_revenue=('Revenue', 'sum'),
    avg_units_sold=('Units_Sold', 'mean'),
    unique_order_segments=('order_segment', 'unique')
)

median_revenue = df['Revenue'].median()
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1

upper_limit = median_revenue + 1.5 * IQR

outliers = df[df['Revenue'] > upper_limit]

print("Store Summary:")
print(store_summary)

print("\nRevenue Outliers:")
print(outliers)

with open('results/store_summary_and_outliers.txt', 'w') as f:
    f.write("Store Summary:\n")
    f.write(store_summary.to_string())
    
    f.write("\n\nRevenue Outliers:\n")
    f.write(outliers.to_string())