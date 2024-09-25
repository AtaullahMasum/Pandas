#leetcode 1729 number problem solution added
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    followers_count = followers.groupby('user_id')['follower_id'].count().reset_index()
    followers_count = followers_count.rename(columns={'follower_id':'followers_count'})
    follower_count_sort = followers_count.sort_values(by='user_id')
    return follower_count_sort