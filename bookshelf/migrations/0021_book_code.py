# Generated by Django 2.1.5 on 2019-02-07 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0020_auto_20190207_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookshelf.BarCode'),
        ),
    ]
