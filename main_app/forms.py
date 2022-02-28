from django. forms import ModelForm
from .models import Symbol

class SymbolForm(ModelForm):
    class Meta:
        model = Symbol
        fields = '__all__'