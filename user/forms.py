

from django import forms 

from django.contrib.auth.models import User

from .models import Posts, Comments

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','content')

    title = forms.CharField(
    	max_length=100,
    	widget=forms.TextInput(attrs={
    		'class' : 'form-control',
    		'id' : 'title', 
    		'placeholder' : 'Başlıq əlavə edin',
    		})
    	)
    content = forms.CharField(
    	max_length=3000,
    	widget=forms.Textarea(attrs={
    		'class' : 'form-control',
    		'id' : 'content',
    		'placeholder' : ' Yazın...',
    		'rows' : '3',
    		})
    	)
    def clean(self):
    	title = self.cleaned_data.get('title')
    	content = self.cleaned_data.get('content')
    	return {
    		'title': title,
    		'content' : content,
    	}

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_content',)

    comment_content = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={
        'class' : 'form-control form-control-sm CommentForm',
        'placeholder' : 'Komment yazın',
        'rows' : '2',
        }))
    def clean(self):
        comment_content = self.cleaned_data.get('comment_content')
        return {'comment_content' : comment_content,}
        