import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['nums_1'] = logs['num'].shift(1)
    logs['nums_2'] = logs['num'].shift(2)
    consecutives = logs[((logs['num']==logs['nums_1']) & (logs['num']==logs['nums_2']))]
    result_df = consecutives[['num']].drop_duplicates().rename(columns={'num':'ConsecutiveNums'})
    return result_df
    