from django import forms


from .models import Thread


class AddThreadForm(forms.ModelForm):
    board_id = forms.IntegerField(widget=forms.HiddenInput)


    class Meta:
        model = Thread
        fields = ['title', 'title_img', 'data', 'board_id']


    def save(self, *args, **kwargs):
        thread_obj = super().save(commit=False)
        thread_obj.board_id = self.cleaned_data.get('board_id')
        thread_obj.save()
        return thread_obj
