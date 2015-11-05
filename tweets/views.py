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


class Profile(FormView):
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        value = form.cleaned_data['text']
        return super(Profile, self).form_valid(form)
