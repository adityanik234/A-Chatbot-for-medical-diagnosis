import pandas as pd
import csv
words = pd.read_table('chatbot/data/glove.840B.300d.txt', sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)


def GloVeEmbeddings(words):
    # List containing all the embeddings for each word in the sentence
    emb_arr = []
    # Representing the embeddings by taking the mean of each in case its
    for word in words.index:
        print(word, words.loc[word])
        break

GloVeEmbeddings(words)