from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from socket import *
import time

startTime = time.time()
connections = []
ports = []

#New Form
class NewTesterForm (forms.Form):
    ipField = forms.CharField(label = "Insert the IP Address here ")

# Create your views here.
def index(request):
    return render(request, "NetworkTesterApp/index.html", {
        "form":NewTesterForm()
    })

def test(request):
    if request.method == "POST":
        ipForTest = NewTesterForm(request.POST)
        if ipForTest.is_valid():
           takeIdInput = ipForTest.cleaned_data["ipField"]
           t_IP = gethostbyname(takeIdInput)
           for i in range(50, 100):
               s = socket(AF_INET, SOCK_STREAM)
               conn = s.connect_ex((t_IP, i))
               if (conn == 0):
                   ports.append(i)
               s.close()
        timeTaken = 'Time taken:', time.time() - startTime
    return render(request, "NetworkTesterApp/test.html", {
        "takeIdInput":takeIdInput, "timeTaken":timeTaken, "port":ports
    })
