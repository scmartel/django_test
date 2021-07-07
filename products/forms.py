from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label = '',
		widget = forms.TextInput(attrs = {"placeholder": "Your title"}))
	description = forms.CharField(
						required = False,
						widget = forms.Textarea(
							attrs={
							"class": "new_class_name",
							"id": "my_id_for_textarea",
							"rows": 20,
							"cols":50
							}))

	class Meta: 
		model = Product
		fields = [
			'title',
			'description',
			'price']

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title: 
			raise forms.ValidationError("this is not a valid title")
		else: 
			return title



class RawProductForm(forms.Form):
	title = forms.CharField(label = '', widget = forms.TextInput(attrs = {"placeholder": "your title"}))
	description = forms.CharField(
						required = False,
						widget = forms.Textarea(
							attrs={
							"class": "new_class_name",
							"id": "my_id_for_textarea",
							"rows": 10,
							"cols":10
							}))
	price = forms.DecimalField(initial = 99.99)
