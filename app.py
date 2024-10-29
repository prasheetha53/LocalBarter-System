from flask import Flask, render_template, request, redirect, url_for, jsonify
from model import chatbotmodel  # Ensure this matches the class name
import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
import random
import matplotlib.pyplot as plt
from autocorrect import Speller
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl','rb'))
tokenizer = Tokenizer(num_words=10000)  # Adjust 'num_words' based on your model
                     
app = Flask(__name__)
spell = Speller()
intents = json.loads(open('Dataset\Dataset.json').read())

model = load_model('chatbot_model.h5')

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"found in bag: {w}")
    return np.array(bag)

lemmatizer = WordNetLemmatizer()

def predict_class(sentence, model):
    p = bow(sentence,words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    print(results)
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        print(return_list)
        print(sentence)
    return return_list

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def getResponse(ints, intents_json):
    if ints:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                return random.choice(i['responses'])
    
    return "Sorry, I didn't understand that. Could you please rephrase?"

def chatbot_response(msg):
    msg = spell(msg)

    res = getResponse(predict_class(msg, model), intents)
    print(f"chatbot_response: {res}")
    
    return res

@app.route("/chat")
def get_bot_response():
    userText = request.args.get('msg')
    if not userText:
        return "Please provide some input."
    
    # Here, implement chatbot_response function to generate a response.
    chatbot_response_text = chatbot_response(userText)  # Your chatbot logic
    return chatbot_response_text

app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("chat.html")

if __name__ == 'main':
    app.run(debug=True)