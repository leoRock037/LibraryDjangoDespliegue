from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from apps.books.models import CategoryBook, News, Publisher, Author,Book,Contact
from apps.books.forms import addNewsForm,addPublisherForm,addAuthorForm,addBookForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def home(request):
	book = Book.objects.filter(status = True)
	ctx = {"books":book}
	return render_to_response('home.html',ctx,context_instance = RequestContext(request))



def sesion_admin_view(request):
	return render_to_response('sesion-admin.html')


# .......................................Books......................................................................

def category_book(request):
	return render_to_response('CategoryBook.html')

def index_books(request):
	book = Book.objects.filter(status = True)
	cat = CategoryBook.objects.filter(status = True)
	ctx = {"books":book,"category":cat}
	return render_to_response('index_books.html',ctx,context_instance = RequestContext(request))

def book(request,id_book):
	book_id = get_object_or_404(Book,pk=id_book)
	book = Book.objects.filter(status = True)
	cat = CategoryBook.objects.filter(status = True)
	return render_to_response('book.html',{'book':book_id,'books':book,"category":cat},context_instance = RequestContext(request))

@login_required()
def addBook_view(request):
	info = "Loading information...."
	if request.method == "POST":
		form = addBookForm(request.POST,request.FILES)
		if form.is_valid():
			newimg = Book(frontbook = request.FILES['frontbook'])
			add = form.save(commit=False)
			add.status = True
			add.save()#guarda la info
			form.save_m2m()#guarda lo many to many
			info ="saved information!"
			return HttpResponseRedirect(reverse('apps.books.views.index_books'))		
	else:
		form = addBookForm()
	image=Book.objects.all()
	auth = Author.objects.filter(status = True)
	publisher=Publisher.objects.filter(status=True)
	category=CategoryBook.objects.filter(status=True)
	ctx = {'form':form, 'information':info,'image':image, 'authors':auth,'publisher':publisher,'category':category}
	return render_to_response('addBook.html',ctx,context_instance=RequestContext(request))




# ...........................Authors......................................................................


def author(request, id_author):
	auth_id = get_object_or_404(Author,pk=id_author)#
	auth = Author.objects.filter(status = True)
	return render_to_response('author.html',{'author':auth_id,'authors':auth},context_instance = RequestContext(request))

def index_authors(request):
	auth = Author.objects.filter(status = True)
	ctx  = {"authors":auth} 
	return render_to_response('index_authors.html',ctx,context_instance = RequestContext(request))

@login_required()
def index_authors_edit(request):
	auth = Author.objects.filter(status = True)
	ctx  = {"authors":auth} 
	return render_to_response('index_authors_edit.html',ctx,context_instance = RequestContext(request))

@login_required()
def addAuthor_view(request):
	info = "Loading information...."
	if request.method == "POST":
		form = addAuthorForm(request.POST,request.FILES)
		if form.is_valid():
			newimg = Author(photo = request.FILES['photo'])
			add = form.save(commit=False)
			add.status = True
			add.save()#guarda la info
			info ="saved information!"
			return HttpResponseRedirect(reverse('apps.books.views.index_authors'))		
	else:
		form = addAuthorForm()
	image=Author.objects.all()
	ctx = {'form':form, 'information':info,'image':image}
	return render_to_response('addAuthor.html',ctx,context_instance=RequestContext(request))


@login_required()
def index_authors_delete(request):
	auth = Author.objects.filter(status = True)
	ctx  = {"authors":auth} 
	return render_to_response('index_authors_delete.html',ctx,context_instance = RequestContext(request))


@login_required()
def author_delete(request, id_author, template_name='deleteAuthor.html'):
    author = get_object_or_404(Author, pk=id_author)    
    if request.method=='POST':
        author.delete()
        return redirect('view_authorslist_delete')
    return render(request, template_name, {'object':author})

@login_required()
def edit_author_view(request,id_author):
	info = "Loading information...."
	author = Author.objects.get(pk=id_author)
	if request.method == "POST":
		form = addAuthorForm(request.POST,request.FILES,instance=author)
		if form.is_valid():
			edit_author = form.save(commit=False)
			
			edit_author.status = True
			edit_author.save() 
			info ="saved information!"
			return render_to_response('sesion-admin.html')
	else:
		form = addAuthorForm(instance=author)
	ctx = {'form':form,'information':info}
	return render_to_response('editAuthor.html',ctx,context_instance=RequestContext(request))





# ..........................................Publisher.....................................................................

def index_publishers(request):
	pub = Publisher.objects.filter(status = True)
	ctx = {"pub":pub}
	return render_to_response('index_publishers.html',ctx,context_instance = RequestContext(request))

def publisher(request,id_pub):
	pub_id = get_object_or_404(Publisher,pk=id_pub)
	pub = Publisher.objects.filter(status = True)
	return render_to_response('publisher.html',{'pub_id':pub_id,'pub':pub},context_instance = RequestContext(request))


@login_required()
def addPublisher_view(request):
	info = "Loading information...."
	if request.method == "POST":
		form = addPublisherForm(request.POST,request.FILES)
		if form.is_valid():
			newimg = Publisher(logotype = request.FILES['logotype'])
			add = form.save(commit=False)
			add.status = True
			add.save()#guarda la info
			info ="saved information!"
			return HttpResponseRedirect(reverse('apps.books.views.index_publishers'))		
	else:
		form = addPublisherForm()
	image=Publisher.objects.all()
	ctx = {'form':form, 'information':info,'image':image}
	return render_to_response('addPublisher.html',ctx,context_instance=RequestContext(request))
	


@login_required()
def index_publishers_delete(request):
	pub = Publisher.objects.filter(status = True)
	ctx  = {"publishers":pub} 
	return render_to_response('index_publishers_delete.html',ctx,context_instance = RequestContext(request))


@login_required()
def publisher_delete(request, id_publisher, template_name='deletePublisher.html'):
    publisher = get_object_or_404(Publisher, pk=id_publisher)    
    if request.method=='POST':
        publisher.delete()
        return redirect('view_publisherslist_delete')
    return render(request, template_name, {'object':publisher})



# ..............................................News......................................................................

def news(request):
	news = News.objects.filter(status = True)
	ctx = {"News":news}
	return render_to_response('news.html',ctx,context_instance = RequestContext(request))


@login_required()
def addNews_view(request):
	info = "Loading information...."
	if request.method == "POST":
		form = addNewsForm(request.POST,request.FILES)
		if form.is_valid():
			newimg = News(newsImage = request.FILES['newsImage'])
			add = form.save(commit=False)
			add.status = True
			add.save()#guarda la info
			info ="saved information!"
			return HttpResponseRedirect(reverse('apps.books.views.news'))		
	else:
		form = addNewsForm()
	image=News.objects.all()
	ctx = {'form':form, 'information':info,'image':image}
	return render_to_response('addNews.html',ctx,context_instance=RequestContext(request))



# .............................................User-Create-User......................................................................


def user(request):
	return render(request,'createUser.html')

def createUser(request):
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	user = User.objects.create_user(username, email, password)	
	user.save()
	return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))

# .............................................Contact......................................................................

def contact(request):
	cont = Contact.objects.filter(status=True)
	ctx = {"Contact":cont}
	return render_to_response('contact.html',ctx,context_instance = RequestContext(request))