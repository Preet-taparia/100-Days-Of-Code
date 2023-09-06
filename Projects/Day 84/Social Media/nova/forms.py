from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    body = forms.CharField(required = True, widget = forms.widgets.Textarea(attrs={"placeholder" : "Enter your Post!", "class" : "form-control"}), label = "")

    class Meta:
        model = Posts
        exclude = ("user",)