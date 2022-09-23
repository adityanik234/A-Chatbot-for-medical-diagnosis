import requests
import tensorflow as tf
import pandas as pd
import numpy as np
import string
import csv
from string import digits


# Function definition for extracting terms that represent symptoms
def symptomExtract(text, out, type):
    """
    This function is used to extract the symptom entities from the output of the BERN (Bio-BERT) API
    :param text: Input text from  the user
    :param out: output from the BERN (Bio-BERT) API
    :param type: The entity type, in our case it is 'disease' as this label contains all the symptom/disease entities
    :return: Extracted symptoms
    """
    denotations = out['denotations']
    symptoms = []

    if type == 'disease':
        symptom_terms = []
        for i in denotations:
            if i['obj'] == 'disease':
                symptom_terms.append((i['span']['begin'], i['span']['end']))

        for i in symptom_terms:
            start = i[0]
            end = i[1]
            symptoms.append(text[start:end])

    return symptoms


# Bio BERT
def rawTextQuery(text, url="https://bern.korea.ac.kr/plain"):
    return requests.post(url, verify=False, data={'sample_text': text}).json()


# Function definition for checking the cosine similarity between two embedding vectors
def similarityCheck(emb1, emb2):
    # Normalising both vectors
    normalize_emb1 = tf.nn.l2_normalize(emb1, 0)
    normalize_emb2 = tf.nn.l2_normalize(emb2, 0)
    # Calculating cos similarity
    cos_similarity = tf.reduce_sum(tf.multiply(normalize_emb1, normalize_emb2))
    return cos_similarity


# Function definition for generating GloVe embeddings
def fasttextEmbeddings(symptom_word, words):
    # List containing all the embeddings for each word in the sentence
    emb_arr = []
    # Representing the embeddings by taking the mean of each in case its
    for word in symptom_word.split():
        emb_arr.append(words.wv[word])  # .to_numpy())
        # emb_arr.append(words.wv[word])
    emb_arr = np.array(emb_arr)
    fin_emb = np.mean(emb_arr, axis=0)
    return fin_emb


def posSymptomExtraction(text, symptom_corpus, symptom_embeddings, words):
    out = rawTextQuery(text)
    extracted_symptoms = symptomExtract(text, out, 'disease')
    # Calculating the most similar words
    for i in range(len(extracted_symptoms)):
        if extracted_symptoms[i] in symptom_corpus:
            pass
        else:
            emb = fasttextEmbeddings(extracted_symptoms[i], words).astype('float32')
            cos_list = []
            for symptom in symptom_corpus:
                cos = similarityCheck(emb, symptom_embeddings[symptom].to_numpy().astype('float32'))
                cos_list.append(cos)

            extracted_symptoms[i] = symptom_corpus[np.argmax(np.array(cos_list))]

    return extracted_symptoms
