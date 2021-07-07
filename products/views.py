from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render

## first version created for the form
# from .forms import ProductForm
# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()

# 	context = {
# 		'form': form
# 	}
# 	return render(request, "product_create.html", context)
# 	#the slash is the folder, after the file we want to render

## second version created for the form 
# from .forms import ProductForm
# def product_create_view(request):
# 	print(request.GET)
# 	print(request.POST)
# 	title = request.POST.get('title')
# 	context = {}
# 	return render(request, "product_create.html", context)
# 	#the slash is the folder, after the file we want to render


## thrid version : pure django form
# from .forms import ProductForm, RawProductForm
# from .models import Product


# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST) #create instance of a class
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		#now the data is good
# 		else: 
# 			print(my_form.errors)

# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "product_create.html", context)
# 	#the slash is the folder, after the file we want to render



## fourth version : 
from .forms import ProductForm
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "product_create.html", context)
	#the slash is the folder, after the file we want to render



####

from .models import Product #importing product class from models doc
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id = 1)
	#context = {
	#	'title': obj.title,
	#	'description': obj.description
	#}

	context = {
		'object': obj
	}
	return render(request, "detail.html", context)
	#the slash is the folder, after the file we want to render