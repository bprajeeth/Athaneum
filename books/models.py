from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, default="Title")
    type = models.CharField(max_length=20, default="type")
    isbn = models.CharField(max_length=20, default="ISBN0000") # unique id
    author = models.CharField(max_length=100,default="author")
    books_count = models.IntegerField(max_length=100,default=10) # count of each book

    def __str__(self):
        return f"{self.isbn} - {self.title}"


class BookUser(models.Model):
    name = models.CharField(max_length=100, default="username")
    email_id= models.CharField(max_length=100, default="username@gmail.com")
    type = models.CharField(max_length=20, default="student")
    status = models.BooleanField(max_length=20, default=True)# true is that he has got book
    isbn=models.CharField(max_length=20, default="ISBN0000")
    dept = models.CharField(max_length=20,default="dept")

    def __str__(self):
        return f"{self.name} - {self.dept}"