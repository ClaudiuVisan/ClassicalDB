from django.forms import ModelForm
from musicdb.models import *


class ComposerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComposerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Compozitori
        fields = '__all__'


class CompositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompositionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Compozitii
        fields = '__all__'


class CatalogueForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CatalogueForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cataloage
        fields = '__all__'


class ComposerDeleteForm(ModelForm):
    class Meta:
        model = Compozitori
        fields = []


class CompositionDeleteForm(ModelForm):
    class Meta:
        model = Compozitii
        fields = []


class CatalogueDeleteForm(ModelForm):
    class Meta:
        model = Cataloage
        fields = []