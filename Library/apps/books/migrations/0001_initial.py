# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table(u'books_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('logotype', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['Publisher'])

        # Adding model 'Author'
        db.create_table(u'books_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['Author'])

        # Adding model 'CategoryBook'
        db.create_table(u'books_categorybook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_Category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['CategoryBook'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ISBN', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=0)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('frontbook', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding M2M table for field category on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('categorybook', models.ForeignKey(orm[u'books.categorybook'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'categorybook_id'])

        # Adding model 'News'
        db.create_table(u'books_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('newsImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['News'])

        # Adding model 'Contact'
        db.create_table(u'books_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_Contact', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_number', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table(u'books_publisher')

        # Deleting model 'Author'
        db.delete_table(u'books_author')

        # Deleting model 'CategoryBook'
        db.delete_table(u'books_categorybook')

        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'books_book_authors'))

        # Removing M2M table for field category on 'Book'
        db.delete_table(db.shorten_name(u'books_book_category'))

        # Deleting model 'News'
        db.delete_table(u'books_news')

        # Deleting model 'Contact'
        db.delete_table(u'books_contact')


    models = {
        u'books.author': {
            'Meta': {'object_name': 'Author'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
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
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '0'}),
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