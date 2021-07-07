from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "home.html", {}) 

#creating another view
def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {}) #string of HTML code 

def about_view(request, *args, **kwargs):
	my_context = {
	"my_text": "this is about us",
	"this_is_true": True,
	"my_number": 123,
	"my_list": [123,4242,12313, "abc"]
	}
	return render(request, "about.html", my_context) #string of HTML code 

