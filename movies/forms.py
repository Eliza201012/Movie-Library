from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "title",
            "poster",
            "description",
            "rating",
            "genre",
            "duration",
            "actors",
            "release_date",
            "status"
        ]
        widgets = {
            "title" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "Enter movie title",
            }),
            "poster" : forms.FileInput(attrs={
                "class" : "form-control",
            }),
            "description" : forms.Textarea(attrs={
                "class" : "form-control",
                "rows" : 4,
                "placeholder" : "Write a description...",
            }),
            "rating" : forms.NumberInput(attrs={
                "class" : "form-control",
                "min" : 0,
                "max" : 10,
            }),
            "genre" : forms.Select(attrs={
                "class" : "form-control",
            }),
            "duration" : forms.NumberInput(attrs={
                "class" : "form-control",
            }),
            "actors" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder" : "List main actors",
            }),
            "release_date" : forms.DateInput(attrs={
                "class" : "form-control",
                "type" : "date",
            }),
        }