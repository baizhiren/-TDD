from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        return HTTPResponse(request.POST['item_text'])
    return render(request, 'home.html') 