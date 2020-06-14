from django.test import TestCase

from analysis_material.models import Document

class DocumentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Document.objects.create(name_document='История', path_file='documents/1_2_главы.docx')

    def test_name_document_label(self):
        document = Document.objects.get(id=1)
        field_label = document._meta.get_field('name_document').verbose_name
        self.assertEquals(field_label,'Учебный материал')

    def test_uploaded_at_label(self):
        document = Document.objects.get(id=1)
        field_label = document._meta.get_field('uploaded_at').verbose_name
        self.assertEquals(field_label,'Время загрузки')

    def test_path_file_label(self):
        document = Document.objects.get(id=1)
        field_label = document._meta.get_field('path_file').verbose_name
        self.assertEquals(field_label,'Файл')

    def test_name_document_max_length(self):
        document = Document.objects.get(id=1)
        max_length = document._meta.get_field('name_document').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_name_document(self):    # проверка для метода __str__
        document = Document.objects.get(id=1)
        expected_object_name = document.name_document
        self.assertEquals(expected_object_name, str(document))

    def test_get_absolute_url(self):
        document = Document.objects.get(id=1)
        self.assertEquals(document.get_absolute_url(),'/1/')
