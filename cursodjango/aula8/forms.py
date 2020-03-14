from django import forms
from .models import Pet

def external_valid_names(name):
    if name == rex:
        return False
    return True

class PetForm(forms.ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.upper == 'PUTINHO':
            raise forms.ValidationError("Nome muito ofensivo!!")
        return nome

    class Meta:
        model = Pet
        fields = '__all__'