# Two Inputs:
# List of books and list of keyphrases
import json
import re
import sys
import pandas as pd
import numpy as np

# open and load sample_book_data.json to dictionary
with open(sys.argv[1], "r") as booklist:
    booklistJson = json.load(booklist)

# open and load sample_genre_keyword_value.csv to pandas dataframe
with open(sys.argv[2], "r") as keyphrases:
    df = pd.read_csv(keyphrases, skipinitialspace=True)

# sort the book list
sorted_booklist = []
for bookname in booklistJson:
    sorted_booklist.append(bookname["title"])
    sorted_booklist = sorted(sorted_booklist)

def returnTotalScores():
    # outside loop iterating sorted booklist
    for bookname in sorted_booklist:
        # inner loop iterating unsorted json
        for book in booklistJson:
            if bookname == book["title"]:
                dict = parseKeyphrases(book)
                #print(dict)
                genrescores_dict = returnGenreScores(dict)
                print(bookname)
                # iterate dict
                for key,value in genrescores_dict.items():
                    # convert dtypes and print final output
                    gen = str(key)
                    score = str(int(value))
                    print(gen+",",score)
                # newline for each book
                print()

def parseKeyphrases(book):
    # define results dict
    dict = {}
    # iterrate pandas dataframe, appending matches
    for keywordItem in df.itertuples():
        # get genre
        genre = keywordItem.Genre
        # use re module to find all instances of keyphrase in description ignoring case
        matches = re.findall(keywordItem.Keyword, book["description"])
        # check if dict contains value
        if genre in dict and len(matches) > 0:
            dict[genre].append(matches)
        elif len(matches) > 0:
            dict[genre] = matches
        else:
            pass
    # iterate dict, flattening lists
    for key, value in dict.items():
        # lambda function to flatten list
        flatten_list = lambda value:[element for item in value for element in flatten_list(item)] if type(value) is list else [value]
        flat = flatten_list(value)
        dict[key] = flat
    return dict
    # iterate dict, printing output

def returnGenreScores(input_dict):
    # define return dict
    return_dict = {}
    for key, value in input_dict.items():
        # n-value
        n = len(value)

        x = np.array(value)
        unique_keywords = np.unique(x)
        #print(key, unique_keywords)

        points = 0
        # get point values from value
        for keyword in unique_keywords:
            # subset dataframe based on matching conditions
            df_filtered = df[((df['Keyword'] == keyword) & (df['Genre'] == key))]
            #print("Point value", df_filtered['Points'].values)
            points += int(df_filtered['Points'].values)
        kw_length = len(unique_keywords)
        # calculate k-value
        k = points/kw_length
        genrescore = n*k
        # set value of return dict
        return_dict[key] = genrescore

    # cleaning: sort the dict by descending score lambda returning each key and sorting with sorted method
    sorted_dict = dict(sorted(return_dict.items(),
                              key=lambda item: item[1],
                              reverse=True))

    # cleaning: slice dict to only top 3 scores
    sliced_dict = dict(list(sorted_dict.items())[0: 3])

    return sliced_dict

if __name__ == '__main__':
    returnTotalScores()


