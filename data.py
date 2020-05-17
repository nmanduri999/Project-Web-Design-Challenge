import pandas as pd

#create dataframe
city_df = "Resources/cities.csv"
city_df = pd.read_csv(city_df)
city_df = city_df.set_index('City_ID')

#render dataframe as html
html = city_df.to_html()

#write html to file
text_file = open("data.html", "w")
text_file.write(html)
text_file.close()