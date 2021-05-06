import re
import requests
import json

import pandas as pd

request = requests.get(url="https://www.timeanddate.com/weather/uk/london/historic")  # Load data from target url
init_data_js = re.findall(re.compile(r"var data=.*?}}};"), request.text)[0]  # Get data from script
init_data_json = json.loads(init_data_js.lstrip("var data=").rstrip(";"))  # Format the data into json form

weather_json = init_data_json['detail']  # Get detailed weather data as json form
weather_dataframe = pd.DataFrame.from_dict(weather_json)  # Switch the form of the weather data into DataFrame
print(weather_dataframe)  # print result

# weather_dataframe.to_csv("weather.csv", encoding="utf_8_sig")  # Output .csv file

# with open("init_data.json", 'w') as file:
#     json.dump(init_data_json, file)

# file = open("request_file.html", 'w', encoding="utf-8")
# file.write(request.text)
# file.close()
