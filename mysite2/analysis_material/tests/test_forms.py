from django.test import TestCase
import datetime
from django.utils import timezone
from analysis_material.forms import DocumentForm

class DocumentFormTest(TestCase):

    def test_document_form_name_field_label(self):
        form = DocumentForm()
        self.assertTrue(form.fields['name_document'].label == None or form.fields['name_document'].label == 'Учебный материал')

    def test_document_form_path_field_label(self):
        form = DocumentForm()
        self.assertTrue(form.fields['path_file'].label == None or form.fields['path_file'].label == 'Файл')
