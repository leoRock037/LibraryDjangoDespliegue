# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.nationality'
        db.add_column(u'books_author', 'nationality',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=50),
                      keep_default=False)


        # Changing field 'Book.price'
        db.alter_column(u'books_book', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=4))

    def backwards(self, orm):
        # Deleting field 'Author.nationality'
        db.delete_column(u'books_author', 'nationality')


        # Changing field 'Book.price'
        db.alter_column(u'books_book', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=0))

    models = {
        u'books.author': {
            'Meta': {'object_name': 'Author'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'books.book': {
            'ISBN': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.Author']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.CategoryBook']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'frontbook': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '4'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Publisher']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'books.categorybook': {
            'Meta': {'object_name': 'CategoryBook'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_Category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'books.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email_Contact': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'books.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logotype': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['books']