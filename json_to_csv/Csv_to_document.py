import os
import pandas as pd
import re
import demoji
import string


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


name = ['All_combined_Irish', 'All_combined_Irish_stopwords_removed']
for n in name:
    df = pd.read_csv("csv_files/Irish/" + n + ".csv")
    num = 0

    for index, row in df.iterrows():
        file_name = n + "_docs/" + str(num) + ".csv"
        with open(file_name, "w") as file:

            # remove hyperlinks
            temp = re.sub(r'http[s]?://\S+', '', str(row['content']))

            # remove language other than english and emojis.
            temp2 = ''
            for i in temp:
                if is_english(i):
                    temp2 += i

            # remove tagged usernames of people
            temp3 = re.sub(r'@\S+', '', temp2)

            # check if text is empty or have only whitespaces or characters other than alphabets
            temp4 = temp3.translate({ord(x): None for x in string.whitespace})
            temp5 = re.search('[a-zA-Z]', temp4)
            if temp5 and len(temp4) > 6:
                file.write(temp3)
                num += 1
                file.close()
        if not temp5:
            os.remove(file_name)
        del temp5
