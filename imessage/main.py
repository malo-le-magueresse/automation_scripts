# Our own modules
from constants import *
from utils import * 

# Other Python modules
import os
from urllib.request import urlopen
import json
import pandas as pd 
from datetime import datetime

### GETTING THE DATA
df = weather_data(URL)
dictionary = get_dict(df, df.columns)
day = format_date(df.index[0], type='day')

### FORMATTING THE MESSAGE
temperature, rain, uv, wind, fog = temperature_message(dictionary), rain_message(dictionary), uv_message(dictionary), wind_message(dictionary), fog_message(dictionary)

MESSAGE = """ 'SF Weather report for {}
{}
{}
{}
{}
{}'    
""".format(day, temperature, rain, uv, wind, fog)

# Printing the message for debugging purposes
print(MESSAGE)
print(dictionary)

# Sending the message to all the recipients
for RECIPIENT_NUMBER in RECIPIENT_NUMBERS:
    os.system('osascript "{}" {} {}'.format(SCRIPT_PATH, RECIPIENT_NUMBER, MESSAGE))