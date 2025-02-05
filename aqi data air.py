import pandas as pd
import xml.etree.ElementTree as ET
from snowflake.connector import connect

# Load XML file
xml_file = 'C:/Users/AJAY/Desktop/Guvi/air_dataset/data_aqi_cpcb.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Lists to store extracted data
raw_data = []
dim_city = []
dim_date = []
dim_pollutant = set()
dim_station = []
fact_data = []

# Parse XML and extract relevant information
for country in root.findall('Country'):
    for state in country.findall('State'):
        state_name = state.get('id')
        for city in state.findall('City'):
            city_name = city.get('id')
            for station in city.findall('Station'):
                station_name = station.get('id')
                last_update = station.get('lastupdate')
                latitude = station.get('latitude')
                longitude = station.get('longitude')
                
                # Extract date components
                day, month, year = last_update.split(' ')[0].split('-')
                date_id = f"{year}-{month}-{day}"
                dim_date.append((date_id, day, month, year))
                
                # Add station details
                dim_station.append((station_name, city_name, latitude, longitude))
                
                # Process pollutants
                for pollutant in station.findall('Pollutant_Index'):
                    pollutant_name = pollutant.get('id')
                    min_value = pollutant.get('Min')
                    max_value = pollutant.get('Max')
                    avg_value = pollutant.get('Avg')
                    dim_pollutant.add(pollutant_name)
                    
                    raw_data.append((station_name, date_id, pollutant_name, min_value, max_value, avg_value))
                
                # Process AQI value
                aqi_element = station.find('Air_Quality_Index')
                if aqi_element is not None:
                    aqi_value = aqi_element.get('Value')
                    predominant_pollutant = aqi_element.get('Predominant_Parameter')
                    fact_data.append((station_name, date_id, aqi_value, predominant_pollutant))

# Create DataFrames
raw_aqi_df = pd.DataFrame(raw_data, columns=['station_name', 'date_id', 'pollutant', 'min_value', 'max_value', 'avg_value'])
dim_city_df = pd.DataFrame(dim_city, columns=['city_name', 'state_name'])
dim_date_df = pd.DataFrame(dim_date, columns=['date_id', 'day', 'month', 'year']).drop_duplicates()
dim_pollutant_df = pd.DataFrame(list(dim_pollutant), columns=['pollutant_name'])
dim_station_df = pd.DataFrame(dim_station, columns=['station_name', 'city_name', 'latitude', 'longitude']).drop_duplicates()
fact_aqi_df = pd.DataFrame(fact_data, columns=['station_name', 'date_id', 'aqi_value', 'predominant_pollutant'])

# Snowflake Connection Details
conn = connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

# Upload data to Snowflake
def upload_to_snowflake(df, table_name):
    cursor = conn.cursor()
    for _, row in df.iterrows():
        values = tuple(row)
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(query, values)
    cursor.close()
    conn.commit()

upload_to_snowflake(raw_aqi_df, 'RAW_AQI_DATA')
upload_to_snowflake(dim_city_df, 'DIM_CITY')
upload_to_snowflake(dim_date_df, 'DIM_DATE')
upload_to_snowflake(dim_pollutant_df, 'DIM_POLLUTANT')
upload_to_snowflake(dim_station_df, 'DIM_STATION')
upload_to_snowflake(fact_aqi_df, 'FACT_AQI_MEASUREMENTS')

print("Data uploaded to Snowflake successfully.")
