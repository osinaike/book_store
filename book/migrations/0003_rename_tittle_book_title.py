# Generated by Django 4.1.3 on 2022-11-21 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_address_publisher_book_authors_book_publisher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tittle',
            new_name='title',
        ),
    ]
