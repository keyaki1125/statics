from django import forms

from .models import Image


class CreationForm(forms.ModelForm):

    title = forms.CharField(label='タイトル')
    image = forms.ImageField(label='画像選択')

    class Meta:
        model = Image
        fields = [
            'title',
            'image',
        ]