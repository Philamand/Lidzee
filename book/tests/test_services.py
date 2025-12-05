from django.test import TestCase
from book.services import get_book_pages
from .factories import BookFactory, PageFactory


class BookPagesServiceTest(TestCase):
    def setUp(self):
        self.book = BookFactory()
        self.pages = PageFactory.create_batch(2, book=self.book)

    def test_returns_correct_structure(self):
        data = get_book_pages(self.book)

        self.assertEqual(len(data["pages"]), 3)
