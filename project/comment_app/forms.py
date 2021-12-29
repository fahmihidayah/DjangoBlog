from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):

    def save(self, commit=True):
        comment : Comment = super(CommentForm, self).save(commit=False)
        comment.post = self.post
        comment.user = self.user
        if commit :
            comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ['message']