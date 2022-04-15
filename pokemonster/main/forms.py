from django import forms

from pokemonster.main.models import Customon, Comment


class AddCustomonForm(forms.ModelForm):
    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner

    def save(self, commit=True):
        customon = super().save(commit=False)
        customon.owner = self.owner
        if commit:
            customon.save()
        return customon

    class Meta:
        model = Customon
        fields = ('name', 'type', 'photo')

from django import forms

from pokemonster.main.models import Customon


class AddCommentForm(forms.ModelForm):
    def __init__(self, customon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customon = customon

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.customon = self.customon
        if commit:
            comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ('text',)
