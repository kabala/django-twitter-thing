from django.views.generic import View, FormView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from user_profile.models import User
from tweets.models import Tweet, HashTag
from tweets.forms import TweetForm


class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)


class Profile(View):
    template_name = 'profile.html'
    form_class = TweetForm

    def get(self, request, username):
        params = {}
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        form = TweetForm()
        params['tweets'] = tweets
        params['user'] = user
        params['form'] = form
        return render(request, 'profile.html', params)


class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet()
            tweet.text=form.cleaned_data['text'],
            tweet.user=user,
            tweet.country=form.cleaned_data['country']
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(
                        name=word[1:])
                    hashtag.tweet.add(tweet)
        return HttpResponseRedirect('/user/'+username)
