from django import forms


class TweetForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 1, 'cols': 85, 'class': 'form-control post-tweet',
                'placeholder': 'Post a new Tweet', 'required': True}),
        max_length=160, required=True)
    country = forms.CharField(widget=forms.HiddenInput(), required=False)
