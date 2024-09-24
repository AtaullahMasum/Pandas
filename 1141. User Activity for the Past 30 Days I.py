import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # Define the end date
    end_date = pd.to_datetime('2019-07-27')
    
    # Filter data where the activity_date is within the past 30 days
    filtered_activity = activity[
        (activity['activity_date'] <= end_date) &
        ((end_date -activity['activity_date']) <  pd.Timedelta(days=30))
    ]
    
    # Group by activity_date and count distinct user_id
    result = filtered_activity.groupby('activity_date')['user_id'].nunique().reset_index()
    
    # Rename columns for clarity
    result.columns = ['day', 'active_users']
    
    return result