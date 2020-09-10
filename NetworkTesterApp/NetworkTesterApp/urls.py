from django.urls import path
from . import views

''' 1 - Create a list urlpatterns.
2 - For each desired URL, add an item to the urlpatterns list that contains a call to the path function with two or three arguments: 
A string representing the URL path, a function from views.py that we wish to call when that URL is visited, and (optionally) a name for that path, in the format name="something". 
For example, here’s what our simple app looks like now:'''


urlpatterns = [
    path("", views.index, name = "index"),
    path("test", views.test, name = "test"),
]
