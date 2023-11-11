import pandas as pd 
import csv

df = pd.read_csv("filtered_stars.csv")

final_stars_list = []
rows = []
stars_data_rows = rows[1:]

for stars_data in stars_data_rows:
    temp_dict = {
        "Name": stars_data[1],
        "Distance": stars_data[2],
        "Mass": stars_data[3],
        "Radius": stars_data[4],
        "Gravity": stars_data[5]
    }
    final_stars_list.append(temp_dict)
    print(final_stars_list)