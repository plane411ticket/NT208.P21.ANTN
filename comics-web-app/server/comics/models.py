from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/')
    audio_file = models.FileField(upload_to='audio/')
    is_audio_comic = models.BooleanField(default=False)
    is_story = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class AudioComic(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio_comics/')

    def __str__(self):
        return f"Audio for {self.comic.title}"