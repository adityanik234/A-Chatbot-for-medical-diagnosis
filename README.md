<img width="689" alt="Screenshot 2022-10-12 at 12 29 33 am" src="https://user-images.githubusercontent.com/95295620/195216828-5b69fcd3-e35b-4e02-baea-a7dd2279656b.png">
<img width="689" alt="Screenshot 2022-10-12 at 12 30 31 am" src="https://user-images.githubusercontent.com/95295620/195216882-747a440e-292d-423d-afaa-14f431a96f30.png">
# A-Chatbot-for-medical-diagnosis
This project involves the use of NLP and Machine learning to develop a chatbot to diagnose patients with certain symptoms.

All jupyter notebooks related to testing and evaluating the various components of the chatbot are in the Evaluation and tesing folder

README

The code consists of two parts:

1. the testing and evaluation notebooks

2. The main chatbot software code

PART 1
The testing and evaluation folder contains 3 jupyter notebooks for the testing and evaluation of the
BERN Bio-Bert model testing and evaluation, Machine learning models testing and evaluation, the question generator and end toend
testing and evaluation

To run the notebooks set the directory of the notebooks to the Tesing and evaluation
notebooks folder

The machine learning testing and evaluation notebook can be run directly as the data files are
present in the folder

for the other notebooks please download the files from the following links and
place it in the Testing and evaluation folder.
These are files for the pre-trained word2vec, Glove and fastext models.
These files are very large ranging from 1.5 gb to about 8 gb in size so it will
take some time to download

Word2vec :https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
place the GoogleNews-vectors-negative300.bin file into the Testing and evaluation notebooks folder

Glove : https://nlp.stanford.edu/data/glove.840B.300d.zip
place the glove.840B.300d.txt file into the Testing and evaluation notebooks folder

Fasttext : https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip
extract and place the crawl-300d-2M-subword.bin file into the Testing and evaluation notebooks folder

Once the Above is done the notebooks can be run
The notebooks are RAM intensive due to the large size of these models so at least
16 GB memory is recommended

PART 2 The code files

The files for the chatbot software are in the chatbot code files folder

First please install the libraries mentioned in the requirements file

Then place the Fasttext model crawl-300d-2M-subword.bin file downloaded from the link given in the previous parts

Place the file into the chatbot code files/medbot/chatbot/data folder

Now run the run.py file in the chatbot code files/medbot folder by setting the medbot folder as the terminal directory

The file will take some time to execute depending on the processing power and RAM

It takes about 40 to 50 seconds to run after which a link will be displayed on the command line like this:  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Paste this link into the browser and press enter

It takes a few seconds again depending on the computer

Once it loads completely the home page will be displayed on the screen

navigate to the cyan sidebar and click on chatbot and chat with the application
