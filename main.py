import string
import tkinter as tk
from collections import Counter
from tkinter import *

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

root = tk.Tk()
root.title("text box")

def input():
    inputValue = text1.get("1.0","end-1c")
    text2 = inputValue


    lower_case = text2.lower()
    final_text = lower_case.translate(str.maketrans('','',string.punctuation))
    tokenized_words= word_tokenize(final_text,"english")

    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)

    lemmatized_words = []
    for word in final_words:
        word = WordNetLemmatizer().lemmatize(word)
        lemmatized_words.append(word)

    emotion_list =[]
    with open('emotion.txt','r') as file:
        for line in file:
            cleaned_line = line.replace("\n",'').replace(",", '').replace("'", '').strip()
            word,emotion = cleaned_line.split(':')

            if word in lemmatized_words:
                emotion_list.append(emotion)

    print(emotion_list)
    x = Counter(emotion_list)
    print(x)

    def sentiment_analyse(sentiment):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment)
        if score['neg']>score['pos']:
            print("Negative sentiment")
        elif score['neg']<score['pos']:
            print("Positive sentiment")
        else:
            print("Neutral Sentiment")


    sentiment_analyse(final_text)

text1 = tk.Text(root,height = 30,width = 50)
text1.pack()

button1= Button(root ,height=1,width=10,text="enter",command=lambda: input())
button1.pack()
mainloop()



