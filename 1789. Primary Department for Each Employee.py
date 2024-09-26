# leetcode 1789. Primary Department for Each Employee
import pandas as pd

def find_primary_department(employee_df: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Condition where primary_flag = 'Y'
    primary_df = employee_df[employee_df['primary_flag']=="Y"]
    # Step 2: Group by employee_id and filter those having exactly one department_id
    single_department = employee_df.groupby('employee_id').filter(lambda x: x['department_id'].nunique()==1 )
    # Step 3: Combine the two conditions
    result_df = pd.concat([primary_df, single_department]).drop_duplicates()

    # Step 4: Select only employee_id and department_id columns
    result_df = result_df[['employee_id', 'department_id']]
    
    return result_df