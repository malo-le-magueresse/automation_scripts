### DATA URL
URL = "https://api.open-meteo.com/v1/forecast?latitude=37.76053&longitude=-122.50777&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation_probability,rain,weathercode,windspeed_10m,winddirection_10m,uv_index&temperature_unit=fahrenheit&windspeed_unit=mph&timezone=America%2FLos_Angeles&forecast_days=1"

#### CONSTANTS
DB_PATH = '/Users/mlmg/Library/Messages/chat.db' # The file where iMessages are stored
RECIPIENT_NUMBERS = ['+33649655508', '+14152032094'] # The numbers we want to automate the sending of messages to
SCRIPT_PATH = "/Users/mlmg/src/python_projects/automation_scripts/imessage/sendMessage.applescript" # The path to the AppleScript file that actually sends the message
