from .models import stickers
from django import forms

class NewPost(forms.ModelForm):
    class Meta:
        model = stickers
        fields = ('cat', 'img', 'title', 'desc', 'price', 'keywords')
        lables = {
            'cat':'',
            'img':'',
            'title':'',
            'desc':'',
            'price':'',
        }
        widgets = {
            'cat': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Категория'}),
            'title': forms.TextInput(attrs={'class':'forms-control','placeholder':'Заголовок'}),
            'desc': forms.Textarea(attrs={'class':'forms-control','placeholder':'Описание'}),
            'price': forms.TextInput(attrs={'class':'forms-control','placeholder':'Цена'}),
            'keywords': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Ключевые слова'}),
        }

