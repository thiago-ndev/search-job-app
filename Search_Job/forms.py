from django import forms

class FiltredForm(forms.Form):
    title_key_words = forms.CharField(label='Palavras Chaves:',
                                      max_length=100,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Ex: backend, Back-end, Desenvolvedor'}
                                      ))
    date_start = forms.DateField(
        label='Data de publicação:',
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Formato padrão de data do Django
            attrs={'type': 'date'}
        ),
        input_formats=['%Y-%m-%d']  # Aceitar este formato para entrada
    )

    description_required_keywords = forms.CharField(label='Skills:',
                                                    max_length=100,
                                                    widget=forms.TextInput(
                                                        attrs={'class': 'form-control',
                                                               'placeholder': 'Ex: C#, .Net'}
                                                    ))
