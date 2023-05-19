from django.db import models

class Diaries(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=20)
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    diary = models.ForeignKey(Diaries, related_name='comments', on_delete=models.CASCADE)
    contents = models.TextField()
    created= models.DateTimeField(auto_now_add=True)

class Notice(models.Model):
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
