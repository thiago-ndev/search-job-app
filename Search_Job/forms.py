from django import forms

class FiltredForm(forms.Form):
    title_key_words = forms.CharField(label='Palavras Chaves:',
                                      max_length=100,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Ex: backend, Back-end, Desenvolvedor'}
                                      ))

    description_required_keywords = forms.CharField(label='Skills:',
                                                    max_length=100,
                                                    widget=forms.TextInput(
                                                        attrs={'class': 'form-control',
                                                               'placeholder': 'Ex: C#, .Net'}
                                                    ))
