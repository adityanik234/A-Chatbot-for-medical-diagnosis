import random
import pandas as pd
from chatbot.symptomExtractor import fasttextEmbeddings
from chatbot.symptomExtractor import similarityCheck

# Getting the symptom meanings
meanings = pd.read_csv('chatbot/data/meanings.csv', header=None)
meanings = meanings.set_index(meanings[0], drop=True)


def questionGenerator1(disease_hypothesis_list, extracted_symptoms, disease_dict, random_symptom_list, words):
    """'
    Function that generates the questions

    '"""

    # Global variables defined the chatbot function file
    global random_symptom, meanings

    # Creating a set of all the symptoms associated with the top 4 most probable diseases
    # Usage of the set function helps eliminate duplicates
    associated_symptoms = set([])
    associated_symptoms = associated_symptoms.union(list(disease_dict[disease_hypothesis_list[0]]),
                                                    list(disease_dict[disease_hypothesis_list[1]]),
                                                    list(disease_dict[disease_hypothesis_list[2]]),
                                                    list(disease_dict[disease_hypothesis_list[3]]))

    # set of all the positive symptoms detected previously through NER or through QA
    detected_symptoms = set(extracted_symptoms)

    # Now we need to select a random symptom from the detected symptoms set to ask the patient about it
    # the random_symptom_list contains all the symptoms about which questions have been previously asked
    # to_check represents the set of symptoms about which questions need to be asked
    to_check = associated_symptoms - detected_symptoms - set(random_symptom_list)

    # Select a random symptom from to_check
    random_symptom = random.choice(list(to_check))

    # Store the randomly selected symptom in a list so that we dont ask the same questions again
    random_symptom_list.append(random_symptom)

    # Return the question
    return 'Are you having any ' + str(random_symptom) + '? ' +str((meanings.loc[random_symptom][1]))


def questionGenerator2(reply, extracted_symptoms, random_symptom_list, words):
    if reply == 'yes' or reply == 'no':
        global random_symptom
        if reply == 'yes':
            extracted_symptoms.append(random_symptom)
        else:
            pass
    else:
        reply_emb = fasttextEmbeddings(reply, words).astype('float32')
        y_embedding = fasttextEmbeddings('yes', words).astype('float32')
        n_embedding = fasttextEmbeddings('no', words).astype('float32')
        cosy = similarityCheck(reply_emb, y_embedding)
        cosn = similarityCheck(reply_emb, n_embedding)
        if cosy > cosn:
            extracted_symptoms.append(random_symptom)
        else:
            pass
    return extracted_symptoms, random_symptom_list
