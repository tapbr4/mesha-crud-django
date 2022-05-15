from django.forms import DateField, ModelForm
from recursos.models import Recursos
from meshateste import settings

# Create the form class.
class RecursosForm(ModelForm):
    class Meta:
        data = DateField(input_formats=settings.DATE_INPUT_FORMATS)
        model = Recursos
        fields = ['nome', 'qtd', 'data']