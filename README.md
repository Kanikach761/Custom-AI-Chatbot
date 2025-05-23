** Custom AI chatbot

This project is a custom-built AI chatbot that responds to user queries based on a domain-specific dataset. It uses TF-IDF vectorization and Logistic Regression for text classification, allowing the chatbot to understand user questions and return appropriate answers.

* How It Works-
**Text Similarity Matching:

User input is transformed into a vector using TF-IDF (Term Frequency-Inverse Document Frequency).

The chatbot calculates cosine similarity between the user input and the dataset questions.

The most similar question is identified, and the corresponding answer is returned.

** JSON format dataset

The chatbot relies on a structured dataset saved in a simple JSON format, designed to pair each user question with an appropriate bot answer. 

* Technologies Used-
  
Python

Scikit-learn (for ML model)

TF-IDF (for text feature extraction)

Logistic Regression

Django (for web interface)

* Fine-tuning-
  
We trained the model once using fine_tune.py, and saved the trained model and vectorizer as model.pkl. Now, whenever the chatbot runs, it loads the pre-trained model instantly, resulting in:
Training the model (TF-IDF + Logistic Regression) once on the dataset.

Saving the model (model.pkl) for fast reuse.

Eliminates the need to re-train the model every time, improving performance.

Faster responses

Improved accuracy

Efficient performance

* Flask Alternative-
  
If you prefer Flask instead of Django, the chatbot logic (bot.py) is modular and can easily be integrated into a Flask web application using routes and templates.



![Screenshot (53)](https://github.com/user-attachments/assets/e3040169-5e37-4ac4-80e4-29bb354ca50b)

![Screenshot (54)](https://github.com/user-attachments/assets/22c0fd62-2676-43ef-9b49-ff7ff5c18616)
