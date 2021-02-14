from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=64)

    class Meta:
        db_table = "posts"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.pk}: {self.title[:20]}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=64)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.pk}: {self.author}"
