# Airbnb Data Processing Pipeline

This project provides a data processing pipeline for Airbnb listings. The pipeline extracts raw Airbnb data from a CSV file, transforms it through various cleaning and feature engineering steps, and then saves the processed data into a new CSV file. This pipeline helps to prepare the data for further analysis, such as calculating booking rates, categorizing availability, and determining the distance of listings from a central location.

## Project Structure

- airbnb_data.py: This script handles the entire ETL (Extract, Transform, Load) process for the Airbnb dataset.
- airbnb_summary.py: This script generates summary statistics by region and room type.
- Tableau public vizualisation

## Data Source

The [raw NY Airbnb data](https://www.kaggle.com/datasets/sudhanvahg/new-york-airbnb-bookings) used in this project is sourced from Kaggle. The dataset can be accessed and downloaded from the Kaggle website.

## Project Overview

This project provides a set of functions to:
- Extract data from a CSV file.
- Transform data by cleaning and feature engineering.
- Categorize listings by availability.
- Add columns for reviews per neighborhood and average price per room type.
- Calculate distances from listings to the city center.
- Save the transformed data to a new CSV file.

## Features

- **Data Cleaning**: Handle missing values, convert data types, and filter out rows based on availability.
- **Feature Engineering**: Extract year, month, and day from dates, categorize availability, and compute additional metrics.
- **Distance Calculation**: Calculate the distance of each listing from a specified city center using the Haversine formula.
- **Sorting and Saving**: Sort the data and save it to a new CSV file.

## Output files
- **`airbnb_data_clean.py`**
- **`airbnb_summary.py`**

## Visualisation 

The clean data was used to create [NY Airbnb listing dashboard](https://public.tableau.com/app/profile/anete.asafreja/viz/NYAirbnblistings/Overview) in Tableau Public.


### Prerequisites

- Python 3.x
- Pandas
- NumPy

You can install the required packages using pip:

```bash
pip install pandas numpy
