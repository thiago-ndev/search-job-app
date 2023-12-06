from django import forms

class FiltredForm(forms.Form):
    title_key_words = forms.CharField(label='title keywords : ',max_length=100, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder': 'Ex: backend, Back-end, Desenvolvedor'}
    ))
    date_start = forms.CharField(label='date')

    description_required_keywords = forms.CharField(label='description required keywords : ',
                                                    max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ex: C#, .Net'}
    ))

