from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    information_about_author = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_publication = models.DateTimeField('date published')
    post_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_of_publication = models.DateTimeField('date pubSlished')
    text = models.CharField(max_length=500)
