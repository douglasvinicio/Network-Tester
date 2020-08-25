from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

def index(request):
    return render(request, "NetworkTesterApp/index.html")

class NewTesterForm (forms.Form):
    test = forms.CharField(label = "New Test")

def test(request):
    if request.method == "POST":
        form = NewTesterForm(request.POST)

        #Function goes here...i'll show the result later on the test page




    return render(request, "NetworkTesterApp/test.html", {
        "form": NewTesterForm()
    })
