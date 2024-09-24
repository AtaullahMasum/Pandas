# leetcode 1070. Product Sales Analysis III Solution using pandas
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the first year (minimum year) for each product
    first_year_df = sales.groupby('product_id')['year'].min().reset_index()

    # Step 2: Merge this result with the original DataFrame to get quantity and price
    result = pd.merge(first_year_df, sales, on=['product_id', 'year'], how='inner')

    # Step 3: Rename columns for clarity
    result = result.rename(columns={'year': 'first_year'})
    result = result[['product_id', 'first_year', 'quantity', 'price']]
    return result