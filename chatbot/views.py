from django.shortcuts import render

from django.shortcuts import render
from .bot import Chatbot

chatbot = Chatbot('chatbot/dataset.json')

def chat_view(request):
    response = ''
    question = ''
    if request.method == 'POST':
        question = request.POST.get('question')
        response = chatbot.get_response(question)
    return render(request, 'chat.html', {'response': response, 'question': question})

