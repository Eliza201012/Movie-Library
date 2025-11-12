from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "photo", "main_text"]

        widgets = {
            "title" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Enter news title...",
            }),
            "photo" : forms.FileInput(attrs={
                "class" : "form-control",
            }),
            "main_text" : forms.Textarea(attrs={
                "class" : "form-control",
                "rows" : 10,
                "placeholder" : "Write the full article text here..."
            }),
        }

        labels = {
            "title" : "News Title",
            "photo" : "Cover Photo",
            "main_text" : "Main Text"
        }