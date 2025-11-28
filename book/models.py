from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to="books/covers/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("book_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="books/images/")
    audio = models.FileField(upload_to="books/audio/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
