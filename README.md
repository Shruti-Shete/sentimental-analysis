**Project Overview:**

This project is a simple sentiment analysis tool built using Python and the Tkinter library for creating a graphical user interface (GUI). <br />
The goal of the project is to analyze the sentiment of a given text and determine whether it is positive, negative, or neutral.

**Libraries Used:**

*Tkinter:* Used for creating the graphical user interface to input and display text.

*NLTK (Natural Language Toolkit):*

nltk.corpus: Provides access to corpora and lexical resources.<br />
nltk.sentiment.vader: Utilized for sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool.<br />
nltk.tokenize: Used for word tokenization.<br />
nltk.stem: Utilized WordNetLemmatizer for word lemmatization.

**Project Workflow:**
The user inputs text into the Tkinter text box. <br />
The input is preprocessed, including converting to lowercase, removing punctuation, and tokenizing the words.<br />
Stop words (common words like "the," "is," etc.) are removed from the tokenized words.<br />
Words are lemmatized to reduce them to their base form.<br />
Emotion labels are assigned to words based on a predefined list in the 'emotion.txt' file.<br />
The occurrences of each emotion are counted using the Counter class.<br />
The sentiment of the input text is analyzed using the VADER sentiment analysis tool.<br />
