from django.shortcuts import render

def home(request):
    context = {
        'message': 'Helle world!!!',
    }
    return render(request, 'home.html', context=context)
