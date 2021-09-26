from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)

        widgets = {
            'name': forms.TextInput(attrs={'name': 'name', 'id': 'name_field'}),#id="name_field"
            'email': forms.TextInput(attrs={'name': 'email', 'id': 'email_field'}),
            'content': forms.Textarea(attrs={'name': 'comment', 'id': 'comment'}),
        }
