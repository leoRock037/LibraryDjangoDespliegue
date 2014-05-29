from django import forms
from apps.books.models import Author,Publisher,CategoryBook,Book,Document


class addBookForm(forms.ModelForm):
	class Meta:
		model 	= Book
		exclude ={'status'}



"""
class addBookForm(forms.Form):
	title 				= forms.CharField(max_length = 100)
	authors 			= forms.ModelMultipleChoiceField(queryset=Author.objects.all())
	ISBN 				= forms.CharField(max_length = 13)
	publisher 			= forms.ModelChoiceField(queryset=Publisher.objects.all())
	publication_date 	= forms.DateField()
	price 				= forms.DecimalField(required=False)
	description 		= forms.CharField(widget = forms.Textarea) 			
	category 			= forms.ModelMultipleChoiceField(queryset=CategoryBook.objects.all())
	frontbook 			= forms.ImageField(required=False)

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data
"""



class addNewsForm(forms.Form):
	title 		= forms.CharField(max_length=50)
	newsImage	= forms.FileField(required=False)#cambiar para poder agregarla
	date 		= forms.DateField()
	description = forms.CharField(widget = forms.Textarea)

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data

class addPublisherForm(forms.Form):
	name 			= forms.CharField(max_length = 30)
	address 		= forms.CharField(max_length = 50)
	city 			= forms.CharField(max_length = 60)
	state_province 	= forms.CharField(max_length = 50)
	website 		= forms.URLField(max_length=200)
	logotype 		= forms.ImageField(required=False)#cambiar....
	

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data


class addAuthorForm(forms.Form):
	first_name 		= forms.CharField(max_length = 30)
	last_name 		= forms.CharField(max_length = 40)
	email 			= forms.EmailField()
	biography 		= forms.CharField(widget = forms.Textarea)
	photo 			= forms.ImageField(required=False)#cmabir.........
	
	

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data
	
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

