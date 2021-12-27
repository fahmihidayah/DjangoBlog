from django import forms
from .models import Post

from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 1000}))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(PostForm, self).__init__( *args, **kwargs)

    def save(self, commit=True):
        object: Post = super(PostForm, self).save(False)
        object.user = self.user
        if commit:
            object.save()
            self.save_m2m()
        return object
    
    class Meta:
        model = Post
        fields = ["image", "title", "content", "categories", "is_published", "is_banner" ]



class PostSearchForm(forms.Form):
    
    title = forms.CharField(required=False)

    content = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(PostSearchForm, self).__init__(*args, **kwargs)


