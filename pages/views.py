from django.shortcuts import render


def page_home(request):
    return render(request, 'pages/page_home.html')
