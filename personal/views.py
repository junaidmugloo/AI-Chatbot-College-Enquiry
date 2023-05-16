from django.shortcuts import render
from .colab import utils

# Create your views here.


def home_screen_view(request):
    print(request.headers)
    return render(request, "personal/home.html", {})


def chating_page(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        output = utils.runQuery(question)
        return render(request, "personal/chatting.html", {'answer': output})
    return render(request, "personal/chatting.html", {})
