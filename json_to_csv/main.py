import pandas as pd
import os
import glob

path_to_json = 'json_files/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
# print(json_files)

irish_cities = (
    'ireland', 'dublin', 'galway', 'cork', 'belfast', 'limerick', 'kilkenny', 'killarney', 'kinsale', 'derry',
    'craigavon',
    'waterford', 'drogheda', 'dundalk', 'kildare', 'dun laoghaire', 'cliffs of moher', 'aran islands', 'éire')


def is_irish(name):
    return True if name.lower() in irish_cities else False


i = 0
csv_files = []
df_all = None
for x in json_files:

    # Not using two empty JSONs.
    if x == "Blackhall_Recreation_tweets.json" or x == "Hardwicke_Street_Community_Centre_tweets.json":
        continue
    else:
        df = pd.read_json(path_to_json + x, lines=True)

        # Check for Irish Location.
        for index, row in df.iterrows():
            if is_irish(row['user']['location']):
                continue
            else:
                df.drop(labels=index, axis=0, inplace=True)
        df = df['content']

        # Store Irish tweets in a separate folder as a CSV.
        csv_file = "csv_files/irish/" + x.removesuffix(".json") + ".csv"
        df.to_csv(csv_file)
        if i == 0:
            df_all = df
        else:
            df_all = pd.concat([df_all, df])
        i = 1
        csv_files.append(csv_file)

# Combine all tweets in a single CSV stored in the same folder.
df_all.to_csv("csv_files/irish/All_combined_irish.csv",
              index=False)  # earlier: All_combined_xxx.csv but loc != Ireland.
print(csv_files)
