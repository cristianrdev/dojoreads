from django.db import models
from apps.login_app.models import User

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=45)
    uploaded_by = models.ForeignKey(User, related_name="author_uploaded_by", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="book_authors", on_delete = models.CASCADE)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded_by", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    review = models.TextField()
    rating = models.CharField(max_length=1)
    uploaded_by = models.ForeignKey(User, related_name="review_uploaded_by", on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name="review_book", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

