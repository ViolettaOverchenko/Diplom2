from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)
    name_document = models.CharField("Учебный материал", max_length=200)
    path_file = models.FileField("Файл", upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #slug = AutoSlugField(populate_from='name_document')

    def __str__(self):
        return self.name_document

    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Учебный материал"
        verbose_name_plural = "Учебные материалы"

class AnalysisDocument(models.Model):
    compatibility_document = models.FloatField(default=0)

    def __str__(self):
        return self.compatibility_document

class Relation_Document_Analysis(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    analysis_document = models.ForeignKey(AnalysisDocument, on_delete=models.CASCADE)

class Keyword(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    description_keyword = models.CharField(max_length=100)
    periodicity_keyword = models.IntegerField(default=0)
