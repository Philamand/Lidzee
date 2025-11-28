import json
from typing import Any
from django.views.generic import ListView, DetailView
from .models import Book, Page


class BookListView(ListView):
    model = Book
    queryset = Book.objects.filter(published=True)
    context_object_name = "book_list"
    ordering = "title"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        audios = []
        pages = [{"image": self.object.cover.url, "text": self.object.title}]
        data = Page.objects.filter(book=self.object).order_by("id").all()

        for index, page in enumerate(data):
            audios.append({"id": f"audio-{str(index + 1)}", "url": page.audio.url})
            pages.append({"image": page.image.url, "text": page.text})
        context["audios"] = audios
        context["pages"] = json.dumps(pages)
        return context
