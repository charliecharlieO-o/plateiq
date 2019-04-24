from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Max length based on the guiness record for "longest book title"
    title = models.CharField(max_length=4805, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ends_on = models.DateField(blank=True, null=True, default=None)
    added_on = models.DateTimeField(auto_now_add=True)
