import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open('chatbot/dataset.json', 'r') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
answers = [item['answer'] for item in data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)
y = list(range(len(answers)))

model = LogisticRegression()
model.fit(X, y)

with open('chatbot/model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("Fine-tuning completed and model saved.")
