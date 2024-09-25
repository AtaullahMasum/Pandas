import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_count = product['product_key'].nunique()
    customer_product_count = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    customer_product_count = customer_product_count[customer_product_count['product_key'] == product_count]
    customer_product_count = customer_product_count[['customer_id']]
    return customer_product_count