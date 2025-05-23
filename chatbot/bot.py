import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
import pickle

class Chatbot:
    def __init__(self, dataset_path):
        with open(dataset_path, 'r') as f:
            data = json.load(f)

        self.questions = [item['question'] for item in data]
        self.answers = [item['answer'] for item in data]

        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

        if os.path.exists('chatbot/model.pkl'):
            with open('chatbot/model.pkl', 'rb') as f:
                self.model, self.vectorizer = pickle.load(f)
        else:
            X = self.vectorizer.fit_transform(self.questions)
            y = list(range(len(self.questions)))
            self.model.fit(X, y)
            with open('chatbot/model.pkl', 'wb') as f:
                pickle.dump((self.model, self.vectorizer), f)

    def get_response(self, user_input):
        X_input = self.vectorizer.transform([user_input])
        prediction = self.model.predict(X_input)[0]

        # Compute cosine similarity
        similarities = cosine_similarity(X_input, self.vectorizer.transform([self.questions[prediction]]))
        similarity_score = similarities[0][0]


        if similarity_score < 0.5:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"
        return self.answers[prediction]


if __name__ == "__main__":
    bot = Chatbot('chatbot/dataset.json')
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = bot.get_response(user_input)
        print("Bot:", response)
