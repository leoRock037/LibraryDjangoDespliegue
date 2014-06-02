from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.books import views


urlpatterns = patterns('apps.books.views',
	
	
	url(r'^home/$','home', name = 'view_home'),

	url(r'^sesion-admin/$','sesion_admin_view',name = 'view_sesion'),


	url(r'^contact/$','contact', name = 'view_contact'),


#.........................user-createUser...............................................

	url(r'^createuser/user$', 'createUser' ,name='createUser'),
    url(r'^createuser/$', 'user' ,name='user'),


#.........................books.........................................................

	url(r'^books/$','index_books', name = 'view_books'),
	url(r'^books/book/(?P<id_book>\d+)$','book', name ='view_book'),
	url(r'^categoryBook/$','category_book', name = 'view_CategoryBook'),

	url(r'^addBook/$','addBook_view',name = 'view_addBook'),


#.........................author.......................................................

	url(r'^authors/$','index_authors', name = 'view_authors'),
	url(r'^authors/author/(?P<id_author>\d+)$','author', name = 'view_author'),

	url(r'^addAuthor/$','addAuthor_view',name = 'view_addAuthor'),

	url(r'^editAuthor/(?P<id_author>.*)/$','edit_author_view',name= "view_edit_author"),
	url(r'^listauthors/$','index_authors_edit', name = 'view_authorslist'),

	url(r'^deleteAuthor/(?P<id_author>.*)$', 'author_delete', name='view_delete_author'),
	url(r'^authors_delete/$','index_authors_delete', name = 'view_authorslist_delete'),


#.........................publisher...................................................

	url(r'^publishers/$','index_publishers', name = 'view_publishers'),
	url(r'^publishers/publisher/(?P<id_pub>\d+)$','publisher', name ='view_publisher'),

	url(r'^addPublisher/$','addPublisher_view',name = 'view_addPublisher'),

	url(r'^deletePublisher/(?P<id_publisher>.*)$', 'publisher_delete', name='view_delete_publisher'),
	url(r'^publisher_delete/$','index_publishers_delete', name = 'view_publisherslist_delete'),


#.........................news.......................................................
	
	url(r'^news/$','news', name = 'view_news'),
	url(r'^addNews/$','addNews_view',name = 'view_addNews'),
	


	
	
	

	
	

	
	

)