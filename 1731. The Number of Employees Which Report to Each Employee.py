import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
       #Step 1: Self-merge (join) the DataFrame on employee_id and reports_to
        merged_df = employees.merge(employees, left_on="employee_id", right_on = "reports_to", suffixes =('_manager','_report'))

        # Step 2: Group by manager's employee_id and name, then calculate the count of reports and average age
        grouped_df = merged_df.groupby(['employee_id_manager','name_manager']).agg(
            reports_count = ('employee_id_report','count'),
            average_age = ('age_report', 'mean')
        ).reset_index()
        # Step 3: Round the average age and filter managers with at least 1 report
        grouped_df['average_age'] = grouped_df['average_age'].apply(lambda x: np.ceil(x) if x%1 >= 0.5 else np.floor(x))
        grouped_df = grouped_df[grouped_df['reports_count']>= 1]
        # Step 4: Sort by employee_id in ascending order
        final_result = grouped_df.sort_values(by='employee_id_manager')
        # Correct column selection for the output
        final_result = final_result.rename(columns={
            'employee_id_manager':'employee_id',
            'name_manager':'name'
        })
       
        final_result = final_result[['employee_id','name','reports_count','average_age']]
        return final_result