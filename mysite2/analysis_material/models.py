from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True, blank=True)
    name_document = models.CharField("Учебный материал", max_length=200)
    path_file = models.FileField("Файл", upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name_document

    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"slug": self.slug})

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

class Theme(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    name_theme = models.CharField(max_length=200)

    def __str__(self):
        return self.name_theme

class AnalysisTheme(models.Model):
    compatibility_theme = models.FloatField(default=0)

    def __str__(self):
        return self.compatibility_theme

class Relation_Theme_Analysis(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    analysis_theme = models.ForeignKey(AnalysisTheme, on_delete=models.CASCADE)

class CleanText(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    description_cleantext = models.TextField()

class Keyword(models.Model):
    cleantext = models.ForeignKey(CleanText, on_delete=models.CASCADE)
    description_keyword = models.CharField(max_length=100)
    periodicity_keyword = models.IntegerField(default=0)
