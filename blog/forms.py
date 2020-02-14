from django import forms

class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea,help_text="Enter comment about blog here")

    def clean_comment_text(self):
        data = self.cleaned_data['comment_text']
        return data