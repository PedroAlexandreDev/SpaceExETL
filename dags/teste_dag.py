import requests
import pandas as pd

def extract():
    url = "https://api.spacexdata.com/v5/launches/upcoming"

    response = requests.get(url) 

    return response.json()

def transform(data):

    dataFrame = pd.json_normalize(data)

    dataFrame["name"] = dataFrame["name"].fillna("nome desconheciedo")

    dataFrame.drop("static_fire_date_utc", axis=1, inplace=True)
    dataFrame.drop("static_fire_date_unix", axis=1, inplace=True)
    dataFrame.drop("net", axis=1, inplace=True)
    dataFrame.drop("rocket", axis=1, inplace=True)
    dataFrame.drop("success", axis=1, inplace=True)
    dataFrame.drop("links.presskit", axis=1, inplace=True)
    dataFrame.drop("links.webcast", axis=1, inplace=True)
    dataFrame.drop("links.article", axis=1, inplace=True)
    dataFrame.drop("links.wikipedia", axis=1, inplace=True)
    dataFrame.drop("failures", axis=1, inplace=True)
    dataFrame.drop("details", axis=1, inplace=True)
    dataFrame.drop("crew", axis=1, inplace=True)
    dataFrame.drop("links.reddit.media", axis=1, inplace=True)
    dataFrame.drop("links.reddit.recovery", axis=1, inplace=True)
    dataFrame.drop("ships", axis=1, inplace=True)
    dataFrame.drop("capsules", axis=1, inplace=True)
    dataFrame.drop("links.youtube_id", axis=1, inplace=True)
    dataFrame.drop("links.youtube_id", axis=1, inplace=True)
    dataFrame.drop("links.youtube_id", axis=1, inplace=True)
    dataFrame.drop("links.youtube_id", axis=1, inplace=True)






    print(dataFrame)

data = extract()

transform(data=data)




