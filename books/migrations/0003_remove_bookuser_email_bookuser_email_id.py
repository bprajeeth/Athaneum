# Generated by Django 4.0.4 on 2022-09-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_status_book_books_count_bookuser_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookuser',
            name='email',
        ),
        migrations.AddField(
            model_name='bookuser',
            name='email_id',
            field=models.CharField(default='username@gmail.com', max_length=100),
        ),
    ]
