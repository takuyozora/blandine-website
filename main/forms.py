from django.db.models import *
from ckeditor.widgets import CKEditorWidget
from main.models import Stage


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'
        exclude = ('photo_height', 'photo_width')
        widgets = {
            'description': CKEditorWidget(),
        }
