from django.shortcuts import render

# Create your views here.


def loginlist(request):
    return render(request, 'loginlist.html')
