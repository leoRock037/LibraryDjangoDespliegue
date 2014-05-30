# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sale'
        db.create_table(u'sales_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('charge_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'sales', ['Sale'])


    def backwards(self, orm):
        # Deleting model 'Sale'
        db.delete_table(u'sales_sale')


    models = {
        u'sales.sale': {
            'Meta': {'object_name': 'Sale'},
            'charge_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['sales']