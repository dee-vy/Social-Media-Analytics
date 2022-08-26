from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import pandas as pd
import numpy as np

nltk.download('vader_lexicon')
import matplotlib.pyplot as plt
import seaborn as sns

path = "json_to_csv/Matrix_Data/tokenFile2.txt"
df = pd.read_csv(path)

senIA = SentimentIntensityAnalyzer()


def get_emotion(s: str) -> bool:
    emotion = senIA.polarity_scores(s)

    if emotion["neg"] == 1.0:
        return "Negative"
    elif emotion["neu"] == 1.0:
        return "Neutral"
    elif emotion["pos"] == 1.0:
        return "Positive"


def get_word_type(s: str) -> bool:
    word_type_tuple = nltk.pos_tag([s])
    word_type = word_type_tuple[0][1]
    if word_type == "JJ":
        return "Adjective"
    elif word_type == "NN":
        return "Noun"
    else:
        return "Other"


df["emotion"] = df.word.apply(lambda x: get_emotion(x))
df["word_type"] = df.word.apply(lambda x: get_word_type(x))

# df.to_csv("/json_to_csv/Matrix_Data/tokenFile2_em_wtype.csv")

# df = df[(df.emotion.isin(["Positive", "Negative"]))]
# df = df[(df.word_type.isin(["Adjective", "Noun"]))]

sns.scatterplot(df.V1, df.V3, hue=df.emotion, s=80)
# plt.show()

sns.scatterplot(df.V1, df.V3, hue=df.word_type, palette=["Maroon", "Green", "Black"], s=20)  # , alpha=0.2
plt.show()

df_v5 = df[["word", "V5", "emotion", "word_type"]]
df_v5_top = df_v5.sort_values('V5', ascending=False).head(30)
print(df_v5_top)

df_v1 = df[["word", "V1", "emotion", "word_type"]]
df_v1_top = df_v1.sort_values('V1', ascending=False).head(50)
print(df_v1_top)

print(df.head(10))
