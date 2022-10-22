from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    return render(request, 'reverse.html', {"user_text": user_text, "reverse_text": reverse_text})