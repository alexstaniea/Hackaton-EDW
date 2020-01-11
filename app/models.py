from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    credit = models.FloatField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    photo = models.FileField(upload_to='media/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=70)
    price = models.FloatField()


class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article, related_name='carts', blank=True)
    sum = models.FloatField()


class Review(models.Model):
    article= models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_reviews')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.CharField(max_length=30, blank=True, null=True)
    nota = models.IntegerField()


