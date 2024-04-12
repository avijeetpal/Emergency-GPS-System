import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np
from gensim.models import Word2Vec
import random
import pickle

class ChatBotTrainer:
    def __init__(self):
        self.model = None
        self.word2vec_model = None
        self.training_data = []
        self.labels = []

    def preprocess(self, text):
        tokens = nltk.word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(lemmatized_tokens)

    def train_word2vec(self):
        self.word2vec_model = Word2Vec(sentences=[text.split() for text in self.training_data], vector_size=100, window=5, min_count=1, workers=4)

    def vectorize_sentence(self, sentence):
        if self.word2vec_model is None:
            return np.zeros((100,))
        vector = np.zeros((100,))
        for word in sentence.split():
            if word in self.word2vec_model.wv.key_to_index:
                vector += self.word2vec_model.wv[word]
        return vector

    def preprocess_training_data(self):
        self.training_data = [self.preprocess(text) for text in self.training_data]

    def vectorize_training_data(self):
        X_train = np.array([self.vectorize_sentence(sentence) for sentence in self.training_data])
        return X_train

    def split_data(self):
        X_train, X_test, y_train, y_test = train_test_split(self.vectorize_training_data(), self.labels, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        X_train, _, y_train, _ = self.split_data()
        self.model.fit(X_train, y_train)

    def evaluate_model(self):
        _, X_test, _, y_test = self.split_data()
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def train(self, intents):
        for intent, data in intents.items():
            for pattern in data['patterns']:
                self.training_data.append(pattern.lower())
                self.labels.append(intent)
        
        self.preprocess_training_data()
        self.train_word2vec()
        self.train_model()
        self.evaluate_model()

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump((self.model, self.word2vec_model, self.training_data, self.labels), file)

    def load(self, filename):
        with open(filename, 'rb') as file:
            self.model, self.word2vec_model, self.training_data, self.labels = pickle.load(file)

class ChatBot:
    def __init__(self):
        self.trainer = ChatBotTrainer()
        self.load_intents()  # Load intents during initialization
        try:
            self.trainer.train(self.intents)  # Train the model
        except Exception as e:
            print("Error during training:", e)

    def load_intents(self):
        try:
            from database.database2 import intents  # Import intents here
            self.intents = intents  # Store intents in the ChatBot instance
        except ImportError:
            print("Error: Could not load intents.")

    def predict_intent(self, user_input):
        preprocessed_input = self.trainer.preprocess(user_input.lower())
        input_vector = self.trainer.vectorize_sentence(preprocessed_input)
        if self.trainer.model is None:
            return None, None, None  # Return None for both intent and confidence if model is not trained
        predictions = self.trainer.model.predict_proba([input_vector])[0]
        max_confidence = max(predictions)
        min_confidence = min(predictions)
        intent = self.trainer.model.classes_[np.argmax(predictions)]  # Get the intent with maximum confidence
        return intent, max_confidence, min_confidence

    def get_response(self, intent):
        responses = self.intents[intent]['responses']
        return random.choice(responses)

    def start_chat(self):
        print("what is the Emergency.")
        
        user_input = input("You: ")
        if user_input.lower() == 'train':
            print("Bot: Training...")
            try:
                self.trainer.train(self.intents)
                print("Bot: Done training.")
            except Exception as e:
                print("Error during training:", e)
        else:
            intent, max_confidence, min_confidence = self.predict_intent(user_input)
            max_confidence = int(max_confidence * 100)
            ris=self.get_response(intent)
            if max_confidence > 12:
                print("Bot:",ris )
                print("Max Confidence:", max_confidence)
                print("Min Confidence:", min_confidence)
                print("Intent:", intent)
            if intent=="police":
                callpolice()
            if intent=="firefigther":
                callfirefighter()
            if intent=="hospital":
                callhospital()
            else:
                print("Bot: Sorry, I'm not sure how to respond to that.")
                print("Intent:", intent)
                print("Max Confidence:", max_confidence)
                print("Min Confidence:", min_confidence)

# Main program
chatbot = ChatBot()
chatbot.start_chat()