from django import forms
from apps.books.models import Author,Publisher,CategoryBook,Book,Document,News


class addBookForm(forms.ModelForm):
	class Meta:
		model 	= Book
		exclude ={'status'}


class addNewsForm(forms.ModelForm):
	class Meta:
		model 	= News	
		exclude ={'status'}


class addPublisherForm(forms.ModelForm):
	class Meta:
		model 	= Publisher	
		exclude ={'status'}


class addAuthorForm(forms.ModelForm):
	class Meta:
		model 	= Author	
		exclude ={'status'}

	

