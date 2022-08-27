import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import pickle
from chatbot.symptomExtractor import fasttextEmbeddings, similarityCheck


def diseaseHypothesis(input_symptoms, symptom_corpus, X_train, y_train, words):
    # Converting the input into a one hot array


    vector_list = []
    for symptom in symptom_corpus:
        if symptom in input_symptoms:
            vector_list.append(1)
        else:
            vector_list.append(0)
    input_vector = np.array(vector_list).reshape(1, -1)

    # Encoding the labels
    le = preprocessing.LabelEncoder()
    le.fit(list(y_train))
    y_train1 = le.transform(list(y_train))

    # initialise the model
    # logistic_model = LogisticRegression(max_iter=80, penalty='l2', solver='lbfgs')
    # Fitting the model to the training data
    # logistic_model.fit(X_train.values, y_train1)

    filename = 'chatbot/finalized_model.sav'
    # pickle.dump(logistic_model, open(filename, 'wb'))

    logistic_model = pickle.load(open(filename, 'rb'))

    # Hypothesis list
    probs = logistic_model.predict_proba(input_vector)
    best_n = np.argsort(probs, axis=1)[:, -4:]

    # Top 3 hypotheses
    hypothesis_list = list(le.inverse_transform(best_n[0]))

    return hypothesis_list, input_vector, probs[0][best_n]
