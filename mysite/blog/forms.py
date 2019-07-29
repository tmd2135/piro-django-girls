from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #어떤 model을 사용할지 장고에 알려주기
    class Meta:
        model = Post
        fields = ('title','text',)