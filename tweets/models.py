from django.db import models
from user_profile.models import User


class Tweet(models.Model):

    """
    Tweet Model
    """

    user = models.ForeignKey(User)
    text = models.CharField('tweet', max_length=160,)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField('país', max_length=30)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.text


class HashTag(models.Model):

    """
    Hashtag Model
    """

    name = models.CharField(max_length=64, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __unicode__(self):
        return self.name
