from urllib.request import urlopen
import json
import pandas as pd 
from datetime import datetime

### GETTING THE DATA

def get_data(url):
    """Returns the JSON response from the url"""
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def get_df(data_json):
    """Returns a DataFrame from the JSON response"""
    df = pd.DataFrame(data_json['hourly'])
    df.set_index('time', inplace=True)
    return df

def weather_data(url):
    """Returns a DataFrame from the JSON response"""
    data_json = get_data(url)
    df = get_df(data_json)
    return df

### FORMATTING FUNCTIONS

def format_date(date, type = 'day'):
    """Formats the date from the JSON response into a readable format"""
    formatted_date = None

    if type == 'day':
        datetime_day = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        formatted_date = datetime_day.strftime("%B %d, %Y")
    elif type == 'hour':
        datetime_hour = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        formatted_date = datetime_hour.strftime("%I:%M %p")
    else:
        print("Wrong type of date")
    
    return formatted_date

def get_dict(df, columns):
    """Returns a dictionary with the min and max values for each column"""
    return {
        col: 
        [[df[col].idxmin(), df[col].min()], # min time of value and min value
         [df[col].idxmax(), df[col].max()]] # max time of value and max value
        for col in columns
    }

### MESSAGE FUNCTIONS

def uv_message(dictionary):
    """Returns the max UV index"""
    max_uv_index = dictionary['uv_index'][1][1]

    if max_uv_index > 10:
        uv_message = "☀️ 🔴 Extreme UV Index ({})".format(max_uv_index)
    elif max_uv_index > 7:
        uv_message = "☀️ 🟠 Very High UV Index ({})".format(max_uv_index)
    elif max_uv_index > 5:
        uv_message = "☀️ 🟡 High UV Index ({})".format(max_uv_index)
    elif max_uv_index > 2:
        uv_message = "☀️ 🟢 Moderate UV Index ({})".format(max_uv_index)
    else:
        uv_message = "☀️ 🔵 Low UV Index ({})".format(max_uv_index)
    
    return uv_message

def wind_message(dictionary):

    """Returns the max wind speed"""
    max_wind_speed = dictionary['windspeed_10m'][1][1]

    if max_wind_speed > 63:
        wind_message = "💨 🔴 Storm-Hurricane force ({} mph)".format(max_wind_speed)
    elif max_wind_speed > 47:
        wind_message = "💨 🟠 Strong Gale ({} mph)".format(max_wind_speed)
    elif max_wind_speed > 31:
        wind_message = "💨 🟡 Near Gale ({} mph)".format(max_wind_speed)
    elif max_wind_speed > 24:
        wind_message = "💨 🟢 Strong Breeze ({} mph)".format(max_wind_speed)
    elif max_wind_speed > 12:
        wind_message = "💨 🔵 Moderate/Fresh Breeze ({} mph)".format(max_wind_speed)
    else:
        wind_message = "💨 ⚪️ Light Breeze ({} mph)".format(max_wind_speed)

    return wind_message

def fog_message(df):
    """Returns the fog probability"""
    fog = "🌫️ Fog expected!" if ((45 or 48) in df['weathercode']) else "🌤️ No fog today!"
    return fog

def rain_message(dictionary):
    """Returns the rain probability"""
    rain_probability = dictionary['precipitation_probability'][1][1]
    
    rain_message = "🌧️ Rain probability: {}%.".format(rain_probability) if rain_probability > 0 else "🌤️ No rain today!"

    return rain_message

def temperature_message(dictionary):
    """Returns the min and max temperatures"""
    min_temp = dictionary['temperature_2m'][0][1]
    max_temp = dictionary['temperature_2m'][1][1]
    time_of_max_temp = format_date(dictionary['temperature_2m'][1][0], type='hour')

    temperature_message = "🌡️ Temperatures: From {}°F to {}°F (at {})".format(min_temp, max_temp, time_of_max_temp)

    return temperature_message