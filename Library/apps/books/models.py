from django.db import models


# Create your models here.
class Publisher(models.Model):
	name 			= models.CharField(max_length = 30)
	address 		= models.CharField(max_length = 50)
	city 			= models.CharField(max_length = 60)
	state_province 	= models.CharField(max_length = 50)
	website 		= models.URLField(max_length=200)
	logotype 		= models.ImageField(upload_to ='imagesDB')
	status 			= models.BooleanField(default = True)

	def __unicode__(self):
		return self.name

class Author(models.Model):
	first_name 		= models.CharField(max_length = 30)
	last_name 		= models.CharField(max_length = 40)
	email 			= models.EmailField(verbose_name ='e-mail')
	biography 		= models.TextField()
	photo 			= models.ImageField(upload_to ='imagesDB')
	status 			= models.BooleanField(default = True)
	
	def __unicode__(self):
		return u'%s%s'%(self.first_name , self.last_name)

class CategoryBook(models.Model):
	name_Category 	=  models.CharField(max_length = 100)
	status 			=  models.BooleanField(default = True)

	def __unicode__(self):
		return self.name_Category

class Book(models.Model):
	title 				= models.CharField(max_length = 100)
	authors 			= models.ManyToManyField(Author)
	ISBN 				= models.CharField(max_length = 13)
	publisher 			= models.ForeignKey(Publisher)
	publication_date 	= models.DateField(null = False)
	price 				= models.DecimalField(max_digits = 20,decimal_places = 4)
	description 		= models.TextField()
	category 			= models.ManyToManyField(CategoryBook)
	frontbook 			= models.FileField(upload_to ='imagesDB')
	status 				= models.BooleanField(default = True)

	def __unicode__(self):
		return self.title

	def comprar(self):
		pass


class News(models.Model):

	title 		= models.CharField(max_length = 50)
	newsImage	= models.FileField(upload_to ='imagesDB')
	date 		= models.DateField()
	description = models.TextField()
	status 		= models.BooleanField(default = True)

	def __unicode__(self):
		return self.title


class Contact(models.Model):
	email_Contact 	= models.EmailField(verbose_name = 'e-mail')
	address 		= models.CharField(max_length = 50)
	phone_number 	= models.IntegerField()
	status 			= models.BooleanField(default = True)

	def __unicode__(self):
		return self.email_Contact

class Document(models.Model):
    docfile = models.FileField(upload_to='imagesDB/%Y/%m/%d')