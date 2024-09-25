import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Group by 'num' and count occurrences
    single_number_df = my_numbers.groupby('num').size().reset_index(name='count')
    
    # Step 2: Filter numbers that appear exactly once
    single_number_df = single_number_df[single_number_df['count'] == 1]['num']
    
    # Step 3: Find the maximum number
    max_single_number = single_number_df.max()
    
    # Step 4: Return the result as a DataFrame
    return pd.DataFrame({'num': [max_single_number]})