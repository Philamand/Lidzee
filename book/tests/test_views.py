from django.test import TestCase
from django.urls import reverse
from .factories import BookFactory, PageFactory


class BookDetailViewTest(TestCase):
    def setUp(self):
        self.book = BookFactory()
        self.pages = PageFactory.create_batch(2, book=self.book)

    def test_get_detail_view(self):
        response = self.client.get(reverse("book_detail", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, 200)

        self.assertIn("pages", response.context)
        self.assertIn("audios", response.context)
        self.assertIn("book", response.context)
