import pandas as pd

data=pd.read_csv("Resources/cities.csv")

weather_data=data.set_index("City_ID")

weather_data.to_html('raw_data.html')