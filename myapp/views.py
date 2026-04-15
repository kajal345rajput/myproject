from django.shortcuts import render

def homePageView(request):
    return render(request, 'myapp/home.html')  