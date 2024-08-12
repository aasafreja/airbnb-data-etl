import pandas as pd
import numpy as np  

# Load the data
file_path = 'airbnb_data_clean.csv' 
data = pd.read_csv(file_path)

# Initialize a dictionary to hold our summaries
summary = {}

# Loop through each row in the DataFrame
for index, row in data.iterrows():
    key = (row['neighbourhood_group'], row['room_type'])
    if key not in summary:
        summary[key] = {
            'prices': [],
            'total_minimum_nights': 0,
            'count': 0,
            'total_availability': 0,
            'total_reviews': 0,
            'unique_hosts': set()
        }


    # Update the summaries with this row's data
    summary[key]['prices'].append(row['price'])
    summary[key]['total_minimum_nights'] += row['minimum_nights']
    summary[key]['total_availability'] += row['availability_365']
    summary[key]['total_reviews'] += row['number_of_reviews']
    summary[key]['unique_hosts'].add(row['host_id'])
    summary[key]['count'] += 1

# Convert the summary dictionary to a format suitable for DataFrame construction
summary_for_df = []
for (neighbourhood_group, room_type), stats in summary.items():
    average_availability = stats['total_availability'] / stats['count']
    summary_for_df.append({
        'neighbourhood_group': neighbourhood_group,
        'room_type': room_type,
        'average_price': np.mean(stats['prices']),
        'median_price': np.median(stats['prices']),
        'count': stats['count'],
        'average_minimum_nights': stats['total_minimum_nights'] / stats['count'],
        'average_availability': average_availability,
        'occupancy_rate': 100 * (365 - average_availability) / 365,
        'total_reviews': stats['total_reviews'],
        'unique_hosts': len(stats['unique_hosts'])
    })

# Convert summary information into a DataFrame
summary_df = pd.DataFrame(summary_for_df)

# Save the summary to a new CSV file
summary_file_path = 'airbnb_summary.csv'  
summary_df.to_csv(summary_file_path, index=False)

print(f"Summary data saved to: {summary_file_path}")