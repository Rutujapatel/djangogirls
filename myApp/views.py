from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	context = {
		"var": 1
	}
	return render(request, "myApp/home.html", context)
