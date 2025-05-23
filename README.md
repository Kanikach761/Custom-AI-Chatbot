** Custom AI Chatbot

This project is a custom AI chatbot built using traditional machine learning techniques and fine-tuning with TF-IDF and Logistic Regression. It demonstrates how to build a question-answering bot trained on a user-defined dataset (dataset.json) with a simple and clean web interface built using Django.

* How It Works-
Text Similarity Matching:

User input is transformed into a vector using TF-IDF (Term Frequency-Inverse Document Frequency).

The chatbot calculates cosine similarity between the user input and the dataset questions.

The most similar question is identified, and the corresponding answer is returned.

Classification Layer (Optional):

Uses Logistic Regression to classify the input if needed.

Especially helpful when the dataset grows or becomes more diverse.


Technologies Used-
Python

Scikit-learn

Django (can be replaced with Flask if needed)

JSON (for training data)

* Fine tuning-

We trained the model once using fine_tune.py, and saved the trained model and vectorizer as model.pkl. Now, whenever the chatbot runs, it loads the pre-trained model instantly, resulting in:

Faster responses

Improved accuracy

Efficient performance

Flask Alternative-
If you prefer Flask instead of Django, the chatbot logic (bot.py) is modular and can easily be integrated into a Flask web application using routes and templates.

![Screenshot (53)](https://github.com/user-attachments/assets/e3040169-5e37-4ac4-80e4-29bb354ca50b)

![Screenshot (54)](https://github.com/user-attachments/assets/22c0fd62-2676-43ef-9b49-ff7ff5c18616)
