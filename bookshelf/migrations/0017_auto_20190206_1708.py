# Generated by Django 2.1.5 on 2019-02-06 17:08

from django.db import migrations


class Migration(migrations.Migration):
    atomic=False
    
    dependencies = [
        ('bookshelf', '0016_auto_20190206_1706'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Log',
            new_name='A_Logger',
        ),
    ]
