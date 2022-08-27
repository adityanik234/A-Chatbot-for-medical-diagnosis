# Main loop
def first():
    random_symptom_list = []
    text = input('Hello, could you please give me a brief description of your symptoms?\n')

    input_symptoms = posSymptomExtraction(text, symptom_corpus, symptom_embeddings)
    #print('Extracted symptoms ', input_symptoms)

def main_loop():
    for i in range(20):
        if i == 0:
            return input_symptoms
        diseases, input_vector, probs = diseaseHypothesis(input_symptoms, symptom_corpus, X_train, y_train)

        input_symptoms, random_symptom_list = questionGenerator(diseases, input_symptoms, disease_dict, random_symptom_list, words)


        #print('You may be having ', diseases)
        #print('associated probabilities: ', probs)
        if i !=0:
            print('You may be having ', diseases)
            print('associated probabilities: ', probs)
        if probs[0][-1] > 0.90:
            return print('It is very likely that you have ', diseases[-1])
            break


print('Hello, could you please give me a brief description of your symptoms?\n')

def chatbot_response(text):
