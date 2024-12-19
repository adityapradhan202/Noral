import pandas as pd

def sort_db(df):
    issue_priority = {
        'Caries': 1,
        'Gingivitis': 2,
        'Mouth_ulcer': 3,
        'Hypodontia': 4,
        'Tooth_discoloration': 5
    }
    df_sorted = df.sort_values(by=['CNNRESULT', 'AGE'], key=lambda x: x.map(issue_priority), ascending=[True, False])
    
    return df_sorted