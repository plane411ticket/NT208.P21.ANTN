from django.test import TestCase
from .models import Comic

class ComicModelTest(TestCase):
    def setUp(self):
        Comic.objects.create(title="Test Comic", author="Author Name", language="Vietnamese")

    def test_comic_creation(self):
        comic = Comic.objects.get(title="Test Comic")
        self.assertEqual(comic.author, "Author Name")
        self.assertEqual(comic.language, "Vietnamese")