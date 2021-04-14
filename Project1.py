import re
import requests
import json

request = requests.get(url="https://www.timeanddate.com/weather/uk/london/historic")
init_data_js = re.findall(re.compile(r"var data=.*?}}};"), request.text)[0]
init_data_json = json.loads(init_data_js.lstrip("var data=").rstrip(";"))

weather_data_json = init_data_json['detail']

print(weather_data_json)

# file = open("request_file.html", 'w', encoding="utf-8")
# file.write(request.text)
# file.close()
