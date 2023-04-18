from django import forms 
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=["post"]
        label={
            "user":"your name",
            "email":"your email",
            "text":"YOUR COMMENT"

        }

