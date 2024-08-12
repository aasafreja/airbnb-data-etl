import pandas as pd
import numpy as np

def extract(file_path):
    """Load the data from the CSV file."""
    data = pd.read_csv(file_path)
    return data

def transform(data):
    """Transform the data by cleaning and feature engineering."""
    # Data Cleaning
    data.drop_duplicates(subset=['id'], inplace=True)
    data['name'].fillna('Unknown', inplace=True)
    data['host_name'].fillna('Unknown', inplace=True)
    data['reviews_per_month'].fillna(0, inplace=True)

    # Convert data types
    data['last_review'] = pd.to_datetime(data['last_review'])

    # Drop rows where 'availability' is 0
    data = data[data['availability_365'] != 0]

    # Ensure no zero or negative values
    data['price'] = data['price'].apply(lambda x: x if x > 0 else 1) 

    # Extract year, month, and day from 'last_review'
    data['last_review_year'] = data['last_review'].dt.year
    data['last_review_month'] = data['last_review'].dt.month
    data['last_review_day'] = data['last_review'].dt.day

    # Calculate booking rate
    data['booking_rate'] = 1 - (data['availability_365'] / 365)

    return data


# Function to categorize listings by availability into "highly available", "moderately available", and "rarely available"
def categorize_availability(df):
    """
    Categorize listings by availability into 'highly available', 
    'moderately available', and 'rarely available'.
    Add a new column 'availability_category' to the DataFrame.
    """
    def categorize(availability):
        if availability > 300:
            return 'highly available'
        elif availability > 100:
            return 'moderately available'
        else:
            return 'rarely available'
    
    df['availability_category'] = df['availability_365'].apply(categorize)
    return df


# Distance calculation from Grand Central station
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula 
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371  # Radius of earth in kilometers
    distance = c * r
    return round(distance, 2)  

def calculate_distance_to_center(df, center_lat, center_lon):
    """
    Add a column 'distance_to_center' to the DataFrame with the distance 
    from each listing to the city center.
    """
    df['distance_to_center'] = df.apply(
        lambda row: haversine(row['latitude'], row['longitude'], center_lat, center_lon), axis=1)
    return df


def load(data, output_file_path):
    """Save the transformed data to a new CSV file."""
    data.to_csv(output_file_path, index=False)

def main():
    # File paths
    input_file_path = 'airbnb_data_raw.csv'
    output_file_path = 'airbnb_data_clean.csv'
    
    # Extract
    data = extract(input_file_path)
    
    # Transform
    data = transform(data)
    data = categorize_availability(data)
    # Transform - distance
    center_lat, center_lon = 40.7534, -73.9768  # Grand Central station coordinates
    data = calculate_distance_to_center(data, center_lat, center_lon)

    # Sorting the data by distance from center
    data = data.sort_values(by=['distance_to_center', 'price'], ascending=True)
    data = data.reset_index(drop=True)
    data.index += 1
    data.index    

    # Load
    load(data, output_file_path)
    print(f"Transformed data saved to {output_file_path}")

if __name__ == "__main__":
    main()