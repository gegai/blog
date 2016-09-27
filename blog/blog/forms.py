from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, min_length=2)
    category_id = forms.IntegerField()
    abstract = forms.CharField(max_length=54)
    content = forms.CharField(min_length=20)
    head_img = forms.ImageField()
