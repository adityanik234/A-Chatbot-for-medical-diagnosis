import time

from symptomExtractor import *
from DiseaseHypothesisGenerator import *
from QuestionGenerator import *

# Loading the symptom corpus
df = pd.read_csv(r'data/Training.csv')

# Loading the Glove file
words = pd.read_table('data/glove.840B.300d.txt', sep=" ", index_col=0, header=None, quoting=csv.QUOTE_NONE)
symptom_corpus = list(df.columns)
symptom_corpus = [x.replace('_', ' ') for x in symptom_corpus]
symptom_corpus = [x.translate(str.maketrans('', '', string.punctuation)) for x in symptom_corpus]
symptom_corpus = [x.translate(str.maketrans('', '', string.digits)) for x in symptom_corpus]
training_df = df
training_df.columns = symptom_corpus

# Removing the two symptoms as they do not exist in the Glove file
symptom_corpus.remove('dischromic  patches')
symptom_corpus.remove('toxic look typhos')
symptom_corpus.remove('prognosis')

# Shuffling the data
training_df = training_df.sample(frac=1).reset_index(drop=True)
X_train = training_df.drop(['prognosis', 'dischromic  patches', 'toxic look typhos'], axis = 1)
y_train = training_df['prognosis']

# Loading the embeddings for the symptom corpus
symptom_embeddings = pd.read_csv(r'data/symptom corpus embeddings.csv')

# Getting the disease symptom dictionary
disease_df = pd.read_csv(r'data/Testing.csv')

symptom_corpus1 = list(disease_df.columns)
symptom_corpus1 = [x.replace('_', ' ') for x in symptom_corpus1]
symptom_corpus1 = [x.translate(str.maketrans('', '', string.punctuation)) for x in symptom_corpus1]
symptom_corpus1 = [x.translate(str.maketrans('', '', string.digits)) for x in symptom_corpus1]
disease_df.columns = symptom_corpus1

disease_df = disease_df.drop(['dischromic  patches', 'toxic look typhos'], axis = 1)

new_df = disease_df.T
new_df.columns = disease_df['prognosis']


disease_dict = {}
for disease in new_df.columns:
    disease_dict[disease] = list(new_df[new_df[disease] == 1].index)


# Main loop
random_symptom_list = []
text = input('Hello, could you please give me a brief description of your symptoms?\n')

input_symptoms = posSymptomExtraction(text, symptom_corpus, symptom_embeddings, words)
print('Extracted symptoms ', input_symptoms)

for i in range(20):
    diseases, input_vector, probs = diseaseHypothesis(input_symptoms, symptom_corpus, X_train, y_train)

    input_symptoms, random_symptom_list = questionGenerator(diseases, input_symptoms, disease_dict, random_symptom_list, words)

    print('You may be having ', diseases)
    print('associated probabilities: ', probs)
    if probs[0][-1] > 0.90:
        break

print('It is very likely that you have ', diseases[-1])
