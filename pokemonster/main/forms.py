from django import forms

from pokemonster.common.mixins import FormWidgetsMixin
from pokemonster.main.models import Customon, Comment


class AddCustomonForm(FormWidgetsMixin, forms.ModelForm):
    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_widget_update()
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


class EditCustomonForm(FormWidgetsMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_widget_update()

    class Meta:
        model = Customon
        fields = ('name', 'type', 'photo')


class AddCommentForm(FormWidgetsMixin,  forms.ModelForm):

    def __init__(self, customon, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_widget_update()
        self.customon = customon
        self.owner=owner

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.customon = self.customon
        comment.owner = self.owner
        if commit:
            comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ('text',)
