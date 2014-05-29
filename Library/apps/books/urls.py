from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.books import views


urlpatterns = patterns('apps.books.views',
	

	url(r'^home/$','home', name = 'view_home'),

	url(r'^books/$','index_books', name = 'view_books'),
	url(r'^books/book/(?P<id_book>\d+)$','book', name ='view_book'),

	url(r'^authors/$','index_authors', name = 'view_authors'),
	url(r'^authors/author/(?P<id_author>\d+)$','author', name = 'view_author'),

	url(r'^publishers/$','index_publishers', name = 'view_publishers'),
	url(r'^publishers/publisher/(?P<id_pub>\d+)$','publisher', name ='view_publisher'),
	
	url(r'^news/$','news', name = 'view_news'),
	url(r'^contact/$','contact', name = 'view_contact'),
	url(r'^categoryBook/$','category_book', name = 'view_CategoryBook'),
	
	url(r'^addBook/$','addBook_view',name = 'view_addBook'),
	url(r'^addNews/$','addNews_view',name = 'view_addNews'),
	url(r'^addPublisher/$','addPublisher_view',name = 'view_addPublisher'),
	url(r'^addAuthor/$','addAuthor_view',name = 'view_addAuthor'),

	url(r'^list/$', 'list', name='list'),
	url(r'^createuser/user$', 'createUser' ,name='createUser'),
    url(r'^createuser/$', 'user' ,name='user'),
	
	url(r'^sesion-admin/$','sesion_admin_view',name = 'view_sesion'),
)