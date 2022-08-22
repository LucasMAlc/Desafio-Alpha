from pyexpat import model
from django import forms
from . models import Ativos

class CadastroAtivos(forms.ModelForm):
    class Meta:
        model = Ativos
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()